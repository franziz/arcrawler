from ..factory.parser    import ParserFactory
from ..factory.generator import GeneratorFactory
from ..obj.thread        import Thread
from ..network_tools     import NetworkTools

class LastPageExtractor:
	def __init__(self, **kwargs):
		self.domain = kwargs.get("domain",None)

	def extract(self, thread=None, xpath=None, **kwargs):
		""" Return:
			last_page : will return None or <str>
		"""
		assert thread 	    is not None, "thread is not defined."
		assert xpath        is not None, "xpath is not defined."
		assert self.domain  is not None, "domain is not defined."
		assert type(thread) is Thread  , "incorrect thread data type."

		network_tools = kwargs.get("network_tools", NetworkTools(use_proxy=False))
		current_page  = network_tools.parse(thread.link)

		xpath_parser = ParserFactory.get_parser(ParserFactory.XPATH)
		last_page    = xpath_parser.parse(current_page, xpath)
		
		# Make it as None if cannot find any last_page
		if type(last_page) is list:
			if len(last_page) == 0: last_page = [None]
			last_page = last_page[0]

		if last_page is not None:
			generator = GeneratorFactory.get_generator(GeneratorFactory.LINK)
			last_page = generator.generate(self.domain, last_page)
		return last_page

class PrevPageExtractor:
	def __init__(self, **kwargs):
		self.domain = kwargs.get("domain",None)

	def extract(self, thread=None, xpath=None, **kwargs):
		assert thread      is not None, "last_page is not defined."
		assert xpath       is not None, "xpath is not defiend."
		assert self.domain is not None, "domain is not defined."
		assert type(thread) is Thread  , "incorrect thread data type."

		network_tools = kwargs.get("network_tools",NetworkTools(use_proxy=False))
		last_page     = network_tools.parse(thread.last_page)

		xpath_parser = ParserFactory.get_parser(ParserFactory.XPATH)
		prev_link    = xpath_parser.parse(last_page, xpath)

		# Make it as None if cannot find any last_page
		if type(prev_link) is list:
			if len(prev_link) == 0: prev_link = [None]
			prev_link = prev_link[0]

		if prev_link is not None:
			generator = GeneratorFactory.get_generator(GeneratorFactory.LINK)
			prev_link = generator.generate(self.domain, prev_link)
		return prev_link