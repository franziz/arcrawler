from ..network_tools     import NetworkTools
from ..factory.parser    import ParserFactory
from ..factory.generator import GeneratorFactory
from ..exceptions        import CannotFindArticleLink
import copy

class ArticleLinkExtractor:
	def __init__(self):
		pass

	def extract(self, home=None, xpath=None, **kwargs):
		""" Exceptions
			- AssertionError (LinkGenerator)
			- IncorrectXPATHSyntax (XPATHParser)
			- CannotFindArticleLink
		"""
		assert home  is not None, "home is not defined."
		assert xpath is not None, "xpath is not defined."

		network_tools = kwargs.get("network_tools", NetworkTools(use_proxy=False))
		domain        = NetworkTools.get_domain(home)
		page          = network_tools.parse(home)

		parser = ParserFactory.get_parser(ParserFactory.XPATH)
		links  = parser.parse(page, xpath)

		if type(links) is not list:
			links = copy.deepcopy([links])

		generator = GeneratorFactory.get_generator(GeneratorFactory.LINK)
		links     = [generator.generate(domain=domain, link=link) for link in links]

		if len(links) == 0:
			raise CannotFindArticleLink("Cannot find article link for %s" % home.encode("utf-8"))

		return links
