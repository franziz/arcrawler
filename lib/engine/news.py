from lib.network_tools     import NetworkTools
from lib.factory.extractor import ExtractorFactory
from lib.factory.generator import GeneratorFactory
from lib.factory.validator import ValidatorFactory

class NewsEngine:
	def __init__(self, **kwargs):
		self.name 				  = kwargs.get("name",None)
		self.country			  = kwargs.get("country", None)
		self.category_link 		  = kwargs.get("category_link", None)
		self.article_xpath 		  = kwargs.get("article_xpath", None)
		self.title_xpath 		  = kwargs.get("title_xpath", None)
		self.published_date_xpath = kwargs.get("published_date_xpath", None)
		self.author_name_xpath    = kwargs.get("author_name_xpath", None)
		self.content_xpath        = kwargs.get("content_xpath", None)
		self.network_tools        = kwargs.get("network_tools", NetworkTools(use_proxy=False))

	def crawl(self, saver=None):
		assert self.category_link        is not None, "category_link is not defined."
		assert self.article_xpath        is not None, "article_xpath is not defined."
		assert self.title_xpath          is not None, "title_xpath is not defined."
		assert self.published_date_xpath is not None, "published_date_xpath is not defined."
		assert self.author_name_xpath    is not None, "author_name_xpath is not defined."
		assert self.content_xpath        is not None, "content_xpath is not defined."
		assert saver                     is not None, "saver is not defined."

		extractor = ExtractorFactory.get_extractor(ExtractorFactory.ARTICLE_LINK)
		articles  = extractor.extract(self.category_link, self.article_xpath, network_tools=self.network_tools)
		print("[NewsEngine] Got %s articles" % len(articles))
		
		for article in articles:
			extractor = ExtractorFactory.get_extractor(ExtractorFactory.ARTICLE)
			article   = extractor.extract(
				             article = article,
				         title_xpath = self.title_xpath,
				published_date_xpath = self.published_date_xpath,
				   author_name_xpath = self.author_name_xpath,
				       content_xpath = self.content_xpath
			)

			generator = GeneratorFactory.get_generator(GeneratorFactory.POST_DATA)
			article   = generator.generate(article, origin=self.category_link, country=self.country, crawled_by=self.name)
			
			validator = ValidatorFactory.get_validator(ValidatorFactory.ARTICLE)
			validator.validate(article)

			saver.save(article)