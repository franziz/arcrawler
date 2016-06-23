from lib.forum_engine import Template

class Crawler(Template):
	TEMPLATE          = "crawler.arct"
	TEST_TEMPLATE     = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME    = "kaskus"
	CRAWLER_NAME      = "Kaskus Crawler"
	LINK_TO_CRAWL     = "http://www.kaskus.co.id/forum/570/kendaraan-roda-4"
	COUNTRY           = "IDN"
	THREAD_XPATH      = "//div[@class='post-title']"
	THREAD_LINK_XPATH = "./a/@href"
	LAST_PAGE_XPATH   = "//a[@class='tooltips last-page']/@href"
	PREV_XPATH        = "//a[@class='tooltips previous-page']/@href"
	POST_XPATH        = "//div[@class='row nor-post']"
	FIELDS            = [
		{"published_date": {
			"single": True, 
			"data_type": "date", 
			"concat": False, 
			"xpath": ".//time[@class=\'entry-date\']/@datetime"
		}},
		{"permalink": {
			"single": True, 
			"data_type": "url", 
			"concat": False, 
			"xpath": ".//div[@class=\'permalink\']/a/@href"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":".//span[@itemprop='name']//text()"
		}},
		{"author_id":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":".//div[@class='user-name']/@data-userid"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='entry']//text()"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@class='current']/text()"
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