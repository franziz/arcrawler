from urllib.parse import urlparse
from lxml         import html
from .backward    import Backward
from .            import exceptions
from ..           import tools
import lxml
import bson.json_util
import requests
import copy

class Engine(object):
	def __init__(self):
		# method options
		self.BACKWARD          = -1

		self.link_to_crawl     = None
		self.domain            = None
		self.name              = ""
		
		# some xpath setting parameters
		self.thread_xpath      = None
		self.thread_link_xpath = None
		self.last_page_xpath   = None
		self.post_xpath        = None
		self.prev_xpath        = None
		self.method            = self.BACKWARD
		self.network_tools     = None
		
		# fields that required for crawler
		self.fields            = {}

		# some variables that maybe used
		self.current_engine    = None
		self.crawl_callback    = None		
	#end def

	def add_field(self, title=None, xpath=None, single=True, concat=False, data_type=None):
		assert title     is not None, "Title is not defined."
		assert xpath     is not None, "XPATH is not defined."
		assert data_type is not None, "Data Type is not defined."

		self.fields.update({
			title:{
				"xpath":xpath,
				"single":single,
				"concat":concat,
				"data_type":data_type
			}
		})
	#end def

	def set_network_tools(self, network_tools):
		self.network_tools = network_tools
	#end def

	def set_name(self, name):
		self.name = name
	#end def

	def set_prev_xpath(self, prev_xpath):
		self.prev_xpath = prev_xpath
	#end def

	def set_post_xpath(self, post_xpath):
		self.post_xpath = post_xpath
	#end def

	def set_last_page_xpath(self, last_page_xpath):
		self.last_page_xpath = last_page_xpath
	#end def

	def set_thread_xpath(self, thread_xpath):
		self.thread_xpath = thread_xpath
	#end def

	def set_thread_link_xpath(self, thread_link_xpath):
		self.thread_link_xpath = thread_link_xpath
	#end def

	def set_link_to_crawl(self,link_to_crawl):
		self.link_to_crawl = link_to_crawl
		self.domain        = '{uri.scheme}://{uri.netloc}/'.format(uri=urlparse(self.link_to_crawl))
	#end def

	def set_method(self, method):
		self.method = method
	#end def

	def get_threads(self):
		assert self.link_to_crawl is not None, "link_to_crawl is not defined."
		assert self.thread_xpath  is not None, "thread_xpath is not defined."
		assert self.network_tools is not None, "network_tools is not defined."

		tree         = self.network_tools.parse(self.link_to_crawl)
		self.threads = tools._xpath(parent=tree, syntax=self.thread_xpath)
		return self.threads
	#end def

	def crawl(self, thread=None, callback=None):
		assert thread                  is not None             , "Thread is not defined."
		assert type(thread)            is lxml.html.HtmlElement, "Wrong Thread type."
		assert callback                is not None             , "Callback is not defined."
		assert hasattr(callback, '__call__')                   , "Wrong Callback type."
		assert self.thread_link_xpath  is not None             , "Thread Link XPATH is not defined."
		assert self.domain             is not None             , "Domain is not defined."

		# TODO: if the result is more than one link, you need to produce a warning
		link = tools._xpath(parent=thread, syntax=self.thread_link_xpath)

		tools._assert(len(link)>0, exceptions.NoThreadLink("Ops! Cannot find the thread link"))
		link = link[0] if type(link) is list else link
		link = tools._expand_link(domain=self.domain, link=link)
		
		if self.method == self.BACKWARD:
			assert self.last_page_xpath is not None, "Last Page XPATH is not defined."
			assert self.prev_xpath      is not None, "Prev XPATH is not defined."

			backward            = Backward(
									         domain = self.domain,
									    thread_link = link, 
									last_page_xpath = self.last_page_xpath,
									     prev_xpath = self.prev_xpath,
									     post_xpath = self.post_xpath,
									  network_tools = self.network_tools
								)
			self.current_engine = backward
			self.crawl_callback = callback
			self._run_crawler()
		#end if
	#end def

	def crawl_next(self):
		self.current_engine.next()
		self._run_crawler()
	#end def

	def _run_crawler(self):
		assert self.current_engine is not None, "Please run Crawl() first."
		assert self.crawl_callback is not None, "Please run Crawl() first."

		posts     = self.current_engine.get_posts()
		documents = self._crawl_posts(posts=posts)
		self.crawl_callback(documents=documents)
	#end def

	def _crawl_posts(self, posts):
		documents = []
		for post in posts:

			# permalink is a must properties
			assert "permalink" in self.fields

			document = {}
			for field,props in self.fields.items():
				result = tools._xpath(parent=post, syntax=props["xpath"])
				
				try:
					tools._assert(len(result) > 0, exceptions.CannotFindXPATH("Cannot find {} given XPATH.".format(field)))
				except:
					result = []
					print("Cannot find {} given XPATH.".format(field))
					# from lxml import etree
					# print(etree.tostring(post,pretty_print=True))
				#end try

				# if the props is not single, but they want to concat, it means force it to single value and concat
				if (props["single"] and props["concat"]) or (not props["single"] and props["concat"]):
					result = " ".join(result)
					result = str(result)
				elif props["single"] and not props["concat"]:
					result = result[0] if type(result) is list and len(result)>0 else result
					result = str(result)
				else:
					result = list(result)
				#end if
				
				assert type(result) is str or type(result) is list

				# removing some unwanted data such as \xc2\xa0
				if type(result) is str:
					result = tools._clean_string(result)
				elif type(result) is list:
					result = [tools._clean_string(r) for r in result]
				#end if

				if "date" in props["data_type"]:
					# as a date format. it should convert the date to utc date time
					# if the date do not have timezone specific information, it will assume the the date is local system timezone
					if type(result) is str:
						result = tools._date_parser(result)
					elif type(result) is list:
						result = [tools._date_parser(r) for r in result]
					#end if
				elif "url" in props["data_type"]:
					if type(result) is str:
						result = tools._expand_link(domain=self.domain, link=result)
						#end if
					elif type(result) is list:
						result = [tools._expand_link(domain=self.domain, link=r) for r in result if "http://" not in r]
					#end if
				#end if

				document.update({field:result})
			#end for
			document.update({"_thread_link":self.current_engine.thread_link})
			documents.append(document)
		#end for
		return documents
	#end def

	def get_info(self):
		return{
			    "link_to_crawl" : self.link_to_crawl,
			           "domain" : self.domain,
			             "name" : self.name,
			     "thread_xpath" : self.thread_xpath,
			"thread_link_xpath" : self.thread_link_xpath,
			  "last_page_xpath" : self.last_page_xpath,
			       "post_xpath" : self.post_xpath,
			       "prev_xpath" : self.prev_xpath,
			           "method" : self.method,
			           "fields" : self.fields
		}
	#end def
#end class