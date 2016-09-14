from urllib.parse 		  import urlparse
from lxml         		  import html
from ..network_tools 	  import NetworkTools
from .tools.field_factory import FieldFactory
from .backward    		  import Backward
from .            		  import exceptions
from ..           		  import tools
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
		self.domain        = NetworkTools.get_domain(self.link_to_crawl)

	def set_method(self, method):
		self.method = method
	#end def

	def get_threads(self):
		""" As the functionality follows its name, get_threads() function will return you a list of threads
		 	in the certain category link. This function will only accept if link_to_crawl, thread_xpath, and 
		 	network_tools variable are set.

		 	The limitation of this function is that the get_threads() function will only get threads
		 	inside the link_to_crawl. It means only single category level url will be crawled. 
		 	In order to crawl more than one category level url, you need to call get_threads() several times.
		"""
		assert self.link_to_crawl is not None, "link_to_crawl is not defined."
		assert self.thread_xpath  is not None, "thread_xpath is not defined."
		assert self.network_tools is not None, "network_tools is not defined."

		parser = FieldFactory.get_parser(FieldFactory.THREAD)
		self.threads = parser.parse(
					        network_tools = self.network_tools,
					                 link = self.link_to_crawl,
					         thread_xpath = self.thread_xpath
					   )
		return self.threads
	#end def

	def get_thread_link(self, thread=None):
		""" This function will get thread link based on the passed thread parameters
			
			parameters:
				- thread<lxml.html.HtmlElement> : thread element. Usually, you can get thread element from 
												  get_threads() function.

			return:
				- link<str> : a string of url from specific thread
		"""			
		parser = FieldFactory.get_parser(FieldFactory.THREAD_LINK)
		link   = parser.parse(
					            domain = self.domain,
				                thread = thread,
				     thread_link_xpath = self.thread_link_xpath
				 )
		return link

	def _make_engine(self, link=None):
		assert self.method is not None, "method is not defined."
		assert link        is not None, "link is not defined."
		if self.method == self.BACKWARD:
			assert self.last_page_xpath is not None, "last_page_xpath is not defined."
			assert self.prev_xpath      is not None, "prev_xpath is not defined."

			engine = Backward(
						         domain = self.domain,
						    thread_link = link, 
						last_page_xpath = self.last_page_xpath,
						     prev_xpath = self.prev_xpath,
					 	     post_xpath = self.post_xpath,
					 	  network_tools = self.network_tools
					 )
		return engine

	def crawl(self, thread=None, callback=None):
		""" crawl() function accept parameters.
			- thread   : thread parameter is lxml.html.HtmlElement object. Usually forum has multiple threads.
			    	 	 However, the function will only accept single thread. In order to accept multi thread
			    	 	 you need to call the crawl() function several times.
			- callback : a callback function. The callback function must accept 1 parameter called 'document'.
						 The callback will be called after finishing one single round of _crawl_posts() function.
						 So, you will get all the posts in certain page.
		"""
		assert thread                  is not None             , "Thread is not defined."
		assert type(thread)            is lxml.html.HtmlElement, "Wrong Thread type."
		assert callback                is not None             , "Callback is not defined."
		assert hasattr(callback, '__call__')                   , "Wrong Callback type."
		assert self.thread_link_xpath  is not None             , "Thread Link XPATH is not defined."
		assert self.domain             is not None             , "Domain is not defined."

		# TODO: if the result is more than one link, you need to produce a warning	
		link                = self.get_thread_link(thread)
		self.current_engine = self._make_engine(link=link)
		self.crawl_callback = callback
		self._run_crawler()
		#end if
	#end def

	def crawl_next(self):
		""" This function is a simple interface that call next() function from the engine method.
			For example, if you set the engine method is Backward, the crawl_next() function will call
			next() function inside Backward class. The next() function sometimes can be different 
			for each engine method.
		"""
		self.current_engine.next()
		self._run_crawler()
	#end def

	def _run_crawler(self):
		""" The _run_crawler() function cannot be crawled independently. It should call crawl() function first.
			Since the crawl() function initialize everything, the _run_crawler() does not need to initialize anything.
		"""
		assert self.current_engine is not None, "Please run crawl() first."
		assert self.crawl_callback is not None, "Please run crawl() first."

		posts     = self.current_engine.get_posts()
		documents = self._crawl_posts(posts=posts)
		self.crawl_callback(documents=documents)
	#end def

	def _crawl_posts(self, posts):
		""" This function will only crawl from given post. The basic behavior of this function is
			you give list of posts, and the crawler will crawl the post based on the field set in the
			src folder.

			The function will return you a list of documents. In normal circumstances, the _crawl_posts() function
			will return you documents with the same number of the posts that you passed.

			return:
			- documents : a list of documents. The documents is the result of posts parsing method. It just simply
						  parse the post in to structured data type.
		"""
		documents = []
		for post in posts:
			assert "permalink"         in self.fields, "permalink is not defined."
			assert self.current_engine is not None   , "current_engine is not defined."

			document = {}
			fields_parser = FieldFactory.get_parser(FieldFactory.FIELDS)
			date_parser   = FieldFactory.get_parser(FieldFactory.DATE)
			url_parser    = FieldFactory.get_parser(FieldFactory.URL)
			for field,props in self.fields.items():
				result = fields_parser.parse(
					 	      post = post, 
					 	     xpath = props["xpath"],
					 	     props = props,
					 	     field = field
						 )

				if "date" in props["data_type"]:
					# as a date format. it should convert the date to utc date time
					# if the date do not have timezone specific information, it will assume the the date is local system timezone
					result = date_parser.parse(result)
				elif "url" in props["data_type"]:
					result = url_parser.parse(value=result, domain=self.domain)
				document.update({field:result})
			document.update({"_thread_link":self.current_engine.thread_link})
			documents.append(document)
		return documents

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