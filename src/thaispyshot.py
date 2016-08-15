from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "thaispyshot"
	CRAWLER_NAME = "Thaispyshot Crawler"
	LINK_TO_CRAWL = [
		"http://www.thaispyshot.com/index.php?board=1.0",
		"http://www.thaispyshot.com/index.php?board=2.0",
		"http://www.thaispyshot.com/index.php?board=3.0",
		"http://www.thaispyshot.com/index.php?board=15.0",
		"http://www.thaispyshot.com/index.php?board=4.0",
		"http://www.thaispyshot.com/index.php?board=5.0",
		"http://www.thaispyshot.com/index.php?board=6.0",
		"http://www.thaispyshot.com/index.php?board=20.0",
		"http://www.thaispyshot.com/index.php?board=21.0",
		"http://www.thaispyshot.com/index.php?board=13.0",
		"http://www.thaispyshot.com/index.php?board=14.0",
		"http://www.thaispyshot.com/index.php?board=8.0",
		"http://www.thaispyshot.com/index.php?board=7.0",
		"http://www.thaispyshot.com/index.php?board=9.0",
		"http://www.thaispyshot.com/index.php?board=10.0",
		"http://www.thaispyshot.com/index.php?board=22.0",
		"http://www.thaispyshot.com/index.php?board=11.0",
		# "http://www.thaispyshot.com/index.php?board=12.0", No need to use this
		"http://www.thaispyshot.com/index.php?board=16.0",		
		"http://www.thaispyshot.com/index.php?board=18.0",
		"http://www.thaispyshot.com/index.php?board=17.0"
    ]
	COUNTRY = "THA"
	THREAD_XPATH = "//span[re:test(@id,'msg_*')]"
	THREAD_LINK_XPATH = "./a/@href"
	LAST_PAGE_XPATH = "(//div[@class='pagesection']//a[@class='navPages'])[last()]/@href"
	PREV_XPATH = "(//div[@class='pagesection']//strong)[last()-1]/preceding-sibling::a[@class='navPages'][1]/@href"
	POST_XPATH = "//form[@id='quickModForm']//div[@class='windowbg' or @class='windowbg2']"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": True,
			"xpath":".//h5[re:test(@id,'subject_*')]/following-sibling::div[1]/text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath": ".//div[@class='poster']/h4//text()"
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
			"xpath": ".//h5[re:test(@id,'subject_*')]/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@class='navigate_section']//li[@class='last']/a//text()"
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
