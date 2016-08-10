from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "hiluxtigerclublub"
	CRAWLER_NAME = "Hiluxtigerclub Crawler"
	LINK_TO_CRAWL = [
		"http://www.hiluxtigerclub.com/V2/index.php?board=16.0",
		"http://www.hiluxtigerclub.com/V2/index.php?board=9.0",
		"http://www.hiluxtigerclub.com/V2/index.php?board=8.0",
		"http://www.hiluxtigerclub.com/V2/index.php?board=14.0",
		"http://www.hiluxtigerclub.com/V2/index.php?board=15.0",
		"http://www.hiluxtigerclub.com/V2/index.php?board=6.0",
		"http://www.hiluxtigerclub.com/V2/index.php?board=17.0",
		"http://www.hiluxtigerclub.com/V2/index.php?board=4.0",
		"http://www.hiluxtigerclub.com/V2/index.php?board=5.0",
		"http://www.hiluxtigerclub.com/V2/index.php?board=10.0",
		"http://www.hiluxtigerclub.com/V2/index.php?board=19.0",
		"http://www.hiluxtigerclub.com/V2/index.php?board=20.0",
		"http://www.hiluxtigerclub.com/V2/index.php?board=12.0",
		"http://www.hiluxtigerclub.com/V2/index.php?board=13.0",
		"http://www.hiluxtigerclub.com/V2/index.php?board=11.0"
        ]
	COUNTRY = "THA"
	THREAD_XPATH = "//div[@id='messageindex']//tr[position()>1]"
	THREAD_LINK_XPATH = ".//span[re:test(@id,'msg*')]/a/@href"
	LAST_PAGE_XPATH = "(//div[@class='pagesection']/div[@class='pagelinks floatleft']/a[@class='navPages'])[last()]/@href"
	PREV_XPATH = "(//div[@class='pagesection']/div[@class='pagelinks floatleft']/strong)[1]/preceding-sibling::a[1]/@href"
	POST_XPATH = "//div[@class='windowbg' or @class='windowbg2']"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath": "substring-before(concat(.//div[@class='keyinfo']//div[@class='smalltext']/text()[2],substring-after(.//div[@class='keyinfo']//div[@class='smalltext']/text()[3],'เวลา')),'»')"
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
			"xpath": ".//div[@class='keyinfo']/h5/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"(//div[@class='navigate_section']/ul/li)[last()]/a/span/text()"
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
