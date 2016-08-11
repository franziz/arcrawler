from ...     	  import tools
from .base 	 	  import Preparator as BasePreparator
from .thread 	  import ThreadPreparator
from urllib.parse import urlparse
import copy

class PostPreparator(BasePreparator):
	def __init__(self, last_post_only=False):
		self.last_post_only = last_post_only

	def get_links(self, source=None):	
		""" This function will call ThreadPreparator Class in order to get all the threads.
			After getting all the threads, the function will get all the last page link. 
			The function assume that all LAST_PAGE_XPATH is correct. Make sure LAST_PAGE_XPATH is tested before calling
			this funciton.

			return 
			['http://forum.com/category/thread/last-page-1', 'http://forum.com/category/thread/last-page-2']
		"""
		assert source is not None, "source is not defined."

		domain  	 = '{uri.scheme}://{uri.netloc}/'.format(uri=urlparse(source.LINK_TO_CRAWL[0])) # In order to get domain, I need to get a sample URL
																									# Getting sample url from LINK_TO_CRAWL should be good approach
																									# since the URL from LINK_TO_CRAWL is the main URL
		preparator   = ThreadPreparator()
		threads      = preparator.get_links(source)
		result_links = []
		for thread in threads:
			page = source.NETWORK_TOOLS.parse(thread)
			link = tools._xpath(page, source.LAST_PAGE_XPATH)
			if len(link) == 0:
				result = copy.copy(thread)
			else:
				if not type(link) is list:
					link = [link]
				result = copy.copy(link[0]) # Assuming that LAST_PAGE_XPATH will return the same array content.
			result_links.append(result)
		result_links = [tools._expand_link(domain, l) for l in result_links]
		if self.last_post_only:
			return [result_links[-1]] if len(result_links) > 0 else []
		return result_links