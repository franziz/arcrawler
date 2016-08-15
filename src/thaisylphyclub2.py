from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "thaisylphyclub2"
	CRAWLER_NAME = "Thaisylphyclub2 Crawler"
	LINK_TO_CRAWL = [
		'http://www.thaisylphyclub.com/index.php?board=1.0',
		 'http://www.thaisylphyclub.com/index.php?board=27.0',
		 'http://www.thaisylphyclub.com/index.php?board=28.0',
		 'http://www.thaisylphyclub.com/index.php?board=6.0',
		 'http://www.thaisylphyclub.com/index.php?board=5.0',
		 'http://www.thaisylphyclub.com/index.php?board=7.0',
		 'http://www.thaisylphyclub.com/index.php?board=8.0',
		 'http://www.thaisylphyclub.com/index.php?board=9.0',
		 'http://www.thaisylphyclub.com/index.php?board=2.0',
		 'http://www.thaisylphyclub.com/index.php?board=23.0',
		 'http://www.thaisylphyclub.com/index.php?board=3.0',
		 'http://www.thaisylphyclub.com/index.php?board=24.0',
		 'http://www.thaisylphyclub.com/index.php?board=33.0',
		 'http://www.thaisylphyclub.com/index.php?board=25.0',
		 'http://www.thaisylphyclub.com/index.php?board=10.0',
		 'http://www.thaisylphyclub.com/index.php?board=30.0',
		 'http://www.thaisylphyclub.com/index.php?board=15.0',
		 'http://www.thaisylphyclub.com/index.php?board=4.0',
		 'http://www.thaisylphyclub.com/index.php?board=11.0',
		 'http://www.thaisylphyclub.com/index.php?board=12.0',
		 'http://www.thaisylphyclub.com/index.php?board=13.0',
		 'http://www.thaisylphyclub.com/index.php?board=14.0',
		 'http://www.thaisylphyclub.com/index.php?board=16.0',
		 'http://www.thaisylphyclub.com/index.php?board=17.0',  ## high frequencey ##
		 'http://www.thaisylphyclub.com/index.php?board=18.0',
		 'http://www.thaisylphyclub.com/index.php?board=19.0',
		 'http://www.thaisylphyclub.com/index.php?board=20.0',
		 'http://www.thaisylphyclub.com/index.php?board=21.0',
		 'http://www.thaisylphyclub.com/index.php?board=22.0'
	]
	COUNTRY = "THA"
	THREAD_XPATH = "//tr//span[re:test(@id,'msg_*')]"
	THREAD_LINK_XPATH = "./a/@href"	
	LAST_PAGE_XPATH = "(//div/a[@class='navPages'])[last()]/@href"
	PREV_XPATH = "//div[@class='pagesection']//div[@class='pagelinks floatleft']/strong/preceding-sibling::a[1]/@href"
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
			"xpath":".//div[@class='poster']//h4//a/text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='post']//div[re:test(@id,'msg_*')]//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath":".//div[@class='postarea']//h5[re:test(@id,'subject_*')]/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"normalize-space(//div[@class='navigate_section']//ul//li[@class='last']//a//text())"
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
