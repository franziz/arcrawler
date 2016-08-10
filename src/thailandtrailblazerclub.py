from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "thailandtrailblazerclub"
	CRAWLER_NAME = "Thailandtrailblazerclub Crawler"
	LINK_TO_CRAWL = [
		"http://thailandtrailblazerclub.com/index.php/board,13.0.html",
		"http://thailandtrailblazerclub.com/index.php/board,22.0.html",
		"http://thailandtrailblazerclub.com/index.php/board,2.0.html",
		"http://thailandtrailblazerclub.com/index.php/board,3.0.html",
		"http://thailandtrailblazerclub.com/index.php/board,4.0.html",
		"http://thailandtrailblazerclub.com/index.php/board,7.0.html",
		"http://thailandtrailblazerclub.com/index.php/board,6.0.html",
		"http://thailandtrailblazerclub.com/index.php/board,5.0.html",
		"http://thailandtrailblazerclub.com/index.php/board,11.0.html",
		"http://thailandtrailblazerclub.com/index.php/board,10.0.html",
		"http://thailandtrailblazerclub.com/index.php/board,9.0.html",
		"http://thailandtrailblazerclub.com/index.php/board,49.0.html",
		"http://thailandtrailblazerclub.com/index.php/board,1.0.html",
		"http://thailandtrailblazerclub.com/index.php/board,21.0.html",
		"http://thailandtrailblazerclub.com/index.php/board,14.0.html",
		"http://thailandtrailblazerclub.com/index.php/board,16.0.html",
		"http://thailandtrailblazerclub.com/index.php/board,19.0.html",
		"http://thailandtrailblazerclub.com/index.php/board,18.0.html",
		"http://thailandtrailblazerclub.com/index.php/board,17.0.html",
		"http://thailandtrailblazerclub.com/index.php/board,15.0.html",
		"http://thailandtrailblazerclub.com/index.php/board,20.0.html"
    ]
	COUNTRY = "THA"
	THREAD_XPATH = "//span[re:test(@id,'msg_*')]"
	THREAD_LINK_XPATH = "./a/@href"
	LAST_PAGE_XPATH = "(//div[@class='pagesection']//a[@class='navPages'])[last()]/@href"
	PREV_XPATH = "(//div[@class='pagesection']//strong)[last()-1]/preceding-sibling::a[@class='navPages'][1]/@href"
	POST_XPATH = "//form[@id='quickModForm']//div[@class='windowbg' or @class='windowbg2']"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": True,
			"xpath":".//h5[re:test(@id,'subject_*')]/following-sibling::div[1]/text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath": ".//div[@class='poster']/h4//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[re:test(@id,'msg*')]//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//h5[re:test(@id,'subject_*')]/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@class='navigate_section']//li[@class='last']/a//text()"
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
