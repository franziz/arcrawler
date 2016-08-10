from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "cruisersforum"
	CRAWLER_NAME = "Cruisersforum Crawler"
	LINK_TO_CRAWL = [
		"http://www.cruisersforum.com/forums/f58/",
		"http://www.cruisersforum.com/forums/f10/",
		"http://www.cruisersforum.com/forums/f9/",
		"http://www.cruisersforum.com/forums/f141/",
		"http://www.cruisersforum.com/forums/f129/",
		"http://www.cruisersforum.com/forums/f106/",
		"http://www.cruisersforum.com/forums/f15/",
		"http://www.cruisersforum.com/forums/f71/",
		"http://www.cruisersforum.com/forums/f17/",
		"http://www.cruisersforum.com/forums/f19/",
		"http://www.cruisersforum.com/forums/f23/",
		"http://www.cruisersforum.com/forums/f24/",
		"http://www.cruisersforum.com/forums/f33/",
		"http://www.cruisersforum.com/forums/f66/",
		"http://www.cruisersforum.com/forums/f60/",
		"http://www.cruisersforum.com/forums/f16/",
		"http://www.cruisersforum.com/forums/f131/",
		"http://www.cruisersforum.com/forums/f108/",
		"http://www.cruisersforum.com/forums/f80/",
		"http://www.cruisersforum.com/forums/f128/",
		"http://www.cruisersforum.com/forums/f127/",
		"http://www.cruisersforum.com/forums/f47/",
		"http://www.cruisersforum.com/forums/f48/",
		"http://www.cruisersforum.com/forums/f109/",
		"http://www.cruisersforum.com/forums/f2/",		
		"http://www.cruisersforum.com/forums/f140/",
		"http://www.cruisersforum.com/forums/f136/",
		"http://www.cruisersforum.com/forums/f139/",
		"http://www.cruisersforum.com/forums/f151/",
		"http://www.cruisersforum.com/forums/f91/",
		"http://www.cruisersforum.com/forums/f92/",
		"http://www.cruisersforum.com/forums/f61/",
		"http://www.cruisersforum.com/forums/f67/",
		"http://www.cruisersforum.com/forums/f74/",
		"http://www.cruisersforum.com/forums/f90/",
		"http://www.cruisersforum.com/forums/f147/",
		"http://www.cruisersforum.com/forums/f121/",
		"http://www.cruisersforum.com/forums/f134/",
		"http://www.cruisersforum.com/forums/f112/",
		"http://www.cruisersforum.com/forums/f122/",
		"http://www.cruisersforum.com/forums/f57/",
		"http://www.cruisersforum.com/forums/f55/",
		"http://www.cruisersforum.com/forums/f124/",
		"http://www.cruisersforum.com/forums/f13/",
		"http://www.cruisersforum.com/forums/f14/",
		"http://www.cruisersforum.com/forums/f54/",
		"http://www.cruisersforum.com/forums/f114/",
		"http://www.cruisersforum.com/forums/f115/",
		"http://www.cruisersforum.com/forums/f116/",
		"http://www.cruisersforum.com/forums/f117/",
		"http://www.cruisersforum.com/forums/f118/",
		"http://www.cruisersforum.com/forums/f152/",
		"http://www.cruisersforum.com/forums/f64/",
		"http://www.cruisersforum.com/forums/f137/",
		"http://www.cruisersforum.com/forums/f30/",
		"http://www.cruisersforum.com/forums/f138/",
		"http://www.cruisersforum.com/forums/f126/"        
	]
	COUNTRY = "THA"
	THREAD_XPATH = "//table[@id='threadslist']//td[re:test(@id,'td_threadtitle_*')]"
	THREAD_LINK_XPATH = "./div/a/@href"
	LAST_PAGE_XPATH = "//div[@class='pagenav']//tr/td[last()-1]/a/@href"
	PREV_XPATH = "//div[@class='pagenav']//a[@rel='prev']/@href"
	POST_XPATH = "//table[re:test(@id,'post*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": True,
			"xpath":"./tr[1]/td[1]/text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//td[@class='userarea']//a[@class='bigusername']//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":"./tr[2]/td[2]//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": "./tr[1]/td[2]/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":"//td[@class='navbar']/strong/text()"
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
