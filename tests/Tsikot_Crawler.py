from forum_engine import Engine
from forum_engine import exceptions
from pymongo import MongoClient
import pymongo
import arrow
import bson.json_util
import json
import tools

class Crawler(object):

	def __init__(self):
		# initialize variables
		self.CRAWLER_NAME = 'Tsikot Crawler'
		self.LINK_TO_CRAWL = "https://www.tsikot.com/forums/racing-off-roading-fun-run-talk-16/"
		self.COUNTRY = 'PHL'
		self.THREAD_XPATH = '//ol//li[re:test(@id,\'thread*\')]'
		self.THREAD_LINK_XPATH = './/a[@class=\'title\']/@href'
		self.LAST_PAGE_XPATH = '//span[@class=\'first_last\']/a/@href'
		self.PREV_XPATH = '//a[@rel=\'prev\']/@href'
		self.POST_XPATH = '//ol//li[re:test(@class,\'postbit*\')]'
		self.FIELDS = '[{"published_date": {"single": true, "data_type": "date", "concat": true, "xpath": ".//span[@class=\'date\']//text()"}}, {"permalink": {"single": true, "data_type": "url", "concat": false, "xpath": ".//div[@class=\'postbody\']//span[@class=\'nodecontrols\']/a/@href"}}, {"author_name": {"single": true, "data_type": "string", "concat": false, "xpath": ".//a[re:test(@class,\'username*\')]//text()"}}, {"content": {"single": true, "data_type": "string", "concat": true, "xpath": ".//div[@class=\'content\']//text()"}}, {"title": {"single": true, "data_type": "string", "concat": false, "xpath": "//span[@class=\'threadtitle\']//text()"}}]'
	#end def

	def crawl_callback(self,documents):
		# preparing additional data in order to complete insertion
		assert len(documents)>0, "No document found."

		document = documents[0]
		document.update({"_country":self.COUNTRY})
		document.update({"_insert_time":arrow.utcnow().datetime})
		document.update({"_origin":self.LINK_TO_CRAWL})
		document.update({"_crawled_by":self.CRAWLER_NAME})
		
		# set some assertion validation
		assert len(document["content"]) > 0, "Content cannot be empty"
		assert "content" in document, "Content is not defined"
		
		print(bson.json_util.dumps(document,indent=4, separators=(",",":")))
	#end def

	def preflight_check(self):
		# check if has permalink field, because it is really critical
		has_permalink_field = False
		fields = json.loads(self.FIELDS)
		for field in fields:
			for key, value in field.items():
				if "permalink" in key:
					has_permalink_field = True
				#end if
			#end for
		#end for

		if  has_permalink_field :
			return True
		else:
			return False
		#end if
	#end def

	def crawl(self):
		# check database indexes
		assert self.preflight_check()==True, "[test][{}] Pre-Flight is not satisfied.".format(self.CRAWLER_NAME)

		global engine
		engine = Engine()
		engine.set_name(self.CRAWLER_NAME)
		engine.set_method(engine.BACKWARD)
		engine.set_link_to_crawl(self.LINK_TO_CRAWL)
		engine.set_thread_xpath(self.THREAD_XPATH)
		engine.set_thread_link_xpath(self.THREAD_LINK_XPATH)
		engine.set_last_page_xpath(self.LAST_PAGE_XPATH)
		engine.set_prev_xpath(self.PREV_XPATH)
		engine.set_post_xpath(self.POST_XPATH)

		fields = json.loads(self.FIELDS)
		for field in fields:
			for key,value in field.items():
				assert type(value) is dict, "[test][{}] Value inside the field's title should be in dict type".format(self.CRAWLER_NAME)
				engine.add_field(
					title=key,
					xpath=value["xpath"],
					single=value["single"],
					concat=value["concat"],
					data_type=value["data_type"]
				)
			#end for
		#end for

		threads = engine.get_threads()
		print("[test][{}] Total threads: {}".format(self.CRAWLER_NAME, len(threads)))
		try:
			assert len(threads) > 0, "[test][{}] No thread found.".format(self.CRAWLER_NAME)
			thread = threads[0]
			engine.crawl(thread, callback=self.crawl_callback)
		except exceptions.NoPrevious as no_prev:
			pass
		#end try
	#end def
#end class