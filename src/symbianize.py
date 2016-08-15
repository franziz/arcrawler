from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "symbianize"
	CRAWLER_NAME = "Symbianize Crawler"
	LINK_TO_CRAWL = [
		"http://www.symbianize.com/forumdisplay.php?f=2",
		"http://www.symbianize.com/forumdisplay.php?f=43",
		"http://www.symbianize.com/forumdisplay.php?f=53",		
		"http://www.symbianize.com/forumdisplay.php?f=126",
		"http://www.symbianize.com/forumdisplay.php?f=132",
		"http://www.symbianize.com/forumdisplay.php?f=61",
		"http://www.symbianize.com/forumdisplay.php?f=146",
		"http://www.symbianize.com/forumdisplay.php?f=150",
		"http://www.symbianize.com/forumdisplay.php?f=149",
		"http://www.symbianize.com/forumdisplay.php?f=184",
		"http://www.symbianize.com/forumdisplay.php?f=64",
		"http://www.symbianize.com/forumdisplay.php?f=8",
		"http://www.symbianize.com/forumdisplay.php?f=65",
		"http://www.symbianize.com/forumdisplay.php?f=63",
		"http://www.symbianize.com/forumdisplay.php?f=66",
		"http://www.symbianize.com/forumdisplay.php?f=209",
		"http://www.symbianize.com/forumdisplay.php?f=193",
		"http://www.symbianize.com/forumdisplay.php?f=211",
		"http://www.symbianize.com/forumdisplay.php?f=210",
		"http://www.symbianize.com/forumdisplay.php?f=208",
		"http://www.symbianize.com/forumdisplay.php?f=147",
		"http://www.symbianize.com/forumdisplay.php?f=62",
		"http://www.symbianize.com/forumdisplay.php?f=67",
		"http://www.symbianize.com/forumdisplay.php?f=192",
		"http://www.symbianize.com/forumdisplay.php?f=154",
		"http://www.symbianize.com/forumdisplay.php?f=156",
		"http://www.symbianize.com/forumdisplay.php?f=158",
		"http://www.symbianize.com/forumdisplay.php?f=157",
		"http://www.symbianize.com/forumdisplay.php?f=159",
		"http://www.symbianize.com/forumdisplay.php?f=160",
		"http://www.symbianize.com/forumdisplay.php?f=34",		
		"http://www.symbianize.com/forumdisplay.php?f=181",
		"http://www.symbianize.com/forumdisplay.php?f=180",
		"http://www.symbianize.com/forumdisplay.php?f=196",
		"http://www.symbianize.com/forumdisplay.php?f=207",
		"http://www.symbianize.com/forumdisplay.php?f=200",
		"http://www.symbianize.com/forumdisplay.php?f=136",
		"http://www.symbianize.com/forumdisplay.php?f=37",
		"http://www.symbianize.com/forumdisplay.php?f=199",
		"http://www.symbianize.com/forumdisplay.php?f=191",
		"http://www.symbianize.com/forumdisplay.php?f=52",
		"http://www.symbianize.com/forumdisplay.php?f=175",
		"http://www.symbianize.com/forumdisplay.php?f=194",		
		"http://www.symbianize.com/forumdisplay.php?f=195",
		"http://www.symbianize.com/forumdisplay.php?f=29",
		"http://www.symbianize.com/forumdisplay.php?f=30",
		"http://www.symbianize.com/forumdisplay.php?f=70",
		"http://www.symbianize.com/forumdisplay.php?f=57",
		"http://www.symbianize.com/forumdisplay.php?f=31",
		"http://www.symbianize.com/forumdisplay.php?f=72",
		"http://www.symbianize.com/forumdisplay.php?f=32",
		"http://www.symbianize.com/forumdisplay.php?f=103",
		"http://www.symbianize.com/forumdisplay.php?f=123",
		"http://www.symbianize.com/forumdisplay.php?f=176",
		"http://www.symbianize.com/forumdisplay.php?f=205",
		"http://www.symbianize.com/forumdisplay.php?f=38",
		"http://www.symbianize.com/forumdisplay.php?f=102",
		"http://www.symbianize.com/forumdisplay.php?f=104",
		"http://www.symbianize.com/forumdisplay.php?f=105",
		"http://www.symbianize.com/forumdisplay.php?f=39",
		"http://www.symbianize.com/forumdisplay.php?f=99",
		"http://www.symbianize.com/forumdisplay.php?f=100",
		"http://www.symbianize.com/forumdisplay.php?f=101",
		"http://www.symbianize.com/forumdisplay.php?f=86",
		"http://www.symbianize.com/forumdisplay.php?f=93",
		"http://www.symbianize.com/forumdisplay.php?f=135",
		"http://www.symbianize.com/forumdisplay.php?f=94",
		"http://www.symbianize.com/forumdisplay.php?f=95",
		"http://www.symbianize.com/forumdisplay.php?f=96",
		"http://www.symbianize.com/forumdisplay.php?f=87",
		"http://www.symbianize.com/forumdisplay.php?f=88",
		"http://www.symbianize.com/forumdisplay.php?f=90",
		"http://www.symbianize.com/forumdisplay.php?f=91",
		"http://www.symbianize.com/forumdisplay.php?f=55",
		"http://www.symbianize.com/forumdisplay.php?f=131",
		"http://www.symbianize.com/forumdisplay.php?f=92",
		"http://www.symbianize.com/forumdisplay.php?f=106",
		"http://www.symbianize.com/forumdisplay.php?f=201",
		"http://www.symbianize.com/forumdisplay.php?f=107",
		"http://www.symbianize.com/forumdisplay.php?f=108",
		"http://www.symbianize.com/forumdisplay.php?f=40",
		"http://www.symbianize.com/forumdisplay.php?f=42",
		"http://www.symbianize.com/forumdisplay.php?f=137",
		"http://www.symbianize.com/forumdisplay.php?f=58",
		"http://www.symbianize.com/forumdisplay.php?f=97",
		"http://www.symbianize.com/forumdisplay.php?f=98",
		"http://www.symbianize.com/forumdisplay.php?f=3"
        ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//li[re:test(@id,'thread_*')]"
	THREAD_LINK_XPATH = ".//a[re:test(@id,'thread_title_*')]/@href"
	LAST_PAGE_XPATH = "(//div[@id='pagination_top']//span[@class='first_last'])[last()]/a/@href"
	PREV_XPATH = "//div[@id='pagination_top']//span[@class='selected']/preceding::a[1]/@href"
	POST_XPATH = "//ol[@id='posts']//li[re:test(@id,'post_*')]/div[@class='posthead']"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": True,
			"xpath":".//span[@class='date']//text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath": "./following-sibling::div[@class='postdetails']//div[@class='username_container']//a[re:test(@class,'username*')]//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":"./following-sibling::div[@class='postdetails']//div[@class='content']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//a[@class='postcounter']/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@class='breadcrumb']//li[@class='navbit lastnavbit']//text()"
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
