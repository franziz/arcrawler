from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "pinoyden"
	CRAWLER_NAME = "Pinoyden Crawler"
	LINK_TO_CRAWL = [
		"http://www.pinoyden.com.ph/index.php?board=2.0",
		"http://www.pinoyden.com.ph/index.php?board=16.0",
		"http://www.pinoyden.com.ph/index.php?board=66.0",
		"http://www.pinoyden.com.ph/index.php?board=3.0",
		"http://www.pinoyden.com.ph/index.php?board=12.0",
		"http://www.pinoyden.com.ph/index.php?board=11.0",
		"http://www.pinoyden.com.ph/index.php?board=107.0",
		"http://www.pinoyden.com.ph/index.php?board=76.0",
		"http://www.pinoyden.com.ph/index.php?board=37.0",
		"http://www.pinoyden.com.ph/index.php?board=72.0",
		"http://www.pinoyden.com.ph/index.php?board=48.0",
		"http://www.pinoyden.com.ph/index.php?board=82.0",
		"http://www.pinoyden.com.ph/index.php?board=83.0",
		"http://www.pinoyden.com.ph/index.php?board=85.0",
		"http://www.pinoyden.com.ph/index.php?board=87.0",
		"http://www.pinoyden.com.ph/index.php?board=86.0",
		"http://www.pinoyden.com.ph/index.php?board=88.0",
		"http://www.pinoyden.com.ph/index.php?board=91.0",
		"http://www.pinoyden.com.ph/index.php?board=89.0",
		"http://www.pinoyden.com.ph/index.php?board=112.0",
		"http://www.pinoyden.com.ph/index.php?board=41.0",
		"http://www.pinoyden.com.ph/index.php?board=131.0",
		"http://www.pinoyden.com.ph/index.php?board=90.0",
		"http://www.pinoyden.com.ph/index.php?board=26.0",
		"http://www.pinoyden.com.ph/index.php?board=108.0",
		"http://www.pinoyden.com.ph/index.php?board=39.0",
		"http://www.pinoyden.com.ph/index.php?board=57.0",
		"http://www.pinoyden.com.ph/index.php?board=58.0",
		"http://www.pinoyden.com.ph/index.php?board=59.0",
		"http://www.pinoyden.com.ph/index.php?board=126.0",
		"http://www.pinoyden.com.ph/index.php?board=60.0",
		"http://www.pinoyden.com.ph/index.php?board=62.0",
		"http://www.pinoyden.com.ph/index.php?board=114.0",
		"http://www.pinoyden.com.ph/index.php?board=128.0",
		"http://www.pinoyden.com.ph/index.php?board=115.0",
		"http://www.pinoyden.com.ph/index.php?board=120.0",
		"http://www.pinoyden.com.ph/index.php?board=123.0",
		"http://www.pinoyden.com.ph/index.php?board=93.0",
		"http://www.pinoyden.com.ph/index.php?board=19.0",
		"http://www.pinoyden.com.ph/index.php?board=5.0",
		"http://www.pinoyden.com.ph/index.php?board=69.0",
		"http://www.pinoyden.com.ph/index.php?board=75.0",
		"http://www.pinoyden.com.ph/index.php?board=129.0",
		"http://www.pinoyden.com.ph/index.php?board=110.0",
		"http://www.pinoyden.com.ph/index.php?board=111.0",
		"http://www.pinoyden.com.ph/index.php?board=54.0",
		"http://www.pinoyden.com.ph/index.php?board=70.0",
		"http://www.pinoyden.com.ph/index.php?board=101.0",
		"http://www.pinoyden.com.ph/index.php?board=103.0",
		"http://www.pinoyden.com.ph/index.php?board=104.0",
		"http://www.pinoyden.com.ph/index.php?board=105.0",
		"http://www.pinoyden.com.ph/index.php?board=102.0"
        ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//span[re:test(@id,'msg_*')]"
	THREAD_LINK_XPATH = "./a/@href"
	LAST_PAGE_XPATH = "(//a[@class='navPages'])[last()]/@href"
	PREV_XPATH = "//div[@id='postbuttons']//b/preceding-sibling::a[1]/@href"
	POST_XPATH = "//div[@class='margintop']"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":".//div[@class='thead_tr']/div[2]/text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//a[re:test(@title,'View the profile*')]/text()"
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
			"xpath":"//td[@class='navbar']//strong/text()"
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
