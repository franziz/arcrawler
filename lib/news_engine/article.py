from ..network_tools import NetworkTools
from ..              import tools
from .parser         import Parser
from .               import exceptions
import difflib

class Article(object):
	def __init__(self):
		self.url            = None
		self.title          = None
		self.domain         = None
		self.author         = None
		self.content        = None
		self.published_date = None
		self.network_tools  = NetworkTools(use_proxy=False)
		self.parser         = Parser()

		# xpath variables
		self.title_xpath          = None
		self.author_xpath         = None
		self.content_xpath        = None
		self.published_date_xpath = None

	def extract(self):
		assert self.url                  is not None, "url is not defined."
		assert self.title_xpath          is not None, "title_xpath is not defined."
		assert self.author_xpath         is not None, "authors_xpath is not defined."
		assert self.content_xpath        is not None, "content_xpath is not defined."
		assert self.published_date_xpath is not None, "published_date_xpath is not defined."

		page                = self.network_tools.parse(self.url)
		self.title          = tools._xpath(page, self.title_xpath)
		self.title          = "".join(self.title)
		self.content        = tools._xpath(page, self.content_xpath)
		self.content        = "".join(self.content)
		self.author         = tools._xpath(page, self.author_xpath)
		self.author         = "".join(self.author)
		self.published_date = tools._xpath(page, self.published_date_xpath)
		self.published_date = "".join(self.published_date)
		self.published_date = tools._date_parser(self.published_date)

	def get_articles(self, url=None):
		assert url is not None, "url is not defined."
		page          = self.network_tools.parse(url)
		link_elements = tools._xpath(page, "//a")
		articles      = list()

		for element in link_elements:
			try:
				article         = Article()
				article.element = element
				article.domain  = self.network_tools.get_domain(url)
				article.url     = self.parser.find_article_url(article)
				articles.append(article)
			except exceptions.BadURLFormat as e:
				pass
		articles = [article for article in articles if article.url is not None]		
		articles = list(set(articles))
		return articles

	def to_dict(self):
		return dict(
			url            = self.url,
			domain         = self.domain,
			title          = self.title,
			content        = self.content,
			permalink      = self.url,
			author         = self.author,
			published_date = self.published_date
		)