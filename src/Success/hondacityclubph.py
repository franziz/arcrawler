from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "hondacityclubph"
	CRAWLER_NAME = "hondacityclubph crawler"
	LINK_TO_CRAWL = [
		"http://www.hondacityclubph.com/forums/forumdisplay.php?fid=4",
		"http://www.hondacityclubph.com/forums/forumdisplay.php?fid=5",
		"http://www.hondacityclubph.com/forums/forumdisplay.php?fid=76",
		"http://www.hondacityclubph.com/forums/forumdisplay.php?fid=77",
		"http://www.hondacityclubph.com/forums/forumdisplay.php?fid=78",
		"http://www.hondacityclubph.com/forums/forumdisplay.php?fid=79",
		"http://www.hondacityclubph.com/forums/forumdisplay.php?fid=80",
		"http://www.hondacityclubph.com/forums/forumdisplay.php?fid=101",
		"http://www.hondacityclubph.com/forums/forumdisplay.php?fid=85",
		"http://www.hondacityclubph.com/forums/forumdisplay.php?fid=82",
		"http://www.hondacityclubph.com/forums/forumdisplay.php?fid=86",
		"http://www.hondacityclubph.com/forums/forumdisplay.php?fid=55",
		"http://www.hondacityclubph.com/forums/forumdisplay.php?fid=56",
		"http://www.hondacityclubph.com/forums/forumdisplay.php?fid=58",
		"http://www.hondacityclubph.com/forums/forumdisplay.php?fid=97",
		"http://www.hondacityclubph.com/forums/forumdisplay.php?fid=99",
		"http://www.hondacityclubph.com/forums/forumdisplay.php?fid=6",
		"http://www.hondacityclubph.com/forums/forumdisplay.php?fid=51",
		"http://www.hondacityclubph.com/forums/forumdisplay.php?fid=54",
		"http://www.hondacityclubph.com/forums/forumdisplay.php?fid=92",
		"http://www.hondacityclubph.com/forums/forumdisplay.php?fid=93",
		"http://www.hondacityclubph.com/forums/forumdisplay.php?fid=91",
		"http://www.hondacityclubph.com/forums/forumdisplay.php?fid=88",
		"http://www.hondacityclubph.com/forums/forumdisplay.php?fid=94",
		"http://www.hondacityclubph.com/forums/forumdisplay.php?fid=95",
		"http://www.hondacityclubph.com/forums/forumdisplay.php?fid=154",
        ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//tr[@class='inline_row']"
	THREAD_LINK_XPATH = "concat('forums/',.//span[re:test(@id,'tid_*')]/a/@href)"
	LAST_PAGE_XPATH = "concat(substring(concat('forums/',(//div[@class='pagination']/a[@class='pagination_page'])[last()]/@href),1 div contains((//div[@class='pagination']/a[@class='pagination_page'])[last()]/@href,'showthread')),substring('',1 div not(contains((//div[@class='pagination']/a[@class='pagination_page'])[last()]/@href,'showthread'))))"
	PREV_XPATH = "concat('forums/',//div[@class='pagination']/a[@class='pagination_previous']/@href)"
	POST_XPATH = "//div[@id='posts']/div[re:test(@id,'post_*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":".//span[@class='post_date']/text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//div[@class='author_information']//a//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[re:test(@id,'pid_*')]//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": "concat('forums/',.//div[@class='post_head']/div[@class='float_right']//a/@href)"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@class='navigation']/span[@class='active']//text()"
		}}       
	]
	CONDITIONS={
		"has_to_have_content":{
			"condition":'"content" in document',
			"exception":'"Content is not defined"'
		},
		"content_cannot_be_empty":{
			"condition":'len(document["content"]) > 0',
			"exception":'"Content cannot be empty"'
		}
	}
#end class
