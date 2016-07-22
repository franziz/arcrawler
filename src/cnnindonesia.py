from lib.news_engine   import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS        = NetworkTools(use_proxy=False)
	TEMPLATE             = "news_engine_crawler.arct"
	TEST_TEMPLATE        = "news_engine_crawler_test.arct"
	DB_SERVER_ADDRESS    = "mongo:27017"
	DB_SERVER_NAME       = "cnnindonesia"
	CRAWLER_NAME         = "CNN Indonesia Crawler"
	LINK_TO_CRAWL        = [
								"http://www.cnnindonesia.com/",
								"http://www.cnnindonesia.com/politik",
								"http://www.cnnindonesia.com/nasional",
								"http://www.cnnindonesia.com/ekonomi",
								"http://www.cnnindonesia.com/internasional",
								"http://www.cnnindonesia.com/olahraga",
								"http://www.cnnindonesia.com/teknologi",
								"http://www.cnnindonesia.com/hiburan",
								"http://www.cnnindonesia.com/gaya-hidup",
								"http://www.cnnindonesia.com/focus"
						   ]
	COUNTRY              = "IDN"
	TITLE_XPATH          = "//h1/text()"
	CONTENT_XPATH        = "//div[@itemprop='description']//text()"
	PUBLISHED_DATE_XPATH = "substring-before(//div[@itemprop='datePublished']/text(), 'WIB')"
	AUTHOR_NAME_XPATH    = "//strong[@itemprop='author']/text()"
#end class