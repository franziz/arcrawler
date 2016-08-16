from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "huahinforum"
	CRAWLER_NAME = "huahinforum crawler"
	LINK_TO_CRAWL = [
		"http://www.huahinforum.com/viewforum.php?f=26",
		"http://www.huahinforum.com/viewforum.php?f=1",
		"http://www.huahinforum.com/viewforum.php?f=3",
		"http://www.huahinforum.com/viewforum.php?f=2",
		"http://www.huahinforum.com/viewforum.php?f=20",
		"http://www.huahinforum.com/viewforum.php?f=16",
		"http://www.huahinforum.com/viewforum.php?f=4",
		"http://www.huahinforum.com/viewforum.php?f=12",
		"http://www.huahinforum.com/viewforum.php?f=10",
		"http://www.huahinforum.com/viewforum.php?f=8",
		"http://www.huahinforum.com/viewforum.php?f=19",
		"http://www.huahinforum.com/viewforum.php?f=36",
		"http://www.huahinforum.com/viewforum.php?f=7",
		"http://www.huahinforum.com/viewforum.php?f=44",
		"http://www.huahinforum.com/viewforum.php?f=9",
		"http://www.huahinforum.com/viewforum.php?f=15",
		"http://www.huahinforum.com/viewforum.php?f=22",
		"http://www.huahinforum.com/viewforum.php?f=42",
		"http://www.huahinforum.com/viewforum.php?f=24",
		"http://www.huahinforum.com/viewforum.php?f=18",
		"http://www.huahinforum.com/viewforum.php?f=23",
		"http://www.huahinforum.com/viewforum.php?f=29",
		"http://www.huahinforum.com/viewforum.php?f=33",
		"http://www.huahinforum.com/viewforum.php?f=17",
		"http://www.huahinforum.com/viewforum.php?f=28",
		"http://www.huahinforum.com/viewforum.php?f=32",
		"http://www.huahinforum.com/viewforum.php?f=46",
		"http://www.huahinforum.com/viewforum.php?f=6",
		"http://www.huahinforum.com/viewforum.php?f=14"
        ]
	COUNTRY = "THA"
	THREAD_XPATH = "//ul//li[re:test(@class,'row bg*')]"
	THREAD_LINK_XPATH = ".//a[@class='topictitle']/@href"
	LAST_PAGE_XPATH = "(//div[@class='pagination']//a[not(contains(text(),'Next'))])[last()]/@href"
	PREV_XPATH = "//div[@class='pagination']//a[@rel='prev']/@href"
	POST_XPATH = "//div[@id='page-body']/div[re:test(@id,'p*') and re:test(@class,'post has-profile bg*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":".//div[@class='postbody']//p[@class='author']/text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": "concat(.//p[@class='author']//a[re:test(@class,'username')]/text(),.//p[@class='author']//span[re:test(@class,'username')]/text())"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='content']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": "concat(substring-after(//h2[@class='topic-title']/a/@href,'./'),'&#',./@id)"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//h2[@class='topic-title']/a/text()"
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
