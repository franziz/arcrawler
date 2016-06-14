from news_engine import Template

class Crawler(Template):
	TEMPLATE                = "news_engine_crawler.arct"
	TEST_TEMPLATE           = "news_engine_crawler_test.arct"
	DB_SERVER_ADDRESS       = "mongo:27017"
	DB_SERVER_NAME          = "otosia"
	CRAWLER_NAME            = "Otosia Crawler"
	LINK_TO_CRAWL           = "http://www.otosia.com/"
	COUNTRY                 = "IDN"
	TITLE_FALLBACK          = []
	CONTENT_FALLBACK        = ["//div[@class='OtoDetailNews']//text()"]
	PUBLISHED_DATE_FALLBACK = ["//span[@class='newsdetail-schedule'][1]/text()"]
	AUTHOR_NAME_FALLBACK    = ["concat('otosia.com','')"]
#end class