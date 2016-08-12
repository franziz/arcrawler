from .                    import exceptions
from ..                   import tools
from .tools.field_factory import FieldFactory
import copy

class Backward(object):
	def __init__(self, domain=None, thread_link=None, last_page_xpath=None, prev_xpath=None, post_xpath=None, network_tools=None):
		assert domain          is not None, "domain is not defined."
		assert thread_link     is not None, "thread_link is not defined."
		assert last_page_xpath is not None, "last_page_xpath is not defined."
		assert prev_xpath      is not None, "prev_xpath is not defined."
		assert network_tools   is not None, "network_tools is not defined."
					
		self.domain            = domain
		self.thread_link  	   = thread_link
		self.post_xpath   	   = post_xpath
		self.prev_xpath   	   = prev_xpath
		self.network_tools 	   = network_tools
		self.last_page_xpath   = last_page_xpath
		self.current_page_link = self.get_last_page_link()
		self.current_page 	   = self.network_tools.parse(self.current_page_link)
		self.has_last_page     = True

		# Print out debug that cannot find last page link
		if self.current_page_link == self.thread_link:
			self.has_last_page = False
			print("[backward_engine][warning] Cannot find Last Page Link: {}".format(self.current_page_link.encode("utf-8")))		
	#end def	

	def get_last_page_link(self):
		parser 		   = FieldFactory.get_parser(FieldFactory.LAST_PAGE_LINK)
		last_page_link = parser.parse(
							   network_tools = self.network_tools,
							     thread_link = self.thread_link,
							 last_page_xpath = self.last_page_xpath
						 )
		return last_page_link


	def get_prev_link(self):
		assert self.prev_xpath is not None, "prev_xpath is not defined."
		assert self.domain     is not None, "domain is not defined."

		parser = FieldFactory.get_parser(FieldFactory.PREV_LINK)
		prev_link = parser.parse(
							domain = self.domain,
						      page = self.current_page,
						prev_xpath = self.prev_xpath
					)
		return prev_link


	def get_posts(self, post_xpath=None):
		print("[backward_engine][debug] Current Page Link: %s" % self.current_page_link)
		post_xpath = self.post_xpath if post_xpath is None else post_xpath
		parser     = FieldFactory.get_parser(FieldFactory.POST)
		posts      = parser.parse(
				               page = self.current_page,
				         post_xpath = post_xpath
					 )
		posts      = list(reversed(posts))
		
		return posts
	#end def

	def next(self):
		# assert self.prev_xpath is not None, "prev_xpath is not defined."
		# assert self.domain is not None, "domain is not defined."

		# prev_link = tools._xpath(parent=self.current_page, syntax=self.prev_xpath)

		# tools._assert(len(prev_link)>0, exceptions.NoPrevious("Ops! No more previous link."))

		# prev_link = prev_link[0]
		# prev_link = tools._expand_link(domain=self.domain, link=prev_link)
		prev_link              = self.get_prev_link()
		self.current_page      = self.network_tools.parse(prev_link)
		self.current_page_link = prev_link
	#end def
#end class