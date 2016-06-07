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
		self.CRAWLER_NAME = 'Kaskus Crawler'
		self.LINK_TO_CRAWL = "http://www.kaskus.co.id/forum/570/kendaraan-roda-4"
		self.COUNTRY = 'IDN'
		self.THREAD_XPATH = '//div[@class=\'post-title\']'
		self.THREAD_LINK_XPATH = './a/@href'
		self.LAST_PAGE_XPATH = '//a[@class=\'tooltips last-page\']/@href'
		self.PREV_XPATH = '//a[@class=\'tooltips previous-page\']/@href'
		self.POST_XPATH = '//div[@class=\'row nor-post\']'
		self.FIELDS = '[{"published_date": {"data_type": "date", "single": true, "xpath": ".//time[@class=\'entry-date\']/@datetime", "concat": false}}, {"permalink": {"data_type": "url", "single": true, "xpath": ".//div[@class=\'permalink\']/a/@href", "concat": false}}, {"author_name": {"data_type": "string", "single": true, "xpath": ".//span[@itemprop=\'name\']//text()", "concat": false}}, {"author_id": {"data_type": "string", "single": true, "xpath": ".//div[@class=\'user-name\']/@data-userid", "concat": false}}, {"content": {"data_type": "string", "single": true, "xpath": ".//div[@class=\'entry\']//text()", "concat": true}}, {"title": {"data_type": "string", "single": true, "xpath": "//div[@class=\'current\']/text()", "concat": false}}]'
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