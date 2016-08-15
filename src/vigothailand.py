from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "vigothailand"
	CRAWLER_NAME = "Vigothailand Crawler"
	LINK_TO_CRAWL = [
		"http://www.vigothailand.com/board/index.php?board=44.0",
		"http://www.vigothailand.com/board/index.php?board=15.0",
		"http://www.vigothailand.com/board/index.php?board=8.0",
		"http://www.vigothailand.com/board/index.php?board=35.0",
		"http://www.vigothailand.com/board/index.php?board=7.0",
		"http://www.vigothailand.com/board/index.php?board=4.0",
		"http://www.vigothailand.com/board/index.php?board=22.0",
		"http://www.vigothailand.com/board/index.php?board=48.0",
		"http://www.vigothailand.com/board/index.php?board=21.0",
		"http://www.vigothailand.com/board/index.php?board=18.0",
		"http://www.vigothailand.com/board/index.php?board=16.0",
		"http://www.vigothailand.com/board/index.php?board=2.0",
		"http://www.vigothailand.com/board/index.php?board=56.0",
		"http://www.vigothailand.com/board/index.php?board=3.0",
		"http://www.vigothailand.com/board/index.php?board=55.0",
		"http://www.vigothailand.com/board/index.php?board=24.0",
		"http://www.vigothailand.com/board/index.php?board=37.0",
		"http://www.vigothailand.com/board/index.php?board=5.0",
		"http://www.vigothailand.com/board/index.php?board=45.0",
		"http://www.vigothailand.com/board/index.php?board=46.0",
		"http://www.vigothailand.com/board/index.php?board=36.0",
		"http://www.vigothailand.com/board/index.php?board=6.0",
		"http://www.vigothailand.com/board/index.php?board=26.0",
		"http://www.vigothailand.com/board/index.php?board=10.0",
		"http://www.vigothailand.com/board/index.php?board=17.0"
	]
	COUNTRY = "THA"
	THREAD_XPATH = "//form[@id='quickModForm']//tr[position()>2]/td[3]/span"
	THREAD_XPATH = "//span[re:test(@id,'msg*')]"
	THREAD_LINK_XPATH = "./a/@href"
	LAST_PAGE_XPATH = "(//td[@class='middletext']//a[@class='navPages'])[last()]/@href"
	PREV_XPATH = "//td[@class='middletext']/b[1]/preceding-sibling::a[@class='navPages'][1]/@href"
	POST_XPATH = "//form[@id='quickModForm']//td[@class='windowbg']"
	FIELDS = [ 
        {"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath": "concat(.//div[re:test(@id,'subject*')]/following-sibling::div[1]/text()[2],.//div[re:test(@id,'subject*')]/following-sibling::div[1]/text()[3])"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
            "xpath": ".//table[1]/tr[1]/td[1]/b/a//text()"
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
	        "xpath":"normalize-space(substring-before(substring-after(//tr[@class='catbg3']//td[3]//text(),': '),'('))"
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
