from urllib.parse import urlparse
from .exceptions  import TestIsNotPassed
from .base 		  import FieldTester
from .. 		  import tools
import lxml
import copy

class UrlTester(FieldTester):
	def __init__(self, **kwargs):
		super(UrlTester, self).__init__(**kwargs)

	def test(self, object_to_test=None, link=None):
		""" This function will test the url by trying to connect.
			The assumption is if the url cannot be parsed, it means that the url is not valied.
			However, based on that assumption, slow connection can cause a trouble.
			As a result, need to do further check if something goes wrong
		"""
		assert object_to_test      is not None, "object_to_test is not defined."

		if len(object_to_test) == 0: 
				raise TestIsNotPassed("No test object.")

		url     = copy.copy(object_to_test)
		url     = self._prepare_value(url)				
		results = []
		if type(url) is str:
			results.append(self.validate_url(url))
		elif type(url) == list:
			results = [self.validate_url(u) for u in url]
		if False in results:
			raise TestIsNotPassed("Not a valid URL")

	def validate_url(self, url=None):
		assert url 		   is not None, "url is not defined."
		assert self.source is not None, "source is not defined."

		domain = '{uri.scheme}://{uri.netloc}/'.format(uri=urlparse(self.source.LINK_TO_CRAWL[0])) # Using LINK_TO_CRAWL variable will help to make the domain.
																								   # Assumming that the LINK_TO_CRAWL is a complete URL set.
		url    = tools._expand_link(domain, url)
		html   = self.source.NETWORK_TOOLS.parse(url, parse=False)		
		if html == "<html></html>":
			return False
		else:
			return True