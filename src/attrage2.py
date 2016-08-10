from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "attrage2"
	CRAWLER_NAME = "Attrage2 Crawler"
	LINK_TO_CRAWL = [
	    "http://www.attrage-club.com/index.php/board,10.0.html/",
	    "http://www.attrage-club.com/index.php/board,1.0.html",
	    "http://www.attrage-club.com/index.php/board,3.0.html",
	    "http://www.attrage-club.com/index.php/board,7.0.html",
	    "http://www.attrage-club.com/index.php/board,9.0.html",
	    "http://www.attrage-club.com/index.php/board,29.0.html",
	    "http://www.attrage-club.com/index.php/board,8.0.html",
	    "http://www.attrage-club.com/index.php/board,11.0.html",
	    "http://www.attrage-club.com/index.php/board,12.0.html",
	    "http://www.attrage-club.com/index.php/board,13.0.html",
	    "http://www.attrage-club.com/index.php/board,15.0.html",
	    "http://www.attrage-club.com/index.php/board,16.0.html",
	    "http://www.attrage-club.com/index.php/board,17.0.html",
	    "http://www.attrage-club.com/index.php/board,14.0.html",
	    "http://www.attrage-club.com/index.php/board,28.0.html",
	    "http://www.attrage-club.com/index.php/board,26.0.html",
	    "http://www.attrage-club.com/index.php/board,27.0.html",
	    "http://www.attrage-club.com/index.php/board,18.0.html",
	    "http://www.attrage-club.com/index.php/board,19.0.html",
	    "http://www.attrage-club.com/index.php/board,20.0.html",
	    "http://www.attrage-club.com/index.php/board,21.0.html",
	    "http://www.attrage-club.com/index.php/board,22.0.html",
	    "http://www.attrage-club.com/index.php/board,23.0.html",
	    "http://www.attrage-club.com/index.php/board,24.0.html",
	    "http://www.attrage-club.com/index.php/board,25.0.html",
	    "http://www.attrage-club.com/index.php/board,30.0.html",
	    ]
	COUNTRY = "THA"
	# THREAD_XPATH = "//td[@class='windowbg2']"
	THREAD_XPATH = "//span[re:test(@id,'msg*')]"
	# THREAD_XPATH = "(//span[re:test(@id,'msg*')]) or (//td[@class='windowbg2'])"
	THREAD_LINK_XPATH = ".//a/@href"
	LAST_PAGE_XPATH = "(//div[@class='pagelinks floatleft']/a[@class='navPages'])[last()]/@href"
	PREV_XPATH ="//div[@class='pagelinks floatleft']/strong/preceding-sibling::a[1]/@href"
	POST_XPATH = "//form[@id='quickModForm']/div[re:test(@class,'windowbg*')]"
	FIELDS = [
		{"published_date": { 
			"single": True, 
			"data_type": "date", 
			"concat": False, 
			"xpath": "substring-before(concat(.//div[@class='keyinfo']//div[@class='smalltext']/text()[2],substring-after(.//div[@class='keyinfo']//div[@class='smalltext']/text()[3],'เวลา')),'»')"
		}},
		{"permalink": {
			"single": True, 
			"data_type": "url", 
			"concat": False, 
			"xpath": ".//h5[re:test(@id,'subject_*')]/a/@href"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":".//div[@class='poster']/h4/a//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='post']//text()"
			# "xpath":"concat('test',.//div[@class='post']//text())"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"normalize-space(substring-before(substring-after(//div[@class='cat_bar']//h3[@class='catbg']//text()[3],':'),'('))"
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
