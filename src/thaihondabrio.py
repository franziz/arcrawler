from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "thaihondabrio"
	CRAWLER_NAME = "Thaihondabrio Crawler"
	LINK_TO_CRAWL = [
		"http://www.thaihondabrio.com/forum/index.php?board=9.0",
		"http://www.thaihondabrio.com/forum/index.php?board=1.0",
		"http://www.thaihondabrio.com/forum/index.php?board=17.0",
		"http://www.thaihondabrio.com/forum/index.php?board=14.0",
		"http://www.thaihondabrio.com/forum/index.php?board=4.0",
		"http://www.thaihondabrio.com/forum/index.php?board=2.0",
		"http://www.thaihondabrio.com/forum/index.php?board=16.0",
		"http://www.thaihondabrio.com/forum/index.php?board=5.0",
		"http://www.thaihondabrio.com/forum/index.php?board=6.0",
		"http://www.thaihondabrio.com/forum/index.php?board=7.0",
		"http://www.thaihondabrio.com/forum/index.php?board=8.0",
		"http://www.thaihondabrio.com/forum/index.php?board=11.0",
		"http://www.thaihondabrio.com/forum/index.php?board=12.0",
		"http://www.thaihondabrio.com/forum/index.php?board=3.0"
    ]
	COUNTRY = "THA"
	THREAD_XPATH = "//td[@class='windowbg' and @width='42%']"
	THREAD_LINK_XPATH = "./a/@href"
	LAST_PAGE_XPATH = "(//td[@class='catbg']//a[@class='navPages'])[last()]/@href"
	PREV_XPATH = "(//td[@class='catbg']//b[text()!=' ... '])/preceding-sibling::a[@class='navPages'][1]/@href"
	POST_XPATH = "//form[@id='quickModForm']//td[@class='windowbg' or @class='windowbg2']"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": True,
			"xpath":".//div[re:test(@id,'subject_*')]/following-sibling::span[1]/text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath": ".//tr[1]/td[1]//a/text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='post']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//div[re:test(@id,'subject_*')]/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"(//span[@class='nav']//b)[last()]/a/text()"
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
