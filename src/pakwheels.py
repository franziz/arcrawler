from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "pakwheels"
	CRAWLER_NAME = "Pakwheels Crawler"
	LINK_TO_CRAWL = [
        "http://www.pakwheels.com/forums/corolla/",
        "http://www.pakwheels.com/forums/vitz-yaris/",
        "http://www.pakwheels.com/forums/prius/",
        "http://www.pakwheels.com/forums/passo/",
        "http://www.pakwheels.com/forums/belta-platz-vios/",
        "http://www.pakwheels.com/forums/other-toyota-models/",
        "http://www.pakwheels.com/forums/civic/",
        "http://www.pakwheels.com/forums/city/",
        "http://www.pakwheels.com/forums/vezel/",
        "http://www.pakwheels.com/forums/accord/",
        "http://www.pakwheels.com/forums/other-honda-models/",
        "http://www.pakwheels.com/forums/mehran/",
        "http://www.pakwheels.com/forums/cultus/",
        "http://www.pakwheels.com/forums/swift/",
        "http://www.pakwheels.com/forums/wagon-r/",
        "http://www.pakwheels.com/forums/liana/",
        "http://www.pakwheels.com/forums/alto/",
        "http://www.pakwheels.com/forums/margalla/",
        "http://www.pakwheels.com/forums/khyber/",
        "http://www.pakwheels.com/forums/baleno/",
        "http://www.pakwheels.com/forums/other-suzuki-models/",
        "http://www.pakwheels.com/forums/cuore-mira/",
        "http://www.pakwheels.com/forums/charade/",
        "http://www.pakwheels.com/forums/other-daihatsu-models/",
        "http://www.pakwheels.com/forums/mitsubishi/",
        "http://www.pakwheels.com/forums/volkswagen/",
        "http://www.pakwheels.com/forums/nissan-datsun/",
        "http://www.pakwheels.com/forums/hyundai-kia/",
        "http://www.pakwheels.com/forums/faw/",
        "http://www.pakwheels.com/forums/member-opinions-suggestions/",
        "http://www.pakwheels.com/forums/fraud-theft-alerts/"
	]
	COUNTRY = "PAK"
	THREAD_XPATH = "//ol//li[re:test(@id,'thread*')]"
	THREAD_LINK_XPATH = ".//a[@class='title']/@href"
	LAST_PAGE_XPATH = "//span[@class='first_last']/a/@href"
	PREV_XPATH = "//span[@class='prev_next']/a[@rel='prev']/@href"
	POST_XPATH = "//ol//li[re:test(@id,'post*')]"
	FIELDS = [
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": True,
			"xpath": ".//span[@class='date']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//div[@class='posthead']//span[@class='nodecontrols']/a[@class='postcounter']/@href"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"normalize-space(.//a[re:test(@class,'username*')]//strong/text())"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='content']//div[re:test(@id,'post_*')]//text()"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":"//div[@class='pagetitle']//span[@class='threadtitle']//text()"
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
