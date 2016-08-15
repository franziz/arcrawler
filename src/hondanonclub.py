from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "hondanonclub"
	CRAWLER_NAME = "Hondanonclub Crawler"
	LINK_TO_CRAWL = [
		"http://www.hondanonclub.com/webboard/index.php?board=30.0",
		"http://www.hondanonclub.com/webboard/index.php?board=1.0",
		"http://www.hondanonclub.com/webboard/index.php?board=20.0",
		"http://www.hondanonclub.com/webboard/index.php?board=37.0",
		"http://www.hondanonclub.com/webboard/index.php?board=39.0",
		"http://www.hondanonclub.com/webboard/index.php?board=40.0",
		"http://www.hondanonclub.com/webboard/index.php?board=41.0",
		"http://www.hondanonclub.com/webboard/index.php?board=21.0",
		"http://www.hondanonclub.com/webboard/index.php?board=89.0",
		"http://www.hondanonclub.com/webboard/index.php?board=112.0",
		"http://www.hondanonclub.com/webboard/index.php?board=22.0",
		"http://www.hondanonclub.com/webboard/index.php?board=110.0",
		"http://www.hondanonclub.com/webboard/index.php?board=111.0",
		"http://www.hondanonclub.com/webboard/index.php?board=60.0",
		"http://www.hondanonclub.com/webboard/index.php?board=28.0",
		"http://www.hondanonclub.com/webboard/index.php?board=31.0",
		"http://www.hondanonclub.com/webboard/index.php?board=29.0",
		"http://www.hondanonclub.com/webboard/index.php?board=32.0",
		"http://www.hondanonclub.com/webboard/index.php?board=33.0",
		"http://www.hondanonclub.com/webboard/index.php?board=34.0",
		"http://www.hondanonclub.com/webboard/index.php?board=35.0",
		"http://www.hondanonclub.com/webboard/index.php?board=36.0",
		"http://www.hondanonclub.com/webboard/index.php?board=38.0",
		"http://www.hondanonclub.com/webboard/index.php?board=42.0",
		"http://www.hondanonclub.com/webboard/index.php?board=43.0",
		"http://www.hondanonclub.com/webboard/index.php?board=44.0",
		"http://www.hondanonclub.com/webboard/index.php?board=45.0",
		"http://www.hondanonclub.com/webboard/index.php?board=46.0",
		"http://www.hondanonclub.com/webboard/index.php?board=47.0",
		"http://www.hondanonclub.com/webboard/index.php?board=48.0",
		"http://www.hondanonclub.com/webboard/index.php?board=49.0",
		"http://www.hondanonclub.com/webboard/index.php?board=50.0",
		"http://www.hondanonclub.com/webboard/index.php?board=51.0",
		"http://www.hondanonclub.com/webboard/index.php?board=53.0",
		"http://www.hondanonclub.com/webboard/index.php?board=54.0",
		"http://www.hondanonclub.com/webboard/index.php?board=55.0",
		"http://www.hondanonclub.com/webboard/index.php?board=56.0",
		"http://www.hondanonclub.com/webboard/index.php?board=57.0",
		"http://www.hondanonclub.com/webboard/index.php?board=58.0",
		"http://www.hondanonclub.com/webboard/index.php?board=61.0",
		"http://www.hondanonclub.com/webboard/index.php?board=66.0",
		"http://www.hondanonclub.com/webboard/index.php?board=70.0",
		"http://www.hondanonclub.com/webboard/index.php?board=71.0",
		"http://www.hondanonclub.com/webboard/index.php?board=72.0",
		"http://www.hondanonclub.com/webboard/index.php?board=73.0",
		"http://www.hondanonclub.com/webboard/index.php?board=74.0",
		"http://www.hondanonclub.com/webboard/index.php?board=75.0",
		"http://www.hondanonclub.com/webboard/index.php?board=77.0",
		"http://www.hondanonclub.com/webboard/index.php?board=78.0",
		"http://www.hondanonclub.com/webboard/index.php?board=79.0",
		"http://www.hondanonclub.com/webboard/index.php?board=80.0",
		"http://www.hondanonclub.com/webboard/index.php?board=82.0",
		"http://www.hondanonclub.com/webboard/index.php?board=83.0",
		"http://www.hondanonclub.com/webboard/index.php?board=84.0",
		"http://www.hondanonclub.com/webboard/index.php?board=85.0",
		"http://www.hondanonclub.com/webboard/index.php?board=86.0",
		"http://www.hondanonclub.com/webboard/index.php?board=87.0",
		"http://www.hondanonclub.com/webboard/index.php?board=88.0",
		"http://www.hondanonclub.com/webboard/index.php?board=90.0",
		"http://www.hondanonclub.com/webboard/index.php?board=91.0",
		"http://www.hondanonclub.com/webboard/index.php?board=92.0",
		"http://www.hondanonclub.com/webboard/index.php?board=93.0",
		"http://www.hondanonclub.com/webboard/index.php?board=94.0",
		"http://www.hondanonclub.com/webboard/index.php?board=95.0",
		"http://www.hondanonclub.com/webboard/index.php?board=96.0",
		"http://www.hondanonclub.com/webboard/index.php?board=97.0",
		"http://www.hondanonclub.com/webboard/index.php?board=98.0",
		"http://www.hondanonclub.com/webboard/index.php?board=99.0",
		"http://www.hondanonclub.com/webboard/index.php?board=100.0",
		"http://www.hondanonclub.com/webboard/index.php?board=101.0",
		"http://www.hondanonclub.com/webboard/index.php?board=102.0",
		"http://www.hondanonclub.com/webboard/index.php?board=103.0",
		"http://www.hondanonclub.com/webboard/index.php?board=104.0",
		"http://www.hondanonclub.com/webboard/index.php?board=105.0",
		"http://www.hondanonclub.com/webboard/index.php?board=106.0",
		"http://www.hondanonclub.com/webboard/index.php?board=107.0",
		"http://www.hondanonclub.com/webboard/index.php?board=108.0",
		"http://www.hondanonclub.com/webboard/index.php?board=113.0",
		"http://www.hondanonclub.com/webboard/index.php?board=114.0",
		"http://www.hondanonclub.com/webboard/index.php?board=115.0",
		"http://www.hondanonclub.com/webboard/index.php?board=116.0",
		"http://www.hondanonclub.com/webboard/index.php?board=117.0",
		"http://www.hondanonclub.com/webboard/index.php?board=118.0",
		"http://www.hondanonclub.com/webboard/index.php?board=119.0",
		"http://www.hondanonclub.com/webboard/index.php?board=120.0",
		"http://www.hondanonclub.com/webboard/index.php?board=81.0",
		"http://www.hondanonclub.com/webboard/index.php?board=52.0",
		"http://www.hondanonclub.com/webboard/index.php?board=23.0",
		"http://www.hondanonclub.com/webboard/index.php?board=27.0",
		"http://www.hondanonclub.com/webboard/index.php?board=59.0",
		"http://www.hondanonclub.com/webboard/index.php?board=24.0",
		"http://www.hondanonclub.com/webboard/index.php?board=18.0",
		"http://www.hondanonclub.com/webboard/index.php?board=19.0",
		"http://www.hondanonclub.com/webboard/index.php?board=25.0"
    ]
	COUNTRY = "THA"
	THREAD_XPATH = "//span[re:test(@id,'msg_*')]"
	THREAD_LINK_XPATH = "./a/@href"
	LAST_PAGE_XPATH = "(//a[@class='navPages'])[last()]/@href"
	PREV_XPATH = "(//td[@class='middletext']//b[text()!=' ... '])[last()-1]/preceding-sibling::a[1]/@href"
	POST_XPATH = "//form[@id='quickModForm']//td[@class='windowbg' or @class='windowbg2']"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath": "substring-before(concat(..//tr/td[@width='85%']//div[@class='smalltext']/text()[2],substring-after(.//tr/td[@width='85%']//div[@class='smalltext']/text()[3],'เวลา')),'»')"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//tr/td[@width='16%']/b/a/text()"
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
			"xpath": ".//tr/td[@width='85%']//div[re:test(@id,'subject_*')]/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"(//table[@style='margin-bottom: 1ex;']//td[@valign='top']//div[@class='nav']//a)[last()]/text()"
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
