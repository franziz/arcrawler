from lib.news_engine   import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS        = NetworkTools(use_proxy=False)
	TEMPLATE             = "news_engine_crawler.arct"
	TEST_TEMPLATE        = "news_engine_crawler_test.arct"
	DB_SERVER_ADDRESS    = "mongo:27017"
	DB_SERVER_NAME       = "otosia"
	CRAWLER_NAME         = "Otosia Crawler"
	LINK_TO_CRAWL        = "http://www.otosia.com/"
	COUNTRY              = "IDN"
	TITLE_XPATH          = "//h1[@class='OtoDetailT']/text()"
	CONTENT_XPATH        = "//div[@class='OtoDetailNews']//text()"
	PUBLISHED_DATE_XPATH = "//span[@class='newsdetail-schedule'][1]/text()"
	AUTHOR_NAME_XPATH    = "concat('otosia.com','')"
#end class