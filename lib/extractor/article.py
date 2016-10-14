from ..factory.parser import ParserFactory
from ..network_tools  import NetworkTools
from ..obj.field      import Field
import copy

class ArticleExtractor:
	def __init__(self):
		pass

	def extract(self, **kwargs):
		article 			 = kwargs.get("article", None)
		title_xpath  		 = kwargs.get("title_xpath", None)
		published_date_xpath = kwargs.get("published_date_xpath", None)
		author_name_xpath    = kwargs.get("author_name_xpath", None)
		content_xpath        = kwargs.get("content_xpath", None)
		network_tools  		 = kwargs.get("network_tools", NetworkTools(use_proxy=False))

		assert article 				is not None, "article is not defined."
		assert title_xpath 			is not None, "title_xpath is not defined."
		assert published_date_xpath is not None, "published_date_xpath is not defined."
		assert author_name_xpath    is not None, "author_name_xpath is not defined."
		assert content_xpath   	    is not None, "content_xpath is not defined."

		article_url = copy.copy(article)
		article     = network_tools.parse(article_url)
		parser      = ParserFactory.get_parser(ParserFactory.XPATH)

		permalink           = Field()
		permalink.name      = "permalink"
		permalink.single    = True
		permalink.concat    = True
		permalink.data_type = "string"
		permalink.value     = article_url

		title           = Field()
		title.name      = "title"
		title.single    = True
		title.concat    = True
		title.data_type = "string"
		title.xpath     = title_xpath
		title.value     = parser.parse(article, title_xpath)

		published_date  		 = Field()
		published_date.name      = "published_date"
		published_date.single    = True
		published_date.concat    = True
		published_date.data_type = "date"
		published_date.xpath     = published_date_xpath
		published_date.value     = parser.parse(article, published_date_xpath)

		author_name  		  = Field()
		author_name.name      = "author_name"
		author_name.single    = True
		author_name.concat    = True
		author_name.data_type = "string"
		author_name.xpath     = author_name_xpath
		author_name.value     = parser.parse(article, author_name_xpath)

		content  		  = Field()
		content.name      = "content"
		content.single    = True
		content.concat    = True
		content.data_type = "string"
		content.xpath     = content_xpath
		content.value     = parser.parse(article, content_xpath)


		return {
			     "permalink" : permalink.value,
			         "title" : title.value,
			"published_date" : published_date.value,
			   "author_name" : author_name.value,
			       "content" : content.value
		}