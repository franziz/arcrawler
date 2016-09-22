from ..extractor.thread import ThreadExtractor
from ..extractor.page   import PrevPageExtractor, LastPageExtractor
from ..extractor.post   import PostExtractor

class ExtractorFactory:
	THREAD    = 0
	PREV_PAGE = 1
	POST      = 2
	LAST_PAGE = 3

	def __init__(self):
		pass

	@classmethod
	def get_extractor(self, extractor_name=None):
		assert extractor_name is not None, "extractor_name is not defined."

		if extractor_name == ExtractorFactory.THREAD:
			return ThreadExtractor()
		elif extractor_name == ExtractorFactory.PREV_PAGE:
			return PrevPageExtractor()
		elif extractor_name == ExtractorFactory.POST:
			return PostExtractor()
		elif extractor_name == ExtractorFactory.LAST_PAGE:
			return LastPageExtractor()
