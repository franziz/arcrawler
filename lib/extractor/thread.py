from ..network_tools     import NetworkTools
from ..factory.parser    import ParserFactory
from ..factory.generator import GeneratorFactory
from ..obj.thread        import Thread
from ..exceptions        import CannotFindThreadLink, ExtractError
from .page               import LastPageExtractor
import copy

class ThreadExtractor:
	def __init__(self):
		pass

	def extract(self, link=None, thread_xpath=None, thread_link_xpath=None, last_page_xpath=None, **kwargs):
		assert link              is not None, "link is not defined."
		assert thread_xpath      is not None, "thread_xpath is not defined."
		assert thread_link_xpath is not None, "thread_link_xpath is not defined."
		assert last_page_xpath   is not None, "last_page_xpath is not defined."

		network_tools = kwargs.get("network_tools",NetworkTools(use_proxy=False))
		domain        = NetworkTools.get_domain(link)
		page          = network_tools.parse(link)
		xpath_parser  = ParserFactory.get_parser(ParserFactory.XPATH)
		threads       = xpath_parser.parse(page, thread_xpath)

		extracted_threads = []
		for thread in threads:
			try:
				extracted_thread      = Thread()
				extractor             = ThreadLinkExtractor(domain=domain)
				extracted_thread.link = extractor.extract(thread, thread_link_xpath)

				if extracted_thread.link is None:
					raise CannotFindThreadLink("Cannot find thread link for %s" % link)

				extractor       		   = LastPageExtractor(domain=domain)
				extracted_thread.last_page = extractor.extract(
					       thread = extracted_thread, 
					        xpath = last_page_xpath, 
					network_tools = network_tools
				)
				
				if extracted_thread.last_page is None:
					extracted_thread.last_page = copy.copy(extracted_thread.link)

				extracted_thread.element   = copy.deepcopy(page)
				extracted_threads.append(extracted_thread)
			except CannotFindThreadLink as ex:
				print(fmtstr("[thread_extractor][error] %s" % ex,"red"))
			except ExtractError as ex:
				print(fmtstr("[thread_extractor][error] %s" % ex,"red"))
		return extracted_threads

class ThreadLinkExtractor:
	def __init__(self, **kwargs):
		self.domain = kwargs.get("domain",None)

	def extract(self, thread=None, xpath=None):
		assert thread 	   is not None, "thread is not defined."
		assert xpath       is not None, "xpath is not defined."
		assert self.domain is not None, "domain is not defined."

		xpath_parser = ParserFactory.get_parser(ParserFactory.XPATH)
		thread_link  = xpath_parser.parse(thread, xpath)

		if len(thread_link) == 0: 
			raise ExtractError("Cannot extract thread link from thread.")

		if type(thread_link) is list:
			thread_link = thread_link[0]

		generator   = GeneratorFactory.get_generator(GeneratorFactory.LINK)
		thread_link = generator.generate(self.domain, thread_link)

		return thread_link