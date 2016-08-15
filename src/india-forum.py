from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "india-forum"
	CRAWLER_NAME = "India-Forum Crawler"
	LINK_TO_CRAWL = [
		"http://www.india-forum.com/forums/index.php?/forum/2-indian-history/",
		"http://www.india-forum.com/forums/index.php?/forum/10-indian-culture/",
		"http://www.india-forum.com/forums/index.php?/forum/5-indian-politics/",
		"http://www.india-forum.com/forums/index.php?/forum/8-strategic-security-of-india/",
		"http://www.india-forum.com/forums/index.php?/forum/14-business-economy/",
		"http://www.india-forum.com/forums/index.php?/forum/22-military-discussion/",
		"http://www.india-forum.com/forums/index.php?/forum/20-newshopper-discuss-recent-news/",
		"http://www.india-forum.com/forums/index.php?/forum/3-general-topics/",
		"http://www.india-forum.com/forums/index.php?/forum/13-member-articles/",
		"http://www.india-forum.com/forums/index.php?/forum/7-library-bookmarks/",
		"http://www.india-forum.com/forums/index.php?/forum/6-trash-can/"
        ]
	COUNTRY = "IND"
	THREAD_XPATH = "//table[@class='ipb_table topic_list']//tr[re:test(@id,'trow_*')]"
	THREAD_LINK_XPATH = ".//a[@class='topic_title']/@href"
	LAST_PAGE_XPATH = "(//ul[@class='pagination left']//a[@title!='Next page'])[last()]/@href"
	PREV_XPATH = "//ul[@class='pagination left']//li[@class='prev']/a/@href"
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
			"xpath": ".//span[@class='author vcard']/a/text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[re:test(@class,'entry-content')]//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//span[@class='post_id']/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//h2[@class='maintitle']/span//text()"
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
