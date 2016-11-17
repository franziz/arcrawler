from ..network_tools  import NetworkTools
from ..factory.parser import ParserFactory
from ..exceptions     import CannotFindPost, CannotSetValue, NotSupported, ParseError
from curtsies 		  import fmtstr
import logging

class PostExtractor:
	def __init__(self):
		self.logger = logging.getLogger(__name__)

	def extract(self, thread=None, xpath=None, attribute=None, **kwargs):
		""" Exceptions:
			- AssertionError
			- CannotFindPost
			- IncorrectXPATHSyntax (XPATHParser)

			This function will go to last_page of thread object and get all the post inside the page
		"""
		assert thread    is not None, "thread is not defined."
		assert xpath     is not None, "xpath is not defined."
		assert attribute is not None, "attribute is not defined."

		post    			= []
		extracted_documents = []
		network_tools       = kwargs.get("network_tools", NetworkTools(use_proxy=False))

		# Go to thread last page
		# and get all the post from xpath provided
		last_page = network_tools.parse(thread.last_page)

		xpath_parser = ParserFactory.get_parser(ParserFactory.XPATH)
		posts        = xpath_parser.parse(last_page, xpath)

		# Continue to other post even if you find an exception thrown by 
		# attr.value. This means, it is possible that one post does not have data,
		# but others have data. If the exception is caught, the logger system will report.
		for post in posts:
			try:
				extracted_document = {}
				for key,attr in attribute.items():
					attr.value = xpath_parser.parse(post, attr.xpath)
					extracted_document.update({key:attr.value})
				extracted_documents.append(extracted_document)
			except AssertionError as ex:
				self.logger.error(str(ex), exc_info=True)
			except CannotSetValue as ex:
				self.logger.error(str(ex), exc_info=True)
			except NotSupported as ex:
				self.logger.error(str(ex), exc_info=True)
			except ParseError as ex:
				self.logger.error(str(ex), exc_info=True)
		if len(extracted_documents) == 0:
			raise CannotFindPost("Number of post for %s is 0 post" % thread.last_page.encode("utf-8"))
		return extracted_documents