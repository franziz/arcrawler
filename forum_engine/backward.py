from . import exceptions
import tools
import copy

class Backward(object):
	def __init__(self, domain=None, thread_link=None, last_page_xpath=None, prev_xpath=None, post_xpath=None):
		assert domain is not None, "Domain is not defined."
		assert thread_link is not None, "Thread Link is not defined."
		assert last_page_xpath is not None, "Last Page XPATH is not defined."
		assert prev_xpath is not None, "Prev XPATH is not defined."
			
		self.domain = domain
		self.thread_link = thread_link
		self.post_xpath = post_xpath
		self.prev_xpath = prev_xpath

		self.current_page = tools._parse(self.thread_link)
		self.current_page_link = copy.deepcopy(self.thread_link)

		try:
			last_page_link = tools._xpath(parent=self.current_page, syntax=last_page_xpath)[0]
			last_page_link = tools._expand_link(domain=domain, link=last_page_link)
			self.current_page = tools._parse(last_page_link)
			self.current_page_link = last_page_link
		except IndexError as ex:
			print("Cannot find Last Page Link: {}".format(self.current_page_link))
		except:
			raise
		#end try
	#end def

	def get_posts(self):
		assert self.current_page is not None, "Current Page is not defined."
		assert self.post_xpath is not None, "Post XPATH is not defined."

		posts = tools._xpath(parent=self.current_page, syntax=self.post_xpath)
		posts = list(reversed(posts))

		return posts
	#end def

	def next(self):
		assert self.prev_xpath is not None, "Prev XPATH is not defined."
		assert self.domain is not None, "Domain is not defined."

		prev_link = tools._xpath(parent=self.current_page, syntax=self.prev_xpath)

		tools._assert(len(prev_link)>0, exceptions.NoPrevious("Ops! No more previous link."))

		prev_link = prev_link[0]
		prev_link = tools._expand_link(domain=self.domain, link=prev_link)

		self.current_page = tools._parse(prev_link)
		self.current_page_link = prev_link
	#end def
#end class