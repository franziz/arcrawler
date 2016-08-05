from ..exceptions import TestIsNotPassed
from ...	 	  import tools
import random
import math

class Preparator(object):
	""" This class will help the tester function to prepare the link_to_crawl
		Basically, the link_to_crawl should be source.LINK_TO_CRAWL.
		However, some of the test cannot use source.LINK_TO_CRAWL, so extending this class will be useful.
	"""
	def __init__(self):
		pass

	def get_links(self, source=None):
		assert source is not None, "source is not defined."

		sample_link = random.sample(source.LINK_TO_CRAWL, math.ceil(len(source.LINK_TO_CRAWL)*0.1))
		return sample_link

		