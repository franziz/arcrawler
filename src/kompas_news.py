from lib.news_engine   import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS        = NetworkTools(use_proxy=False)
	TEMPLATE             = "news_engine_crawler.arct"
	TEST_TEMPLATE        = "news_engine_crawler_test.arct"
	DB_SERVER_ADDRESS    = "mongo:27017"
	DB_SERVER_NAME       = "kompas_news"
	CRAWLER_NAME         = "Kompas News Crawler"
	LINK_TO_CRAWL        = "http://www.kompas.com/"
	COUNTRY              = "IDN"
	TITLE_XPATH          = [
								"//div[@class='kcm-read-top clearfix']/h2/text()",
								"//div[@class='kcm-read-content-top']/h2/text()",
								"//div[@class='baca-content']/h1/text()"
						   ]
	CONTENT_XPATH        = [
								"//div[@class='kcm-read-text']//p/text()",
								"//span[@class='kcmread1114']//p/text()",
								"//div[@class='div-read']//p/text()"
						   ]
	PUBLISHED_DATE_XPATH = [
								"//div[@class='kcm-date msmall grey']/text()",
								"substring-after(//div[@class='kcm-date msmall grey mb2']/text(),'Tekno')"
						   ]
	AUTHOR_NAME_XPATH    = [
								"substring-after(//div[@class='kcm-read-copy mt2']/table/tbody/tr[1]/td[2]/text(),': ')",
								"substring-after(//div[@class='kcm-read-copy mb2']//td[2]/text(),': ')",
								"substring-after(//div[@class='penulis-editor']//td[2]/text(),': ')",
								"substring-after(//div[@class='kcm-read-copy mt1']//td[2]/text(),': ')"
						   ]
#end class