from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "thaimarch"
	CRAWLER_NAME = "Thaimarch Crawler"
	LINK_TO_CRAWL = [
		"http://www.thaimarch.com/index.php?board=17.0",
		"http://www.thaimarch.com/index.php?board=30.0",
		"http://www.thaimarch.com/index.php?board=1.0",
		"http://www.thaimarch.com/index.php?board=22.0",
		"http://www.thaimarch.com/index.php?board=23.0",
		"http://www.thaimarch.com/index.php?board=24.0",
		"http://www.thaimarch.com/index.php?board=25.0",
		"http://www.thaimarch.com/index.php?board=26.0",
		"http://www.thaimarch.com/index.php?board=29.0",
		"http://www.thaimarch.com/index.php?board=9.0",
		"http://www.thaimarch.com/index.php?board=3.0",
		"http://www.thaimarch.com/index.php?board=19.0",
		"http://www.thaimarch.com/index.php?board=4.0",
		"http://www.thaimarch.com/index.php?board=15.0",
		"http://www.thaimarch.com/index.php?board=18.0",
		"http://www.thaimarch.com/index.php?board=16.0",
		"http://www.thaimarch.com/index.php?board=5.0",
		"http://www.thaimarch.com/index.php?board=6.0",
		"http://www.thaimarch.com/index.php?board=7.0",
		"http://www.thaimarch.com/index.php?board=32.0",
		"http://www.thaimarch.com/index.php?board=8.0",
		"http://www.thaimarch.com/index.php?board=33.0",
		"http://www.thaimarch.com/index.php?board=34.0",
		"http://www.thaimarch.com/index.php?board=2.0",
		"http://www.thaimarch.com/index.php?board=11.0",
		"http://www.thaimarch.com/index.php?board=10.0",
		"http://www.thaimarch.com/index.php?board=12.0",
		"http://www.thaimarch.com/index.php?board=35.0",
		"http://www.thaimarch.com/index.php?board=36.0",
		"http://www.thaimarch.com/index.php?board=37.0",
		"http://www.thaimarch.com/index.php?board=40.0",
		"http://www.thaimarch.com/index.php?board=38.0",
		"http://www.thaimarch.com/index.php?board=39.0",
		"http://www.thaimarch.com/index.php?board=20.0",
		"http://www.thaimarch.com/index.php?board=13.0"

    ]
	COUNTRY = "THA"
	THREAD_XPATH = "//span[re:test(@id,'msg_*')]"
	THREAD_LINK_XPATH = "./a/@href"
	LAST_PAGE_XPATH = "(//a[@class='navPages'])[last()]/@href"
	PREV_XPATH = "//b[text()!=' ... ']/preceding-sibling::a[@class='navPages'][1]/@href"
	POST_XPATH = "//form[@id='quickModForm']//td[@class='windowbg' or @class='windowbg2']"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath": "concat(.//div[re:test(@id,'subject*')]/following-sibling::div[1]/text()[2],.//div[re:test(@id,'subject*')]/following-sibling::div[1]/text()[3])"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath": ".//tr/td[@width='16%']/b//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='post']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//div[re:test(@id,'subject_*')]/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@class='nav']/b[last()]/a[@class='nav']//text()"
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
