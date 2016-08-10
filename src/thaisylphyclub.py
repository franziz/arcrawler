from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "thaisylphyclub"
	CRAWLER_NAME = "Thaisylphyclub Crawler"
	LINK_TO_CRAWL = [
		 'http://www.thaisylphyclub.com/'
	]	
	COUNTRY = "THA"
	THREAD_XPATH = "//tr//td[@class='windowbg2']"
	THREAD_LINK_XPATH = "./a/@href"
	LAST_PAGE_XPATH = "(//div/a[@class='navPages'])[last()]/@href"
	PREV_XPATH = "//div[@class='pagesection']//div[@class='pagelinks floatleft']/strong/preceding-sibling::a[1]/@href"
	POST_XPATH = "//form[@id='quickModForm']//div[@class='windowbg' or @class='windowbg2']"
	FIELDS = [
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath": "substring-before(concat(.//div[@class='keyinfo']//div[@class='smalltext']/text()[2],substring-after(.//div[@class='keyinfo']//div[@class='smalltext']/text()[3],'เวลา')),'»')"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":".//div[@class='poster']//h4//a/text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='post']//div[re:test(@id,'msg_*')]//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath":".//div[@class='postarea']//h5[re:test(@id,'subject_*')]/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"normalize-space(//div[@class='navigate_section']//ul//li[@class='last']//a//text())"
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
