from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "viosclubphil"
	CRAWLER_NAME = "Viosclubphil Crawler"
	LINK_TO_CRAWL = [
		"http://www.viosclubphil.com/forum/index.php?board=7.0",
		"http://www.viosclubphil.com/forum/index.php?board=21.0",
		"http://www.viosclubphil.com/forum/index.php?board=22.0",
		"http://www.viosclubphil.com/forum/index.php?board=37.0",
		"http://www.viosclubphil.com/forum/index.php?board=10.0",
		"http://www.viosclubphil.com/forum/index.php?board=54.0",
		"http://www.viosclubphil.com/forum/index.php?board=152.0",
		"http://www.viosclubphil.com/forum/index.php?board=184.0",		
		"http://www.viosclubphil.com/forum/index.php?board=158.0",
		"http://www.viosclubphil.com/forum/index.php?board=155.0",
		"http://www.viosclubphil.com/forum/index.php?board=154.0"
    ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//span[re:test(@id,'msg_*')]"
	THREAD_LINK_XPATH = "./a/@href"
	LAST_PAGE_XPATH = "(//div[@class='pagelinks floatleft'])[last()]/a[last()]/@href"
	PREV_XPATH = "(//div[@class='pagelinks floatleft']/strong)[last()]/preceding-sibling::a[1]/@href"
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
			"xpath": ".//div[@class='poster']/h4/a/text()"
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
			"xpath": ".//div[@class='keyinfo']/h5/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"(//div[@class='navigate_section']/ul/li)[last()]/a/span/text()"
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
