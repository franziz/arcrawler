from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "tezimandee"
	CRAWLER_NAME = "Tezimandee Crawler"
	LINK_TO_CRAWL = [
				"http://www.tezimandee.com/forum/forum/41-general-chit-chat/",
        ]
	COUNTRY = "IND"
	THREAD_XPATH = "//a[re:test(@id,'tid-link-*')]"
	THREAD_LINK_XPATH = "./@href"
	LAST_PAGE_XPATH = "(//div[@class='pagination clearfix left ']//a[not(contains(text(),'Next'))])[last()]/@href"
	PREV_XPATH = "//div[@class='pagination clearfix left ']//li[@class='prev']/a/@href"
	POST_XPATH = "//div[re:test(@id,'post_id_*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":".//abbr[@class='published']/text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//span[@class='author vcard']//a[@title='View Profile']//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='post entry-content ']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//a[re:test(@title,'Link to post*')]/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@class='ipsBox_withphoto']//h1//text()"
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
