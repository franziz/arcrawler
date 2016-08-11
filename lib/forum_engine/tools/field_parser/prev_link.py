from .             import Parser
from ....  		   import tools
from ...exceptions import NoPrevious
import lxml

class PrevLink(Parser):
	def __init__(self):
		pass

	def parse(self, domain=None, page=None, prev_xpath=None):
		assert domain     is not None			  , "domain is not defined."
		assert page       is not None			  , "page is not defined."
		assert prev_xpath is not None		      , "prev_xpath is not defined."
		assert type(page) is lxml.html.HtmlElement, "incorrect page data type."

		prev_link = tools._xpath(page, prev_xpath)

		if len(prev_link) == 0:
			raise NoPrevious("Ops! No more previous link.")
		if not type(prev_link) is list:
			prev_link = [prev_link]
		prev_link = prev_link[0]
		prev_link = tools._expand_link(domain,prev_link)
		return prev_link