from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "theautomotiveindia"
	CRAWLER_NAME = "Theautomotiveindia Crawler"
	LINK_TO_CRAWL = [
                "http://www.theautomotiveindia.com/forums/indian-auto-sector/",
                "http://www.theautomotiveindia.com/forums/global-auto-sector/",
                "http://www.theautomotiveindia.com/forums/automotive-library/",
                "http://www.theautomotiveindia.com/forums/test-drive-reviews/",
                "http://www.theautomotiveindia.com/forums/ownership-reviews/"
	]
	COUNTRY = "IND"
	THREAD_XPATH = "//tr//td[re:test(@id,'td_threadtitle_*')]"
	THREAD_LINK_XPATH = ".//a[re:test(@id,'thread_title_*')]/@href"
	LAST_PAGE_XPATH = "//a[re:test(@title,'Last Page*')]/@href"
	PREV_XPATH = "//a[@rel='prev']/@href"
	POST_XPATH = "//div[re:test(@id,'posts*')]//table[re:test(@id,'post*')]"
	FIELDS = [
		{"published_date": {
			"single": True, 
			"data_type": "date", 
			"concat": False, 
			"xpath": "normalize-space(.//tr[1]//td[1]//text()[2])"
		}},
		{"permalink": {
			"single": True, 
			"data_type": "url", 
			"concat": False, 
			"xpath": ".//td[@class='thead']//a[@title='permalink']/@href"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":".//div[re:test(@id,'postmenu_*')]//a[@class='bigusername']//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[re:test(@id,'post_message_*')]//text()"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//h1[@class='relevant_replacement']//text()"
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
