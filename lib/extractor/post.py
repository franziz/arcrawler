from ..network_tools  import NetworkTools
from ..factory.parser import ParserFactory
from ..exceptions     import CannotSetValue, CannotFindPost
from curtsies 		  import fmtstr

class PostExtractor:
	def __init__(self):
		pass

	def extract(self, thread=None, xpath=None, attribute=None, **kwargs):
		""" This function will go to last_page of thread object and get all the post inside the page
		"""
		assert thread    is not None, "thread is not defined."
		assert xpath     is not None, "xpath is not defined."
		assert attribute is not None, "attribute is not defined."

		network_tools = kwargs.get("network_tools", NetworkTools(use_proxy=False))

		# Go to thread last page
		# and get all the post from xpath provided
		last_page    = network_tools.parse(thread.last_page)
		xpath_parser = ParserFactory.get_parser(ParserFactory.XPATH)
		posts        = xpath_parser.parse(last_page, xpath)

		extracted_documents = []
		for post in posts:
			try:
				extracted_document = {}
				for key,attr in attribute.items():
					attr.value = xpath_parser.parse(post, attr.xpath)
					extracted_document.update({key:attr.value})
				extracted_documents.append(extracted_document)
			except CannotSetValue as ex:
				print(fmtstr("[PostExtractor][warning] %s" % ex, "yellow"))
		if len(extracted_documents) == 0:
			raise CannotFindPost("Number of post for %s is 0 post" % thread.last_page.encode("utf-8"))
		return extracted_documents