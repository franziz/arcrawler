from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "indiaconsumercomplaints"
	CRAWLER_NAME = "indiaconsumercomplaints crawler"
	LINK_TO_CRAWL = [
		"http://forum.indiaconsumercomplaints.com/Forum-Consumer-Complaints-General-Forum",
		"http://forum.indiaconsumercomplaints.com/Forum-Narrate-Your-Horror-Story",
		"http://forum.indiaconsumercomplaints.com/Forum-Legal-Advisory-Help",
		"http://forum.indiaconsumercomplaints.com/Forum-Suggestions-Feedback",
		"http://forum.indiaconsumercomplaints.com/Forum-Everything-Else",
		"http://forum.indiaconsumercomplaints.com/Forum-Maruti-Alto",		
		"http://forum.indiaconsumercomplaints.com/Forum-All-Cars--405",
		"http://forum.indiaconsumercomplaints.com/Forum-Hero-Honda",
		"http://forum.indiaconsumercomplaints.com/Forum-Honda-Bikes",
		"http://forum.indiaconsumercomplaints.com/Forum-i10-i20",
		"http://forum.indiaconsumercomplaints.com/Forum-All-Cars",
		"http://forum.indiaconsumercomplaints.com/Forum-Volkswagen"
        ]
	COUNTRY = "IND"
	THREAD_XPATH = "//a[re:test(@id,'tid_*')]"
	THREAD_LINK_XPATH = "./@href"
	LAST_PAGE_XPATH = "(//div[@class='pagination']//a[not(contains(text(),'Next'))])[last()]/@href"
	PREV_XPATH = "//div[@class='pagination']//a[@class='pagination_previous']/@href"
	POST_XPATH = "//table[re:test(@id,'post_*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":".//td[@class='tcat']/div[1]/text()[1]"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//td[@class='post_author']/strong/span/a//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//td[@class='trow2 post_content ']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//strong[contains(text(),'Post:')]/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@class='navigation']//span[@class='active']/text()"
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
