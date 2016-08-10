from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "santabanta"
	CRAWLER_NAME = "Santabanta Crawler"
	LINK_TO_CRAWL = [
		"http://forum.santabanta.com/forumdisplay.htm?2-General-Discussion",
		"http://forum.santabanta.com/forumdisplay.htm?3-Bollywood-Celebrities",
		"http://forum.santabanta.com/forumdisplay.htm?4-International-Celebrities",
		"http://forum.santabanta.com/forumdisplay.htm?9-Ask-Preeto-Agony-Aunt",
		"http://forum.santabanta.com/forumdisplay.htm?14-Mobile-and-Gadgets",
		"http://forum.santabanta.com/forumdisplay.htm?6-Movies",
		"http://forum.santabanta.com/forumdisplay.htm?15-Politics-and-Religious-Chaupal",
		"http://forum.santabanta.com/forumdisplay.htm?7-Television",
		"http://forum.santabanta.com/forumdisplay.htm?13-Regional-Celebrities", ##issue category
		"http://forum.santabanta.com/forumdisplay.htm?5-Music",
		"http://forum.santabanta.com/forumdisplay.htm?8-Sports",
		"http://forum.santabanta.com/forumdisplay.htm?10-Chit-Chat-Corner",
		"http://forum.santabanta.com/forumdisplay.htm?12-SBF-Guest-House",
		"http://forum.santabanta.com/forumdisplay.htm?11-Videos"
        ]
	COUNTRY = "IND"
	THREAD_XPATH = "//li[re:test(@id,'thread_*')]"
	THREAD_LINK_XPATH = ".//a[@class='title']/@href"
	LAST_PAGE_XPATH = "//div[@class='pagination_top']//span[@class='first_last']/a/@href"
	PREV_XPATH = "//div[@class='pagination_top']//span[@class='prev_next']/a/@href"
	POST_XPATH = "//ol[@class='posts']/li[re:test(@id,'post_*')]"
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
			"xpath": ".//div[@class='userinfo']//a/strong//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[re:test(@class,'postrow*')]//text()"
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
			"xpath":"//span[@class='threadtitle']//text()"
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
