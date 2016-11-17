from ..factory.parser    import ParserFactory
from ..factory.generator import GeneratorFactory
from ..network_tools     import NetworkTools
from ..exceptions        import CannotFindThread, CannotFindThreadLink
from ..obj.thread        import Thread
import logging
import copy

class ThreadExtractor:
	def __init__(self):
		self.logger = logging.getLogger(__name__)

	def extract(self, link=None, xpath=None, **kwargs):
		""" Exceptions:
			- AssertionError
			- CannotFindThread
			- IncorrectXPATHSyntax (XPATHParser)
		"""
		assert link  is not None, "link is not defined."
		assert xpath is not None, "xpath is not defined."

		network_tools = kwargs.get("network_tools",NetworkTools(use_proxy=False))
		domain        = NetworkTools.get_domain(link)
		page          = network_tools.parse(link)

		threads		  = []		
		xpath_parser  = ParserFactory.get_parser(ParserFactory.XPATH)
		threads       = xpath_parser.parse(page, xpath)

		# Cannot find thread
		if len(threads) == 0:
			raise CannotFindThread("Cannot find thread!")

		for thread in threads:
			extracted_thread = Thread()
			extracted_thread.element = copy.deepcopy(thread)
			yield extracted_thread

class ThreadLinkExtractor:
	def __init__(self, **kwargs):
		self.logger = logging.getLogger(__name__)
		self.domain = kwargs.get("domain", None)

	def extract(self, thread=None, xpath=None, **kwargs):
		""" Exceptions:
			- AssertionError (LinkGenerator)
			- IncorrectXPATHSyntax (XPATHParser)
			- CannotFindThreadLink
		"""
		assert thread      is not None, "thread is not defined."
		assert xpath       is not None, "xpath is not defined."
		assert self.domain is not None, "domain is not defined."

		result = None
		link   = None
		
		xpath_parser = ParserFactory.get_parser(ParserFactory.XPATH)
		link         = xpath_parser.parse(thread, xpath)

		if type(link) is list:
			link = copy.copy(link[0])

		if len(link) == 0:
			raise CannotFindThreadLink("Cannot find thread link!")
		
		generator = GeneratorFactory.get_generator(GeneratorFactory.LINK)
		result    = generator.generate(self.domain, link)
		return result