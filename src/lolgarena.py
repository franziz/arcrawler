from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "lolgarena"
	CRAWLER_NAME = "Lolgarena Crawler"
	LINK_TO_CRAWL = [
		"http://forum.lol.garena.ph/forumdisplay.php?51-UNIVERSAL-RULES-AND-GUIDELINES&",
		"http://forum.lol.garena.ph/forumdisplay.php?2-NEWS&",
		"http://forum.lol.garena.ph/forumdisplay.php?3-Events-and-Promotions&",
		"http://forum.lol.garena.ph/forumdisplay.php?10-GENERAL-DISCUSSIONS&",
		"http://forum.lol.garena.ph/forumdisplay.php?190-Mount-Targon&",
		"http://forum.lol.garena.ph/forumdisplay.php?16-Noxus&",
		"http://forum.lol.garena.ph/forumdisplay.php?29-The-Twisted-Tree-Line&",
		"http://forum.lol.garena.ph/forumdisplay.php?244-League-Client-Update-Alpha&",
		"http://forum.lol.garena.ph/forumdisplay.php?172-HELP-amp-SUPPORT&",
		"http://forum.lol.garena.ph/forumdisplay.php?58-Installation-amp-Updates&",
		"http://forum.lol.garena.ph/forumdisplay.php?57-Network-amp-Connectivity&",
		"http://forum.lol.garena.ph/forumdisplay.php?112-ESPORTS&",
		"http://forum.lol.garena.ph/forumdisplay.php?120-Pro-Gaming-Series-(PGS)&",
		"http://forum.lol.garena.ph/forumdisplay.php?141-LoL-Collegiate-League-(LCL)&",
        ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//li[re:test(@id,'thread_*')]"
	THREAD_LINK_XPATH = ".//a[re:test(@id,'thread_title_*')]/@href"
	LAST_PAGE_XPATH = "//div[@class='pagination_top']//span[@class='first_last']/a/@href"
	PREV_XPATH = "//div[@class='pagination_top']//span[@class='selected']/preceding-sibling::span[1]/a/@href"
	POST_XPATH = "//ol[@id='posts']//li[re:test(@id,'post_*')]"
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
			"concat":False,
			"xpath": ".//div[@class='username_container']//a/strong//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[re:test(@id,'post_message_*')]//text()"
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
