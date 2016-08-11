from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "edulix"
	CRAWLER_NAME = "Edulix Crawler"
	LINK_TO_CRAWL = [
		"http://www.edulix.com/forum/forumdisplay.php?fid=23",
		"http://www.edulix.com/forum/forumdisplay.php?fid=36",
		"http://www.edulix.com/forum/forumdisplay.php?fid=10",
		"http://www.edulix.com/forum/forumdisplay.php?fid=2",
		"http://www.edulix.com/forum/forumdisplay.php?fid=140",
		"http://www.edulix.com/forum/forumdisplay.php?fid=141",
		"http://www.edulix.com/forum/forumdisplay.php?fid=132",
		"http://www.edulix.com/forum/forumdisplay.php?fid=6",
		"http://www.edulix.com/forum/forumdisplay.php?fid=97",
		"http://www.edulix.com/forum/forumdisplay.php?fid=118",
		"http://www.edulix.com/forum/forumdisplay.php?fid=89",
		"http://www.edulix.com/forum/forumdisplay.php?fid=96",
		"http://www.edulix.com/forum/forumdisplay.php?fid=66",
		"http://www.edulix.com/forum/forumdisplay.php?fid=134",
		"http://www.edulix.com/forum/forumdisplay.php?fid=91",
		"http://www.edulix.com/forum/forumdisplay.php?fid=94",
		"http://www.edulix.com/forum/forumdisplay.php?fid=95",
		"http://www.edulix.com/forum/forumdisplay.php?fid=142",
		"http://www.edulix.com/forum/forumdisplay.php?fid=47",
		"http://www.edulix.com/forum/forumdisplay.php?fid=52",
		"http://www.edulix.com/forum/forumdisplay.php?fid=4",
		"http://www.edulix.com/forum/forumdisplay.php?fid=137",
		"http://www.edulix.com/forum/forumdisplay.php?fid=139",
		"http://www.edulix.com/forum/forumdisplay.php?fid=138",
		"http://www.edulix.com/forum/forumdisplay.php?fid=128",
		"http://www.edulix.com/forum/forumdisplay.php?fid=129",
		"http://www.edulix.com/forum/forumdisplay.php?fid=130",
		"http://www.edulix.com/forum/forumdisplay.php?fid=9",
		"http://www.edulix.com/forum/forumdisplay.php?fid=51",
		"http://www.edulix.com/forum/forumdisplay.php?fid=11",
		"http://www.edulix.com/forum/forumdisplay.php?fid=25",
		"http://www.edulix.com/forum/forumdisplay.php?fid=12",
		"http://www.edulix.com/forum/forumdisplay.php?fid=101",
		"http://www.edulix.com/forum/forumdisplay.php?fid=136",
		"http://www.edulix.com/forum/forumdisplay.php?fid=32",
		"http://www.edulix.com/forum/forumdisplay.php?fid=115",
		"http://www.edulix.com/forum/forumdisplay.php?fid=131",
		"http://www.edulix.com/forum/forumdisplay.php?fid=85",
		"http://www.edulix.com/forum/forumdisplay.php?fid=27",
		"http://www.edulix.com/forum/forumdisplay.php?fid=49",
		"http://www.edulix.com/forum/forumdisplay.php?fid=29",
		"http://www.edulix.com/forum/forumdisplay.php?fid=19",
		"http://www.edulix.com/forum/forumdisplay.php?fid=22",
		"http://www.edulix.com/forum/forumdisplay.php?fid=76",
		"http://www.edulix.com/forum/forumdisplay.php?fid=62",
		"http://www.edulix.com/forum/forumdisplay.php?fid=63",		
		"http://www.edulix.com/forum/forumdisplay.php?fid=82",		
		"http://www.edulix.com/forum/forumdisplay.php?fid=57",
		"http://www.edulix.com/forum/forumdisplay.php?fid=105",		
		"http://www.edulix.com/forum/forumdisplay.php?fid=112",
		"http://www.edulix.com/forum/forumdisplay.php?fid=119",		
		"http://www.edulix.com/forum/forumdisplay.php?fid=125",
		"http://www.edulix.com/forum/forumdisplay.php?fid=117",
		"http://www.edulix.com/forum/forumdisplay.php?fid=110",
		"http://www.edulix.com/forum/forumdisplay.php?fid=78",		
		"http://www.edulix.com/forum/forumdisplay.php?fid=34",
		"http://www.edulix.com/forum/forumdisplay.php?fid=8"
        ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//a[re:test(@id,'tid_*')]"
	THREAD_LINK_XPATH = "concat('forum/',./@href)"
	LAST_PAGE_XPATH = "concat(substring(concat('forum/',(//div[@class='pagination']/a[not(contains(text(),'Next'))])[last()]/@href),1 div number(contains((//div[@class='pagination']/a[not(contains(text(),'Next'))])[last()]/@href,'showthread'))),substring('',	1 div number(contains((//div[@class='pagination']/a[not(contains(text(),'Next'))])[last()]/@href,'showthread'))))"
	PREV_XPATH = "concat(substring(concat('forum/',//div[@class='pagination']/a[@class='pagination_previous']/@href),1 div number(contains(//div[@class='pagination']/a[@class='pagination_previous']/@href,'showthread'))),substring('',	1 div number(contains(//div[@class='pagination']/a[@class='pagination_previous']/@href,'showthread'))))"
	POST_XPATH = "//table[re:test(@id,'post_*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":".//td[@style='white-space: nowrap; text-align: center; vertical-align: middle;']/span/text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//td[@width='15%']/strong[1]//span[@class='largetext']//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//tr[1]/td[2]//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//tr[1]/td[2]//tr[1]/td[1]//strong/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@class='navigation']//span[@class='active']/text()"
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
