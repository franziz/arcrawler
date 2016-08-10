from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "koratnana"
	CRAWLER_NAME = "Koratnana Crawler"
	LINK_TO_CRAWL = [
		"http://www.koratnana.com/index.php?board=2.0",
		"http://www.koratnana.com/index.php?board=3.0",
		"http://www.koratnana.com/index.php?board=64.0",
		"http://www.koratnana.com/index.php?board=68.0",
		"http://www.koratnana.com/index.php?board=69.0",
		"http://www.koratnana.com/index.php?board=5.0",
		"http://www.koratnana.com/index.php?board=80.0",
		"http://www.koratnana.com/index.php?board=4.0",
		"http://www.koratnana.com/index.php?board=66.0",
		"http://www.koratnana.com/index.php?board=20.0",
		"http://www.koratnana.com/index.php?board=83.0",
		"http://www.koratnana.com/index.php?board=84.0",
		"http://www.koratnana.com/index.php?board=76.0",
		"http://www.koratnana.com/index.php?board=77.0",
		"http://www.koratnana.com/index.php?board=78.0",
		"http://www.koratnana.com/index.php?board=79.0",
		"http://www.koratnana.com/index.php?board=85.0",
		"http://www.koratnana.com/index.php?board=8.0",
		"http://www.koratnana.com/index.php?board=9.0",
		"http://www.koratnana.com/index.php?board=13.0",
		"http://www.koratnana.com/index.php?board=10.0",
		"http://www.koratnana.com/index.php?board=12.0",
		"http://www.koratnana.com/index.php?board=11.0",
		"http://www.koratnana.com/index.php?board=14.0",
		"http://www.koratnana.com/index.php?board=18.0",
		"http://www.koratnana.com/index.php?board=15.0",
		"http://www.koratnana.com/index.php?board=16.0",
		"http://www.koratnana.com/index.php?board=17.0",
		"http://www.koratnana.com/index.php?board=19.0",
		"http://www.koratnana.com/index.php?board=58.0",
		"http://www.koratnana.com/index.php?board=55.0",
		"http://www.koratnana.com/index.php?board=60.0",
		"http://www.koratnana.com/index.php?board=74.0",
		"http://www.koratnana.com/index.php?board=86.",
		"http://www.koratnana.com/index.php?board=56.0",
		"http://www.koratnana.com/index.php?board=67.0",
		"http://www.koratnana.com/index.php?board=82.0",
		"http://www.koratnana.com/index.php?board=59.0",
		"http://www.koratnana.com/index.php?board=21.0",
		"http://www.koratnana.com/index.php?board=25.0",
		"http://www.koratnana.com/index.php?board=26.0",
		"http://www.koratnana.com/index.php?board=27.0",
		"http://www.koratnana.com/index.php?board=28.0",
		"http://www.koratnana.com/index.php?board=29.0",
		"http://www.koratnana.com/index.php?board=30.0",
		"http://www.koratnana.com/index.php?board=65.",
		"http://www.koratnana.com/index.php?board=22.0",
		"http://www.koratnana.com/index.php?board=31.0",
		"http://www.koratnana.com/index.php?board=32.0",
		"http://www.koratnana.com/index.php?board=33.0",
		"http://www.koratnana.com/index.php?board=34.0",
		"http://www.koratnana.com/index.php?board=35.0",
		"http://www.koratnana.com/index.php?board=36.0",
		"http://www.koratnana.com/index.php?board=37.0",
		"http://www.koratnana.com/index.php?board=38.0",
		"http://www.koratnana.com/index.php?board=39.0",
		"http://www.koratnana.com/index.php?board=40.0",
		"http://www.koratnana.com/index.php?board=41.0",
		"http://www.koratnana.com/index.php?board=42.0",
		"http://www.koratnana.com/index.php?board=43.0",
		"http://www.koratnana.com/index.php?board=44.0",
		"http://www.koratnana.com/index.php?board=23.0",
		"http://www.koratnana.com/index.php?board=45.0",
		"http://www.koratnana.com/index.php?board=46.0",
		"http://www.koratnana.com/index.php?board=47.0",
		"http://www.koratnana.com/index.php?board=48.0",
		"http://www.koratnana.com/index.php?board=49.0",
		"http://www.koratnana.com/index.php?board=50.0",
		"http://www.koratnana.com/index.php?board=51.0",
		"http://www.koratnana.com/index.php?board=52.0",
		"http://www.koratnana.com/index.php?board=53.0",
		"http://www.koratnana.com/index.php?board=54.0",
		"http://www.koratnana.com/index.php?board=24.0",
		"http://www.koratnana.com/index.php?board=62.0",
		"http://www.koratnana.com/index.php?board=61.0",
		"http://www.koratnana.com/index.php?board=63.0",
		"http://www.koratnana.com/index.php?board=75.0",
		"http://www.koratnana.com/index.php?board=70.0",
		"http://www.koratnana.com/index.php?board=81.0",
		"http://www.koratnana.com/index.php?board=72.0",
		"http://www.koratnana.com/index.php?board=73.0"
    ]
	COUNTRY = "THA"
	THREAD_XPATH = "//span[re:test(@id,'msg_*')]"
	THREAD_LINK_XPATH = "./a/@href"
	LAST_PAGE_XPATH = "(//div[@class='pagesection']//a[@class='navPages'])[last()]/@href"
	PREV_XPATH = "(//div[@class='pagesection']//strong)[last()-1]/preceding-sibling::a[@class='navPages'][1]/@href"
	POST_XPATH = "//form[@id='quickModForm']//div[@class='displaybg']"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":"concat(.//preceding-sibling::div[@class='infodis'][1]//span/text()[1],.//preceding-sibling::div[@class='infodis'][1]//span/b/text(),.//preceding-sibling::div[@class='infodis'][1]//span/text()[2])"
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
			"xpath":"//div[@class='breadCrumb module']//li[@class='last']/h1/a//text()"
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
