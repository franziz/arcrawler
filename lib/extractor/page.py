from ..factory.parser     import ParserFactory
from ..factory.generator  import GeneratorFactory
from ..exceptions         import CannotFindPrevLink
from ..obj.thread         import Thread
from ..network_tools      import NetworkTools
import logging

class ArticlePageExtractor:
	""" Return:
		articles: All article link from given link
	"""
	def __init__(self):
		pass

	def extract(self, link=None, xpath=None, **kwargs):
		assert link  is not None, "link is not defined."
		assert xpath is not None, "xpath is not defined."

		network_tools = kwargs.get("network_tools", NetworkTools(use_proxy=False))
		page          = network_tools.parse(link)
		# TODO:
		

class LastPageExtractor:
	def __init__(self, **kwargs):
		self.logger = logging.getLogger(__name__)
		self.domain = kwargs.get("domain",None)

	def extract(self, thread_link=None, xpath=None, **kwargs):
		""" this function will return
			- AssertionError (LinkGenerator)
			- IncorrectXPATHSyntax (XPATHParser)

			Return:
			last_page : will return None or <str>
		"""
		assert thread_link  is not None, "thread is not defined."
		assert xpath        is not None, "xpath is not defined."
		assert self.domain  is not None, "domain is not defined."

		network_tools = kwargs.get("network_tools", NetworkTools(use_proxy=False))
		current_page  = network_tools.parse(thread_link)

		last_page    = []
		xpath_parser = ParserFactory.get_parser(ParserFactory.XPATH)
		last_page    = xpath_parser.parse(current_page, xpath)

		# Make it as None if cannot find any last_page
		if len(last_page) == 0:
			last_page = thread_link
		if type(last_page) is list:
			last_page = last_page[0]

		generator = GeneratorFactory.get_generator(GeneratorFactory.LINK)
		last_page = generator.generate(self.domain, last_page)

		return last_page

class PrevPageExtractor:
	def __init__(self, **kwargs):
		self.logger = logging.getLogger(__name__)
		self.domain = kwargs.get("domain",None)

	def extract(self, thread=None, xpath=None, **kwargs):
		""" Exceptions:
			- AssertionError (LinkGenerator)
			- CannotFindPrevLink
			- IncorrectXPATHSyntax (XPATHParser)
		"""
		assert thread       is not None, "last_page is not defined."
		assert xpath        is not None, "xpath is not defiend."
		assert self.domain  is not None, "domain is not defined."
		assert type(thread) is Thread  , "incorrect thread data type."

		network_tools = kwargs.get("network_tools",NetworkTools(use_proxy=False))
		last_page     = network_tools.parse(thread.last_page)
		
		xpath_parser = ParserFactory.get_parser(ParserFactory.XPATH)
		prev_link    = xpath_parser.parse(last_page, xpath)

		# Make it as None if cannot find any prev_link
		if len(prev_link) == 0:
			prev_link = None
		if type(prev_link) is list:
			prev_link = prev_link[0]

		if prev_link is None:
			raise CannotFindPrevLink("Cannot find prev link.")
		
		generator = GeneratorFactory.get_generator(GeneratorFactory.LINK)
		prev_link = generator.generate(self.domain, prev_link)
		
		return prev_link