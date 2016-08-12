from .             import Parser
from ...exceptions import NoThreadLink
from ....          import tools
import lxml

class ThreadLink(Parser):
	def __init__(self):
		pass

	def parse(self, domain=None, thread=None, thread_link_xpath=None):
		assert thread            is not None             , "thread is not defined."
		assert type(thread)      is lxml.html.HtmlElement, "incorrect thread data type."
		assert thread_link_xpath is not None             , "thread_link_xpath is not defined."
		assert domain 			 is not None 			 , "domain is not defined."
		link = tools._xpath(thread, thread_link_xpath)
		
		if len(link) == 0:
			raise NoThreadLink("No thread link.")
		link = link[0] if type(link) is list else link
		link = tools._expand_link(domain,link)
		return link