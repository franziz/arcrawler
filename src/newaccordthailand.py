from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "newaccordthailand"
	CRAWLER_NAME = "Newaccordthailand Crawler"
	LINK_TO_CRAWL = [
		"http://newaccordthailand.com/forum/viewforum.php?f=11",
		"http://newaccordthailand.com/forum/viewforum.php?f=13",
		"http://newaccordthailand.com/forum/viewforum.php?f=14",
		"http://newaccordthailand.com/forum/viewforum.php?f=12",
		"http://newaccordthailand.com/forum/viewforum.php?f=16",
		"http://newaccordthailand.com/forum/viewforum.php?f=17",
		"http://newaccordthailand.com/forum/viewforum.php?f=18",
		"http://newaccordthailand.com/forum/viewforum.php?f=19",
		"http://newaccordthailand.com/forum/viewforum.php?f=20",
		"http://newaccordthailand.com/forum/viewforum.php?f=21",
		"http://newaccordthailand.com/forum/viewforum.php?f=25",
		"http://newaccordthailand.com/forum/viewforum.php?f=37",
		"http://newaccordthailand.com/forum/viewforum.php?f=38",
		"http://newaccordthailand.com/forum/viewforum.php?f=26",
		"http://newaccordthailand.com/forum/viewforum.php?f=27",
		"http://newaccordthailand.com/forum/viewforum.php?f=28",
		"http://newaccordthailand.com/forum/viewforum.php?f=29",
		"http://newaccordthailand.com/forum/viewforum.php?f=30",
		"http://newaccordthailand.com/forum/viewforum.php?f=39",
		"http://newaccordthailand.com/forum/viewforum.php?f=31",
		"http://newaccordthailand.com/forum/viewforum.php?f=32",
		"http://newaccordthailand.com/forum/viewforum.php?f=33",
		"http://newaccordthailand.com/forum/viewforum.php?f=34",
		"http://newaccordthailand.com/forum/viewforum.php?f=35"
	]
	COUNTRY = "THA"
	THREAD_XPATH = "//div[@class='catglow']//td[@class='forumdetails']"
	THREAD_LINK_XPATH = "concat('forum/',./a/@href)"
	LAST_PAGE_XPATH = "concat(substring(concat('forum/',(//div[@class='pagination']/span/a)[last()]/@href),1 div contains((//div[@class='pagination']/span/a)[last()]/@href,'viewtopic')),substring('',1 div not(contains((//div[@class='pagination']/span/a)[last()]/@href,'viewtopic'))))"
	PREV_XPATH = "concat('forum/',//div[@class='pagination']/span/strong/preceding-sibling::a[1]/@href)"
	POST_XPATH = "//div[@class='vtouter']"
	FIELDS = [
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":"substring-after(normalize-space(.//span[@class='vtdate']//text()),' ')"
        }},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":".//span[@class='vtusername']//text()" 
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":".//div[@class='content']//text()" 
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//h3[re:test(@class,'vtsubject')]/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@class='contentpadding']/h2//text()"
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
