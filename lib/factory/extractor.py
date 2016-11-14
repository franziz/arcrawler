from ..extractor.thread  import ThreadExtractor, ThreadLinkExtractor
from ..extractor.page    import PrevPageExtractor, LastPageExtractor
from ..extractor.post    import PostExtractor
from ..extractor.link    import ArticleLinkExtractor
from ..extractor.article import ArticleExtractor

class ExtractorFactory:
	THREAD       = 0
	THREAD_LINK  = 1
	PREV_PAGE    = 2
	POST         = 3
	LAST_PAGE    = 4
	ARTICLE_LINK = 5
	ARTICLE      = 6

	def __init__(self):
		pass

	@classmethod
	def get_extractor(self, extractor_name=None):
		assert extractor_name is not None, "extractor_name is not defined."

		if extractor_name == ExtractorFactory.THREAD:
			return ThreadExtractor()
		elif extractor_name == ExtractorFactory.THREAD_LINK:
			return ThreadLinkExtractor()
		elif extractor_name == ExtractorFactory.PREV_PAGE:
			return PrevPageExtractor()
		elif extractor_name == ExtractorFactory.POST:
			return PostExtractor()
		elif extractor_name == ExtractorFactory.LAST_PAGE:
			return LastPageExtractor()
		elif extractor_name == ExtractorFactory.ARTICLE_LINK:
			return ArticleLinkExtractor()
		elif extractor_name == ExtractorFactory.ARTICLE:
			return ArticleExtractor()
