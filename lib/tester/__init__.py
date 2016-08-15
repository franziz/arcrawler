from ..forum_engine.engine import Engine
import random
import math

class Tester:
	def __init__(self):
		pass

	def test(self, source=None):
		self.source    = source
		self.links     = self.sample_links()

	def prepare_engine(self, **kwargs):
		source = kwargs.get("source", self.source)
		assert source is not None, "source is not defined."

		engine = Engine()
		engine.set_name(source.CRAWLER_NAME)
		engine.set_method(engine.BACKWARD)		
		engine.set_thread_xpath(source.THREAD_XPATH)
		engine.set_thread_link_xpath(source.THREAD_LINK_XPATH)
		engine.set_last_page_xpath(source.LAST_PAGE_XPATH)
		engine.set_prev_xpath(source.PREV_XPATH)
		engine.set_post_xpath(source.POST_XPATH)
		engine.set_network_tools(source.NETWORK_TOOLS)
		return engine

	def sample_links(self, size=0.1):
		""" This function will sample the link. The default sample is 10% of the total LINK_TO_CRAWL
		"""
		assert self.source is not None, "source is not defined."
		sample_links = random.sample(
					       self.source.LINK_TO_CRAWL, 
					       math.ceil(len(self.source.LINK_TO_CRAWL)*size)
					   )
		return sample_links