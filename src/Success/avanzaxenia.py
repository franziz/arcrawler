from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "avanzaxenia"
	CRAWLER_NAME = "avanzaxenia crawler"
	LINK_TO_CRAWL = [
		"http://avanzaxenia.net/forumdisplay.php?fid=133",
		"http://avanzaxenia.net/forumdisplay.php?fid=6",
		"http://avanzaxenia.net/forumdisplay.php?fid=14",
		"http://avanzaxenia.net/forumdisplay.php?fid=29",
		"http://avanzaxenia.net/forumdisplay.php?fid=120",
		"http://avanzaxenia.net/forumdisplay.php?fid=20",
		"http://avanzaxenia.net/forumdisplay.php?fid=179",
		"http://avanzaxenia.net/forumdisplay.php?fid=137",
		"http://avanzaxenia.net/forumdisplay.php?fid=208",
		"http://avanzaxenia.net/forumdisplay.php?fid=163",
		"http://avanzaxenia.net/forumdisplay.php?fid=182",
		"http://avanzaxenia.net/forumdisplay.php?fid=181",
		"http://avanzaxenia.net/forumdisplay.php?fid=15",
		"http://avanzaxenia.net/forumdisplay.php?fid=16",
		"http://avanzaxenia.net/forumdisplay.php?fid=5",
		"http://avanzaxenia.net/forumdisplay.php?fid=21",
		"http://avanzaxenia.net/forumdisplay.php?fid=18",
		"http://avanzaxenia.net/forumdisplay.php?fid=19",
		"http://avanzaxenia.net/forumdisplay.php?fid=114",
		"http://avanzaxenia.net/forumdisplay.php?fid=115",
		"http://avanzaxenia.net/forumdisplay.php?fid=116",
		"http://avanzaxenia.net/forumdisplay.php?fid=117",
		"http://avanzaxenia.net/forumdisplay.php?fid=118",
		"http://avanzaxenia.net/forumdisplay.php?fid=17",
		"http://avanzaxenia.net/forumdisplay.php?fid=174",
		"http://avanzaxenia.net/forumdisplay.php?fid=175",
		"http://avanzaxenia.net/forumdisplay.php?fid=176",
		"http://avanzaxenia.net/forumdisplay.php?fid=34",
		"http://avanzaxenia.net/forumdisplay.php?fid=108",
		"http://avanzaxenia.net/forumdisplay.php?fid=109",
		"http://avanzaxenia.net/forumdisplay.php?fid=110",
		"http://avanzaxenia.net/forumdisplay.php?fid=111",
		"http://avanzaxenia.net/forumdisplay.php?fid=112",
		"http://avanzaxenia.net/forumdisplay.php?fid=113",
		"http://avanzaxenia.net/forumdisplay.php?fid=56",
		"http://avanzaxenia.net/forumdisplay.php?fid=22",
		"http://avanzaxenia.net/forumdisplay.php?fid=146",
		"http://avanzaxenia.net/forumdisplay.php?fid=205",
		"http://avanzaxenia.net/forumdisplay.php?fid=172",
		"http://avanzaxenia.net/forumdisplay.php?fid=149",
		"http://avanzaxenia.net/forumdisplay.php?fid=148",
		"http://avanzaxenia.net/forumdisplay.php?fid=151",
		"http://avanzaxenia.net/forumdisplay.php?fid=147",
		"http://avanzaxenia.net/forumdisplay.php?fid=152",
		"http://avanzaxenia.net/forumdisplay.php?fid=158",
		"http://avanzaxenia.net/forumdisplay.php?fid=183",
		"http://avanzaxenia.net/forumdisplay.php?fid=156",
		"http://avanzaxenia.net/forumdisplay.php?fid=25",
		"http://avanzaxenia.net/forumdisplay.php?fid=24",
		"http://avanzaxenia.net/forumdisplay.php?fid=129",
		"http://avanzaxenia.net/forumdisplay.php?fid=35",
		"http://avanzaxenia.net/forumdisplay.php?fid=197",
		"http://avanzaxenia.net/forumdisplay.php?fid=155",
		"http://avanzaxenia.net/forumdisplay.php?fid=38",
		"http://avanzaxenia.net/forumdisplay.php?fid=39",
		"http://avanzaxenia.net/forumdisplay.php?fid=42",
		"http://avanzaxenia.net/forumdisplay.php?fid=51",
		"http://avanzaxenia.net/forumdisplay.php?fid=121",
		"http://avanzaxenia.net/forumdisplay.php?fid=195",
		"http://avanzaxenia.net/forumdisplay.php?fid=36",
		"http://avanzaxenia.net/forumdisplay.php?fid=27",
		"http://avanzaxenia.net/forumdisplay.php?fid=28",
		"http://avanzaxenia.net/forumdisplay.php?fid=122",
		"http://avanzaxenia.net/forumdisplay.php?fid=45",
		"http://avanzaxenia.net/forumdisplay.php?fid=104",
		"http://avanzaxenia.net/forumdisplay.php?fid=203",
		"http://avanzaxenia.net/forumdisplay.php?fid=119",
		"http://avanzaxenia.net/forumdisplay.php?fid=106",
		"http://avanzaxenia.net/forumdisplay.php?fid=105",
		"http://avanzaxenia.net/forumdisplay.php?fid=107",
		"http://avanzaxenia.net/forumdisplay.php?fid=124",
		"http://avanzaxenia.net/forumdisplay.php?fid=198"        ]
	COUNTRY = "IDN"
	THREAD_XPATH = "//a[re:test(@id,'tid_*')]"
	THREAD_LINK_XPATH = "./@href"
	LAST_PAGE_XPATH = "(//span[@class='pagenavbit'])[last()]/a/@href"
	PREV_XPATH = "//span[@class='pagenavcurrent']/preceding-sibling::span[1]/a/@href"
	POST_XPATH = "//td[@class='trow1' and @width='85%']"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath": ".//preceding::tr[1]//span/text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//preceding-sibling::td[1]/strong/span/a//text()"
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
			"xpath": ".//span[@class='smalltext']/strong/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":"//table[@style='clear: both;']//div[2]/strong/text()"
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
