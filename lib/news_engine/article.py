from ..              import tools
from .parser         import Parser
from .               import exceptions
import difflib

class Article(object):
	def __init__(self):
		self.url            = None
		self.title          = None
		self.domain         = None
		self.author_name    = None
		self.content        = None
		self.published_date = None
		self.network_tools  = None
		self.parser         = Parser()		

		# xpath variables
		self.title_xpath          = None
		self.author_name_xpath    = None
		self.content_xpath        = None
		self.published_date_xpath = None	

	def extract(self):
		assert self.url                  is not None, "url is not defined."
		assert self.title_xpath          is not None, "title_xpath is not defined."
		assert self.author_name_xpath    is not None, "authors_xpath is not defined."
		assert self.content_xpath        is not None, "content_xpath is not defined."
		assert self.published_date_xpath is not None, "published_date_xpath is not defined."
		assert self.network_tools        is not None, "network_tools is not defined."

		page                = self.network_tools.parse(self.url)
		self.title          = self.parser.get_by_xpath(page, self.title_xpath)
		self.content        = self.parser.get_by_xpath(page, self.content_xpath)
		self.author_name    = self.parser.get_by_xpath(page, self.author_name_xpath)
		self.published_date = self.parser.get_by_xpath(page, self.published_date_xpath)
		self.published_date = self.published_date.replace("|"," ")
		self.published_date = tools._date_parser(self.published_date)

	def get_articles(self, url=None):
		assert url                is not None, "url is not defined."
		assert self.network_tools is not None, "network_tools is not defined."

		self.parser.network_tools = self.network_tools
		page                      = self.network_tools.parse(url)
		link_elements             = tools._xpath(page, "//a")
		articles                  = list()

		for element in link_elements:
			try:
				article               = Article()
				article.network_tools = self.network_tools
				article.element       = element
				article.domain        = self.network_tools.get_domain(url)
				article.url           = self.parser.find_article_url(article)
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
			author_name    = self.author_name,
			published_date = self.published_date
		)