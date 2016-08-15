from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "hondacityclub"
	CRAWLER_NAME = "Hondacityclub Crawler"
	LINK_TO_CRAWL = [
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=92",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=33",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=99",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=116",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=89",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=47",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=17",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=61",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=46",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=96",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=120",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=121",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=4",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=8",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=127",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=85",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=84",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=83",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=2",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=31",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=125",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=123",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=114",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=126",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=115",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=101",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=41",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=86",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=87",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=90",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=95",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=40",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=36",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=37",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=39",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=38",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=5",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=6",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=124",
		"http://www.hondacityclub.com/board/forumdisplay.php?fid=35"
    ]
	COUNTRY = "THA"
	THREAD_XPATH = "//span[re:test(@id,'thread_*')]"
	THREAD_LINK_XPATH = "concat('board/',./a/@href)"
	LAST_PAGE_XPATH = "concat(substring(concat('board/',(//div[@class='pages']//a)[last()-1]/@href),1 div contains((//div[@class='pages']//a)[last()-1]/@href,'viewthread')),substring('',1 div not(contains((//div[@class='pages']//a)[last()-1]/@href,'viewthread'))))"
	PREV_XPATH = "concat(substring(concat('board/',//div[@class='pages']/strong/preceding-sibling::a/@href),1 div contains(//div[@class='pages']/strong/preceding-sibling::a/@href,'viewthread')),substring('',1 div not(contains(//div[@class='pages']/strong/preceding-sibling::a/@href,'viewthread'))))"
	POST_XPATH = "//div[@id='postlist']/div[re:test(@id,'post*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath": "concat(substring(concat(substring-before(substring-after(substring-after(substring-after(.//em[re:test(@id,'authorposton*')]/text(),' '),'/'),'/'),' '),'/',substring-before(substring-after(substring-after(.//em[re:test(@id,'authorposton*')]/text(),' '),'/'),'/'),'/',substring-before(substring-after(.//em[re:test(@id,'authorposton*')]/text(),' '),'/'),' ',substring-after(substring-after(.//em[re:test(@id,'authorposton*')]/text(),' '),' ')),	1 div contains(substring-after(.//em[re:test(@id,'authorposton*')]/text(),' '),'/')),substring(.//em[re:test(@id,'authorposton*')]/span/text(),	1 div not(contains(substring-after(.//em[re:test(@id,'authorposton*')]/text(),' '),'/'))))"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//td[@class='postauthor']//div[@class='postinfo']/a/text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//td[@class='postcontent']//div[@class='defaultpost']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": "concat('board/',.//div[@class='authorinfo']/a/@href)"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@id='nav']/text()[last()]"
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
