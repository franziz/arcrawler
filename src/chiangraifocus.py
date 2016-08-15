from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "chaingraifocus"
	CRAWLER_NAME = "Chaingraifocus Crawler"
	LINK_TO_CRAWL = [
		"http://www.chiangraifocus.com/forums/index.php?board=5.0",
        "http://www.chiangraifocus.com/forums/index.php?board=13.0",
        "http://www.chiangraifocus.com/forums/index.php?board=35.0",
        "http://www.chiangraifocus.com/forums/index.php?board=15.0",
        "http://www.chiangraifocus.com/forums/index.php?board=28.0",
        "http://www.chiangraifocus.com/forums/index.php?board=12.0",
        "http://www.chiangraifocus.com/forums/index.php?board=6.0",
        "http://www.chiangraifocus.com/forums/index.php?board=43.0",
        "http://www.chiangraifocus.com/forums/index.php?board=45.0",
        "http://www.chiangraifocus.com/forums/index.php?board=46.0",
        "http://www.chiangraifocus.com/forums/index.php?board=47.0",
        "http://www.chiangraifocus.com/forums/index.php?board=1.0",
        "http://www.chiangraifocus.com/forums/index.php?board=2.0",
        "http://www.chiangraifocus.com/forums/index.php?board=4.0",
        "http://www.chiangraifocus.com/forums/index.php?board=51.0",
        "http://www.chiangraifocus.com/forums/index.php?board=10.0",
        "http://www.chiangraifocus.com/forums/index.php?board=11.0",
        "http://www.chiangraifocus.com/forums/index.php?board=7.0",
        "http://www.chiangraifocus.com/forums/index.php?board=49.0",
        "http://www.chiangraifocus.com/forums/index.php?board=50.0",
        "http://www.chiangraifocus.com/forums/index.php?board=30.0",
        "http://www.chiangraifocus.com/forums/index.php?board=27.0",
        "http://www.chiangraifocus.com/forums/index.php?board=22.0",
        "http://www.chiangraifocus.com/forums/index.php?board=37.0",
        "http://www.chiangraifocus.com/forums/index.php?board=38.0",
        "http://www.chiangraifocus.com/forums/index.php?board=8.0",
        "http://www.chiangraifocus.com/forums/index.php?board=16.0",
        "http://www.chiangraifocus.com/forums/index.php?board=24.0",
        "http://www.chiangraifocus.com/forums/index.php?board=36.0",
        "http://www.chiangraifocus.com/forums/index.php?board=52.0",
        "http://www.chiangraifocus.com/forums/index.php?board=26.0",
        "http://www.chiangraifocus.com/forums/index.php?board=32.0",
        "http://www.chiangraifocus.com/forums/index.php?board=33.0",
        "http://www.chiangraifocus.com/forums/index.php?board=34.0",
        "http://www.chiangraifocus.com/forums/index.php?board=42.0"
	]
	COUNTRY = "THA"
	THREAD_XPATH = "//td[re:test(@class,'window*') and @width='42%']"
	THREAD_LINK_XPATH = "./a/@href"
	LAST_PAGE_XPATH = "(//td/a[@class='navPages'])[last()]/@href"
	PREV_XPATH = "//td/b[not(contains(text(),' ... '))][last()]//preceding-sibling::a[@class='navPages'][1]/@href"
	POST_XPATH = "//form[@id='quickModForm']//td[re:test(@class,'windowbg*')]"
	FIELDS = [
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":"concat(substring-after(concat(.//div[re:test(@id,'subject*')]/following-sibling::span[1]/text()[2],.//div[re:test(@id,'subject*')]/following-sibling::span[1]/text()[3]),'วันที่'),	substring-after(concat(.//div[re:test(@id,'subject*')]/following-sibling::span[1]/text()[2],.//div[re:test(@id,'subject*')]/following-sibling::span[1]/text()[3]),'เวลา'))"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":".//td[@rowspan='2']/b//text()"
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
			"xpath":".//div[re:test(@id,'subject_*')]//a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"normalize-space(//tr[@class='titlebg']//td[@id='top_subject']/font[1]/text())"
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
