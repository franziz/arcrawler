from ..network_tools     import NetworkTools
from ..factory.extractor import ExtractorFactory
from ..factory.generator import GeneratorFactory
from ..factory.validator import ValidatorFactory
from ..exceptions        import ValidationError, CannotSetValue, NotSupported, ParseError
from curtsies 			 import fmtstr
import logging

class NewsEngine:
	def __init__(self, **kwargs):
		self.logger               = logging.getLogger(__name__)
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
		""" Exceptions:
			- AssertionError (ArticleLinkExtractor, ArticleExtractor, PostDataGenerator, ArticleSaver)
			- IncorrectXPATHSyntax (ArticleLinkExtractor, ArticleExtractor)
			- CannotFindArticleLink (ArticleLinkExtractor)
		"""
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
		
		for article_link in articles:
			try:
				extractor = ExtractorFactory.get_extractor(ExtractorFactory.ARTICLE)
				article   = extractor.extract(
					             article = article_link,
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
			except ValidationError as ex:
				self.logger.error(str(ex), exc_info=True)
			except CannotSetValue as ex:
				self.logger.warning(str(ex), exc_info=True)
			except NotSupported as ex:
				self.logger.error(str(ex), exc_info=True)
			except ParseError as ex:
				self.logger.error(str(ex), exc_info=True)