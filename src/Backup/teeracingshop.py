from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "teeracingshop"
	CRAWLER_NAME = "Teeracingshop Crawler"
	LINK_TO_CRAWL = [
		"http://www.teeracingshop.com/index.php?board=55.0",
		"http://www.teeracingshop.com/index.php?board=58.0",
		"http://www.teeracingshop.com/index.php?board=25.0",
		"http://www.teeracingshop.com/index.php?board=30.0",
		"http://www.teeracingshop.com/index.php?board=31.0",
		"http://www.teeracingshop.com/index.php?board=29.0",
		"http://www.teeracingshop.com/index.php?board=28.0",
		"http://www.teeracingshop.com/index.php?board=27.0",
		"http://www.teeracingshop.com/index.php?board=26.0",
		"http://www.teeracingshop.com/index.php?board=68.0",
		"http://www.teeracingshop.com/index.php?board=82.0",
		"http://www.teeracingshop.com/index.php?board=84.0",
		"http://www.teeracingshop.com/index.php?board=147.0",
		"http://www.teeracingshop.com/index.php?board=148.0",
		"http://www.teeracingshop.com/index.php?board=153.0",
		"http://www.teeracingshop.com/index.php?board=155.0",
		"http://www.teeracingshop.com/index.php?board=154.0",
		"http://www.teeracingshop.com/index.php?board=86.0",
		"http://www.teeracingshop.com/index.php?board=151.0",
		"http://www.teeracingshop.com/index.php?board=115.0",
		"http://www.teeracingshop.com/index.php?board=106.0",
		"http://www.teeracingshop.com/index.php?board=105.0",
		"http://www.teeracingshop.com/index.php?board=104.0",
		"http://www.teeracingshop.com/index.php?board=103.0",
		"http://www.teeracingshop.com/index.php?board=102.0",
		"http://www.teeracingshop.com/index.php?board=101.0",
		"http://www.teeracingshop.com/index.php?board=100.0",
		"http://www.teeracingshop.com/index.php?board=99.0",
		"http://www.teeracingshop.com/index.php?board=98.0",
		"http://www.teeracingshop.com/index.php?board=97.0",
		"http://www.teeracingshop.com/index.php?board=96.0",
		"http://www.teeracingshop.com/index.php?board=95.0",
		"http://www.teeracingshop.com/index.php?board=94.0",
		"http://www.teeracingshop.com/index.php?board=93.0",
		"http://www.teeracingshop.com/index.php?board=92.0",
		"http://www.teeracingshop.com/index.php?board=87.0",
		"http://www.teeracingshop.com/index.php?board=112.0",
		"http://www.teeracingshop.com/index.php?board=111.0",
		"http://www.teeracingshop.com/index.php?board=110.0",
		"http://www.teeracingshop.com/index.php?board=109.0",
		"http://www.teeracingshop.com/index.php?board=108.0",
		"http://www.teeracingshop.com/index.php?board=149.0",
		"http://www.teeracingshop.com/index.php?board=107.0",
		"http://www.teeracingshop.com/index.php?board=91.0",
		"http://www.teeracingshop.com/index.php?board=157.0",
		"http://www.teeracingshop.com/index.php?board=90.0",
		"http://www.teeracingshop.com/index.php?board=89.0",
		"http://www.teeracingshop.com/index.php?board=88.0",
		"http://www.teeracingshop.com/index.php?board=158.0",
		"http://www.teeracingshop.com/index.php?board=113.0",
		"http://www.teeracingshop.com/index.php?board=117.0",
		"http://www.teeracingshop.com/index.php?board=116.0",
		"http://www.teeracingshop.com/index.php?board=114.0",
		# "http://www.teeracingshop.com/index.php?board=118.0", # should not use this one
		"http://www.teeracingshop.com/index.php?board=124.0",
		"http://www.teeracingshop.com/index.php?board=123.0",
		"http://www.teeracingshop.com/index.php?board=122.0",
		"http://www.teeracingshop.com/index.php?board=121.0",
		"http://www.teeracingshop.com/index.php?board=120.0",
		"http://www.teeracingshop.com/index.php?board=119.0",
		"http://www.teeracingshop.com/index.php?board=125.0",
		"http://www.teeracingshop.com/index.php?board=128.0",
		"http://www.teeracingshop.com/index.php?board=127.0",
		"http://www.teeracingshop.com/index.php?board=126.0",
		"http://www.teeracingshop.com/index.php?board=129.0",
		"http://www.teeracingshop.com/index.php?board=136.0",
		"http://www.teeracingshop.com/index.php?board=135.0",
		"http://www.teeracingshop.com/index.php?board=134.0",
		"http://www.teeracingshop.com/index.php?board=133.0",
		"http://www.teeracingshop.com/index.php?board=132.0",
		"http://www.teeracingshop.com/index.php?board=131.0",
		"http://www.teeracingshop.com/index.php?board=130.0",
		"http://www.teeracingshop.com/index.php?board=137.0",
		# "http://www.teeracingshop.com/index.php?board=141.0",
		"http://www.teeracingshop.com/index.php?board=140.0",
		"http://www.teeracingshop.com/index.php?board=139.0",
		"http://www.teeracingshop.com/index.php?board=138.0",
		"http://www.teeracingshop.com/index.php?board=142.0",
		"http://www.teeracingshop.com/index.php?board=152.0",
		"http://www.teeracingshop.com/index.php?board=146.0",
		"http://www.teeracingshop.com/index.php?board=145.0",
		"http://www.teeracingshop.com/index.php?board=144.0",
		"http://www.teeracingshop.com/index.php?board=143.0",
		"http://www.teeracingshop.com/index.php?board=156.0",
		"http://www.teeracingshop.com/index.php?board=150.0",
		"http://www.teeracingshop.com/index.php?board=51.0",
		"http://www.teeracingshop.com/index.php?board=18.0",
		"http://www.teeracingshop.com/index.php?board=52.0"
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
			"xpath":".//div[re:test(@id,'msg*')]//text()"
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
