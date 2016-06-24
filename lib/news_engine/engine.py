from .newspaper import news_pool, Config, Article
from .          import newspaper
from ..         import tools
import arrow

class Engine(object):
	def __init__(self):
		self._config                    = Config()
		self._config.memoize_articles   = False
		self._config.fetch_images       = False
		self._config.browser_user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
		self._config.request_timeout    = 10
		self._config.http_success_only  = False

		# private variable
		self._title          = None
		self._content        = None
		self._published_date = None
		self._author_name    = None
		self._url            = None

		# Public variables
		self.domain                  = None
		self.title_fallback          = []
		self.content_fallback        = []
		self.published_date_fallback = []
		self.author_name_fallback    = []
		self.network_tools           = None
	#end def

	@property
	def url(self):
		""" You cannot set url variable from outside. 
		"""
		return self._url

	@property
	def content(self):
		""" You cannot set content variable from outside. 
		"""
		return self._content

	@property
	def title(self):
		""" You cannot set title variable from outside. 
		"""
		return self._title

	@property
	def author_name(self):
		""" You cannot set author_name variable from outside. 
		"""
		return self._author_name
	
	@property
	def published_date(self):
		""" You cannot set published_date from outside.
		"""
		return self._published_date
	
	@property
	def config(self):
		""" You cannot set config variable form outside.
		"""
		return self._config
	
	@property
	def urls(self):
		""" You cannot set the urls variable from outside.
		"""
		assert self.domain is not None                                , "domain is not defined."
		assert "http://"   in self.domain or "https://" in self.domain, "domain is in wrong format"
		
		domain     = newspaper.build(self.domain, config=self.config)
		self._urls = list()
		for article in domain.articles:
			self._urls.append(article.url)
		return self._urls
	
	def parse(self,url=None):
		""" Parse given the URL.
		"""
		assert url                                is not None, "url is not defined."
		assert type(self.title_fallback)          is list    , "title_fallback have to be in list"
		assert type(self.content_fallback)        is list    , "content_fallback have be in list"
		assert type(self.published_date_fallback) is list    , "published_date_fallback have be in list"
		assert type(self.author_name_fallback)    is list    , "author_name_fallback have be in list"

		article = Article(url, config=self.config)
		article.download()
		article.parse()

		self._url            = article.url
		self._title          = article.title if article.title else None
		self._content        = article.text if article.text else None
		self._published_date = article.publish_date if article.publish_date else None
		self._author_name    = article.authors[0] if len(article.authors) > 0 else None

		self._title          = self._fallback_assigner(variable=self.title, fallback=self.title_fallback)
		self._content        = self._fallback_assigner(variable=self.content, fallback=self.content_fallback)
		self._published_date = self._fallback_assigner(variable=self.published_date, fallback=self.published_date_fallback)
		self._author_name    = self._fallback_assigner(variable=self.author_name, fallback=self.author_name_fallback)

		self._title          = tools._clean_string(string=self.title) if self._title is not None else self.title
		self._content        = tools._clean_string(string=self.content) if self._content is not None else self.content
		self._author_name    = tools._clean_string(string=self.author_name) if self._author_name is not None else self.author_name

		self._published_date = self.published_date if self.published_date is not None else arrow.utcnow().datetime

		if type(self.published_date) is str:
			self._published_date = tools._clean_string(string=self.published_date)
			self._published_date = tools._date_parser(str_date=self.published_date)			
	#end def

	def _fallback_assigner(self, variable=None, fallback=None):
		assert self.url           is not None, "url is not defined."
		assert self.network_tools is not None, "network_tools is not defined."
		
		result = variable
		if variable is None:
			for xpath in fallback:
				page   = self.network_tools.parse(url=self.url)
				result = tools._xpath(parent=page, syntax=xpath)
				result = "".join(result) if "concat" in xpath else " ".join(result) if len(result) > 0 else None		

				if result is not None: break
			#end for
		#end if
		return result
	#end def

#end class