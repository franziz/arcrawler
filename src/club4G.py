from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "club4G"
	CRAWLER_NAME = "Club4G Crawler"
	LINK_TO_CRAWL = [
                "http://www.club4g.com/index.php?board=15.0",
                "http://www.club4g.com/index.php/board,1.0",
                "http://www.club4g.com/index.php/board,37.0",
                "http://www.club4g.com/index.php/board,47.0",
                "http://www.club4g.com/index.php/board,41.0",
                "http://www.club4g.com/index.php/board,42.0",
                "http://www.club4g.com/index.php/board,43.0",
                "http://www.club4g.com/index.php/board,52.0",
                "http://www.club4g.com/index.php/board,24.0",
                "http://www.club4g.com/index.php/board,5.0",
                "http://www.club4g.com/index.php?board=21.0",
                "http://www.club4g.com/index.php?board=18.0",
                "http://www.club4g.com/index.php/board,18.0",
                "http://www.club4g.com/index.php/board,3.0",
                "http://www.club4g.com/index.php/board,46.0",
                "http://www.club4g.com/index.php/board,40.0",
                "http://www.club4g.com/index.php/board,50.0",
                "http://www.club4g.com/index.php/board,34.0",
                "http://www.club4g.com/index.php/board,22.0"
                ]
	COUNTRY = "THA"
	# THREAD_XPATH = "//td[@class='subject windowbg2']/div/span"
	THREAD_XPATH = "//span[re:test(@id,'msg_*')]"
	THREAD_LINK_XPATH = "./a/@href"
	LAST_PAGE_XPATH = "(//div[@class='pagelinks floatleft']//a[@class='navPages'])[last()]/@href"
	PREV_XPATH = "//div[@class='pagelinks floatleft']/strong/preceding-sibling::a[1]/@href"
	POST_XPATH = "//div[re:test(@id,'forumposts')]//div[re:test(@class,'windowbg*')]"
	FIELDS = [
		{"published_date": {
			"single": True, 
			"data_type": "date", 
			"concat": False, 
			"xpath": "substring-before(concat(.//div[@class='keyinfo']//div[@class='smalltext']/text()[2],substring-after(.//div[@class='keyinfo']//div[@class='smalltext']/text()[3],'เวลา')),'»')"
			# "xpath": "concat(.//div[@class='keyinfo']//div[@class='smalltext']/text()[2],substring-before(substring-after(.//div[@class='keyinfo']//div[@class='smalltext']/text()[3],'เวลา'),'»'))"
		}},
		{"permalink": {
			"single": True, 
			"data_type": "url", 
			"concat": False, 
			"xpath": ".//div[@class='keyinfo']/h5/a/@href"
		}},                
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":".//div[@class='poster']//h4//a//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":".//div[@class='inner']//text()"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@class='navigate_section']//li[@class='last']//a//text()"
			# "xpath":"normalize-space(substring-before(substring-after(//div[@class='cat_bar']//h3[@class='catbg']//text()[3],':'),'('))"
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
