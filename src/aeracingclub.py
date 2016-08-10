from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "aeracingclub"
	CRAWLER_NAME = "Aeracingclub Crawler"
	LINK_TO_CRAWL = [
		"http://www.aeracingclub.net/forums/index.php?board=6.0",
		"http://www.aeracingclub.net/forums/index.php?board=23.0",
		"http://www.aeracingclub.net/forums/index.php?board=24.0",
		"http://www.aeracingclub.net/forums/index.php?board=25.0",
		"http://www.aeracingclub.net/forums/index.php?board=26.0",
		"http://www.aeracingclub.net/forums/index.php?board=27.0",
		"http://www.aeracingclub.net/forums/index.php?board=28.0",
		"http://www.aeracingclub.net/forums/index.php?board=7.0",
		"http://www.aeracingclub.net/forums/index.php?board=46.0",
		"http://www.aeracingclub.net/forums/index.php?board=45.0",
		"http://www.aeracingclub.net/forums/index.php?board=8.0",
		"http://www.aeracingclub.net/forums/index.php?board=9.0",
		"http://www.aeracingclub.net/forums/index.php?board=10.0",
		"http://www.aeracingclub.net/forums/index.php?board=11.0",
		"http://www.aeracingclub.net/forums/index.php?board=12.0",
		"http://www.aeracingclub.net/forums/index.php?board=13.0",
		"http://www.aeracingclub.net/forums/index.php?board=35.0",
		"http://www.aeracingclub.net/forums/index.php?board=36.0",
		"http://www.aeracingclub.net/forums/index.php?board=38.0",
		"http://www.aeracingclub.net/forums/index.php?board=39.0",
		"http://www.aeracingclub.net/forums/index.php?board=40.0",
		"http://www.aeracingclub.net/forums/index.php?board=41.0",
		"http://www.aeracingclub.net/forums/index.php?board=42.0",
		"http://www.aeracingclub.net/forums/index.php?board=43.0",
		"http://www.aeracingclub.net/forums/index.php?board=31.0",
		"http://www.aeracingclub.net/forums/index.php?board=30.0",
		"http://www.aeracingclub.net/forums/index.php?board=44.0",
		"http://www.aeracingclub.net/forums/index.php?board=37.0",
		"http://www.aeracingclub.net/forums/index.php?board=14.0",
		"http://www.aeracingclub.net/forums/index.php?board=19.0",
		"http://www.aeracingclub.net/forums/index.php?board=15.0",
		"http://www.aeracingclub.net/forums/index.php?board=16.0",
		"http://www.aeracingclub.net/forums/index.php?board=17.0",
		"http://www.aeracingclub.net/forums/index.php?board=32.0",
		"http://www.aeracingclub.net/forums/index.php?board=18.0",
		"http://www.aeracingclub.net/forums/index.php?board=5.0"
	]
	COUNTRY = "THA"
	THREAD_XPATH = "//tr//span[re:test(@id,'msg_*')]"
	THREAD_LINK_XPATH = "./a/@href"
	LAST_PAGE_XPATH = "(//td[@class='middletext']/a[@class='navPages'])[last()]/preceding-sibling::a[1]/@href"
	PREV_XPATH = "//td[@class='middletext']/b/preceding-sibling::a[1]/@href"
	POST_XPATH = "//form[@id='quickModForm']//td[re:test(@class,'windowbg*')]"
	
	FIELDS = [
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath": "concat(.//td[@width='85%']//div[@class='smalltext']/text()[2],(.//td[@width='85%']//div[@class='smalltext']/b)[not(contains(text(),':'))]/text(),.//td[@width='85%']//div[@class='smalltext']/text()[3])"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":".//td[@width='16%']/b//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='post']/text()[1]"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath":".//div[re:test(@id,'subject_*')]/a/@href" 
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
