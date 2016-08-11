from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "hondajazzlover"
	CRAWLER_NAME = "hondajazzlover crawler"
	LINK_TO_CRAWL = [
		"http://www.hondajazzlover.com/forum/index.php?board=2.0",
		"http://www.hondajazzlover.com/forum/index.php?board=21.0",
		"http://www.hondajazzlover.com/forum/index.php?board=1.0",
		"http://www.hondajazzlover.com/forum/index.php?board=4.0",
		"http://www.hondajazzlover.com/forum/index.php?board=16.0",
		"http://www.hondajazzlover.com/forum/index.php?board=20.0",
		"http://www.hondajazzlover.com/forum/index.php?board=3.0",
		"http://www.hondajazzlover.com/forum/index.php?board=18.0",
		"http://www.hondajazzlover.com/forum/index.php?board=11.0",
		"http://www.hondajazzlover.com/forum/index.php?board=19.0",
		"http://www.hondajazzlover.com/forum/index.php?board=5.0",
		"http://www.hondajazzlover.com/forum/index.php?board=15.0",
		"http://www.hondajazzlover.com/forum/index.php?board=6.0",
		"http://www.hondajazzlover.com/forum/index.php?board=9.0",
		"http://www.hondajazzlover.com/forum/index.php?board=8.0",
		"http://www.hondajazzlover.com/forum/index.php?board=10.0"
	]
	COUNTRY = "THA"
	THREAD_XPATH = "//tr//span[re:test(@id,'msg_*')]"
	THREAD_LINK_XPATH = "./a/@href"
	LAST_PAGE_XPATH = "//tr[@class='catbg']//td[@class='middletext']//a[@class='navPages'][last()]//@href"
	PREV_XPATH = "//tr[@class='catbg']//td[@class='middletext']//b[not(contains(text(),' ... '))]//preceding-sibling::a[@class='navPages'][1]//@href"
	POST_XPATH = "//form[@id='quickModForm']//td[@class='windowbg' or @class='windowbg2']"
	FIELDS = [
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": True,
			"xpath":".//div[re:test(@id,'subject_*')]/following-sibling::div[1]/text()"
			# "xpath": "concat(.//td[@width='85%']//div[@class='smalltext']/text()[2],.//td[@width='85%']//div[@class='smalltext']/b[2]/text(),.//td[@width='85%']//div[@class='smalltext']/text()[3])"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":".//td[@rowspan='2' and @width='16%']//b/a/text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//td[@width='85%']//div[@class='post']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath":".//td[@width='85%']//td[2]//div[re:test(@id,'subject_*')]/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"(//span[@class='pathway']/a)[last()]/following-sibling::text()[1]"
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
