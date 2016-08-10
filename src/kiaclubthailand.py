from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "kiaclubthailand."
	CRAWLER_NAME = "Kiaclubthailand Crawler"
	LINK_TO_CRAWL = [
		"http://www.kiaclubthailand.com/forums/index.php?board=4.0",
		"http://www.kiaclubthailand.com/forums/index.php?board=5.0",
		"http://www.kiaclubthailand.com/forums/index.php?board=14.0",
		"http://www.kiaclubthailand.com/forums/index.php?board=20.0",
		"http://www.kiaclubthailand.com/forums/index.php?board=18.0",
		"http://www.kiaclubthailand.com/forums/index.php?board=6.0",
		"http://www.kiaclubthailand.com/forums/index.php?board=7.0",
		"http://www.kiaclubthailand.com/forums/index.php?board=8.0",
		"http://www.kiaclubthailand.com/forums/index.php?board=9.0",
		"http://www.kiaclubthailand.com/forums/index.php?board=10.0",
		"http://www.kiaclubthailand.com/forums/index.php?board=11.0",
		"http://www.kiaclubthailand.com/forums/index.php?board=13.0",
		"http://www.kiaclubthailand.com/forums/index.php?board=15.0",
		"http://www.kiaclubthailand.com/forums/index.php?board=16.0",
		"http://www.kiaclubthailand.com/forums/index.php?board=19.0"
    ]
	COUNTRY = "THA"
	THREAD_XPATH = "//span[re:test(@id,'msg_*')]"
	THREAD_LINK_XPATH = "./a/@href"
	LAST_PAGE_XPATH = "(//a[@class='navPages'])[last()]/@href"
	PREV_XPATH = "//td[@class='middletext']/b/preceding-sibling::a[@class='navPages'][1]/@href"
	POST_XPATH = "//form[@id='quickModForm']//td[@class='windowbg' or @class='windowbg2']"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath": "concat(.//td[@width='85%']//div[@class='smalltext']/text()[2],.//td[@width='85%']//div[@class='smalltext']/b[2]/text(),.//td[@width='85%']//div[@class='smalltext']/text()[3])"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//td[@width='16%']/b/a/text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//td[@width='85%']//div[@class='post']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//td[@width='85%']//div[re:test(@id,'subject_*')]/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"(//div[@class='nav']//a[@class='nav'])[last()]/text()"
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
