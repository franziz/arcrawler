from .article        import Article

class Engine(object):
	def __init__(self):
		self.url           = None
		self.articles      = []
		self.network_tools = None

		# xpath variables
		self.title_xpath          = None
		self.author_name_xpath    = None
		self.content_xpath        = None
		self.published_date_xpath = None

	def parse(self):
		assert self.url is not None, "url is not none."
		article               = Article()
		article.network_tools = self.network_tools
		self.articles         = article.get_articles(self.url)

	def extract(self):
		assert self.articles is not None, "articles is not defined."
		for article in self.articles:
			article.title_xpath          = self.title_xpath
			article.author_name_xpath    = self.author_name_xpath
			article.content_xpath        = self.content_xpath
			article.published_date_xpath = self.published_date_xpath
			article.extract()