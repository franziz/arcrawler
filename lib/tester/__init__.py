import random
import math

class Tester:
	def __init__(self):
		pass

	def test(self, source=None):
		self.source = source
		self.links  = self.sample_links()

	def sample_links(self, size=0.1):
		""" This function will sample the link. The default sample is 10% of the total LINK_TO_CRAWL
		"""
		assert self.source is not None, "source is not defined."
		sample_links = random.sample(
					       self.source.LINK_TO_CRAWL, 
					       math.ceil(len(self.source.LINK_TO_CRAWL)*size)
					   )
		return sample_links