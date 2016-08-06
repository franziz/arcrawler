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

		tree         = self.network_tools.parse(self.link_to_crawl)
		self.threads = tools._xpath(parent=tree, syntax=self.thread_xpath)
		return self.threads
	#end def

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

			# permalink is a must properties
			assert "permalink" in self.fields

			document = {}
			for field,props in self.fields.items():
				result = tools._xpath(parent=post, syntax=props["xpath"])
				
				try:
					tools._assert(len(result) > 0, exceptions.CannotFindXPATH("Cannot find {} given XPATH.".format(field)))
				except:
					result = []
					print("[arcrawler][error] Cannot find {} given XPATH.".format(field))
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