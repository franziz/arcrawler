from lib.forum_engine import Template

class Crawler(Template):
	TEMPLATE          = "crawler.arct"
	TEST_TEMPLATE     = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME    = "detik"
	CRAWLER_NAME      = "Detik Forum Crawler"
	LINK_TO_CRAWL     = "http://forum.detik.com/mobil-f80.html"
	COUNTRY           = "IDN"
	THREAD_XPATH      = "//tbody[@id='threadbits_forum_80']/tr"
	THREAD_LINK_XPATH = ".//a[re:test(@id,'thread_title_*')]/@href"
	LAST_PAGE_XPATH   = "//a[re:test(@title,'Last Page*')]/@href"
	PREV_XPATH        = "//a[@rel='prev']/@href"
	POST_XPATH        = "//table[re:test(@id,'post*')]"
	FIELDS            = [
		{"published_date": {
			"single": True, 
			"data_type": "date", 
			"concat": True, 
			"xpath": "./tbody/tr[1]/td[1]/text()"
		}},
		{"permalink": {
			"single": True, 
			"data_type": "url", 
			"concat": False, 
			"xpath": ".//a[re:test(@id,'postcount*')]/@href"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":".//a[@class='bigusername']/text()"
		}},
		# {"author_id":{
		# 	"single":True,
		# 	"data_type": "string",
		# 	"concat":False,
		# 	"xpath":".//div[@class='user-name']/@data-userid"
		# }},
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
			"xpath":"//td[@class='navbar']/strong/text()"
		}}
	]
	CONDITIONS = {
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