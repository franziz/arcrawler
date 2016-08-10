from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "corollocclubrace"
	CRAWLER_NAME = "Corolloclubrace Crawler"
	LINK_TO_CRAWL = [
		"http://www.corollaclubrace.com/forum/index.php?board=2.0",
		"http://www.corollaclubrace.com/forum/index.php?board=15.0",
		"http://www.corollaclubrace.com/forum/index.php?board=4.0",
		"http://www.corollaclubrace.com/forum/index.php?board=9.0",
		"http://www.corollaclubrace.com/forum/index.php?board=12.0",
		"http://www.corollaclubrace.com/forum/index.php?board=8.0",
		"http://www.corollaclubrace.com/forum/index.php?board=5.0",
		"http://www.corollaclubrace.com/forum/index.php?board=6.0"
    ]
	COUNTRY = "THA"
	THREAD_XPATH = "//span[re:test(@id,'msg_*')]"
	THREAD_LINK_XPATH = "./a/@href"
	LAST_PAGE_XPATH = "(//td[@class='middletext']//a[@class='navPages'])[last()]/@href"
	PREV_XPATH = "//td[@class='middletext']/b/preceding-sibling::a[1]/@href"
	POST_XPATH = "//form[@id='quickModForm']//td[re:test(@class,'windowbg')]"
	FIELDS = [
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath": "concat(substring-before(concat(.//div[re:test(@id,'subject_*')]/following-sibling::div[1]/text()[2],.//div[re:test(@id,'subject_*')]/following-sibling::div[1]/b[2]/text(),.//div[re:test(@id,'subject_*')]/following-sibling::div[1]/text()[3]),'PM'),substring-before(concat(.//div[re:test(@id,'subject_*')]/following-sibling::div[1]/text()[2],.//div[re:test(@id,'subject_*')]/following-sibling::div[1]/b[2]/text(),.//div[re:test(@id,'subject_*')]/following-sibling::div[1]/text()[3]),'AM'))"
		}},			
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//div[re:test(@id,'subject_*')]/a/@href"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"normalize-space(.//td[@rowspan=2]/b/a/text())"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='post']//text()"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"normalize-space(substring-before(substring-after(//tr[@class='catbg3']//td[@id='top_subject']//text(),':'),'('))"
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
