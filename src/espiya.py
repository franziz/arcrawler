from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "espiya"
	CRAWLER_NAME = "Espiya Crawler"
	LINK_TO_CRAWL = [
		"http://espiya.net/forum/index.php?board=99.0",
		"http://espiya.net/forum/index.php?board=45.0",
		"http://espiya.net/forum/index.php?board=476.0",
		"http://espiya.net/forum/index.php?board=7.0",
		"http://espiya.net/forum/index.php?board=82.0",
		"http://espiya.net/forum/index.php?board=109.0",
		"http://espiya.net/forum/index.php?board=463.0",
		"http://espiya.net/forum/index.php?board=103.0",
		"http://espiya.net/forum/index.php?board=54.0",
		"http://espiya.net/forum/index.php?board=50.0",
		"http://espiya.net/forum/index.php?board=145.0",
		"http://espiya.net/forum/index.php?board=8.0",
		"http://espiya.net/forum/index.php?board=146.0",
		"http://espiya.net/forum/index.php?board=110.0",
		"http://espiya.net/forum/index.php?board=121.0",
		"http://espiya.net/forum/index.php?board=417.0",
		"http://espiya.net/forum/index.php?board=373.0",
		"http://espiya.net/forum/index.php?board=304.0",
		"http://espiya.net/forum/index.php?board=288.0",
		"http://espiya.net/forum/index.php?board=291.0",
		"http://espiya.net/forum/index.php?board=290.0",
		"http://espiya.net/forum/index.php?board=289.0",
		"http://espiya.net/forum/index.php?board=287.0",
		"http://espiya.net/forum/index.php?board=285.0",
		"http://espiya.net/forum/index.php?board=377.0",
		"http://espiya.net/forum/index.php?board=394.0",
		"http://espiya.net/forum/index.php?board=375.0",
		"http://espiya.net/forum/index.php?board=374.0",
		"http://espiya.net/forum/index.php?board=385.0",
		"http://espiya.net/forum/index.php?board=378.0",
		"http://espiya.net/forum/index.php?board=376.0",
		"http://espiya.net/forum/index.php?board=112.0",
		"http://espiya.net/forum/index.php?board=115.0",
		"http://espiya.net/forum/index.php?board=114.0",
		"http://espiya.net/forum/index.php?board=309.0",
		"http://espiya.net/forum/index.php?board=418.0",
		"http://espiya.net/forum/index.php?board=77.0",
		"http://espiya.net/forum/index.php?board=383.0",
		"http://espiya.net/forum/index.php?board=370.0",
		"http://espiya.net/forum/index.php?board=17.0",
		"http://espiya.net/forum/index.php?board=147.0",
		"http://espiya.net/forum/index.php?board=40.0",
		"http://espiya.net/forum/index.php?board=470.0",
		"http://espiya.net/forum/index.php?board=473.0",
		"http://espiya.net/forum/index.php?board=472.0",
		"http://espiya.net/forum/index.php?board=471.0",
		"http://espiya.net/forum/index.php?board=474.0",
		"http://espiya.net/forum/index.php?board=120.0",
		"http://espiya.net/forum/index.php?board=450.0",
		"http://espiya.net/forum/index.php?board=446.0",
		"http://espiya.net/forum/index.php?board=447.0",
		"http://espiya.net/forum/index.php?board=448.0",
		"http://espiya.net/forum/index.php?board=451.0",
		"http://espiya.net/forum/index.php?board=449.0",
		"http://espiya.net/forum/index.php?board=444.0",
		"http://espiya.net/forum/index.php?board=445.0",
		"http://espiya.net/forum/index.php?board=271.0",
		"http://espiya.net/forum/index.php?board=465.0",
		"http://espiya.net/forum/index.php?board=464.0",
		"http://espiya.net/forum/index.php?board=466.0",
		"http://espiya.net/forum/index.php?board=467.0",
		"http://espiya.net/forum/index.php?board=329.0",
		"http://espiya.net/forum/index.php?board=325.0",
		"http://espiya.net/forum/index.php?board=326.0",
		"http://espiya.net/forum/index.php?board=372.0",
		"http://espiya.net/forum/index.php?board=3.0",
		"http://espiya.net/forum/index.php?board=321.0",
		"http://espiya.net/forum/index.php?board=126.0",
		"http://espiya.net/forum/index.php?board=127.0",
		"http://espiya.net/forum/index.php?board=276.0",
		"http://espiya.net/forum/index.php?board=44.0",
		"http://espiya.net/forum/index.php?board=333.0",
		"http://espiya.net/forum/index.php?board=334.0",
		"http://espiya.net/forum/index.php?board=462.0",
		"http://espiya.net/forum/index.php?board=443.0",
		"http://espiya.net/forum/index.php?board=439.0",
		"http://espiya.net/forum/index.php?board=460.0",
		"http://espiya.net/forum/index.php?board=441.0",
		"http://espiya.net/forum/index.php?board=461.0",
		"http://espiya.net/forum/index.php?board=442.0",
		"http://espiya.net/forum/index.php?board=440.0",
		"http://espiya.net/forum/index.php?board=438.0",
		"http://espiya.net/forum/index.php?board=371.0",
		"http://espiya.net/forum/index.php?board=435.0",
		"http://espiya.net/forum/index.php?board=15.0",
		"http://espiya.net/forum/index.php?board=22.0",
		"http://espiya.net/forum/index.php?board=429.0",
		"http://espiya.net/forum/index.php?board=97.0",
		"http://espiya.net/forum/index.php?board=382.0",
		"http://espiya.net/forum/index.php?board=340.0",
		"http://espiya.net/forum/index.php?board=338.0",		
		"http://espiya.net/forum/index.php?board=337.0",
		"http://espiya.net/forum/index.php?board=336.0",
		"http://espiya.net/forum/index.php?board=475.0",
		"http://espiya.net/forum/index.php?board=24.0",
		"http://espiya.net/forum/index.php?board=335.0",
		"http://espiya.net/forum/index.php?board=398.0",
		"http://espiya.net/forum/index.php?board=389.0",
		"http://espiya.net/forum/index.php?board=390.0",
		"http://espiya.net/forum/index.php?board=388.0",
		"http://espiya.net/forum/index.php?board=387.0",
		"http://espiya.net/forum/index.php?board=386.0",
		"http://espiya.net/forum/index.php?board=391.0",
		"http://espiya.net/forum/index.php?board=261.0",
		"http://espiya.net/forum/index.php?board=136.0",
		"http://espiya.net/forum/index.php?board=135.0",
        ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//span[re:test(@id,'msg_*')]"
	THREAD_LINK_XPATH = "./a/@href"
	LAST_PAGE_XPATH = "(//div[@class='pagelinks floatleft']/a[@class='navPages'])[last()]/@href"
	PREV_XPATH = "//div[@class='pagelinks floatleft']/strong/preceding-sibling::a[@class='navPages'][1]/@href"
	POST_XPATH = "//form[@id='quickModForm']//div[@class='windowbg' or @class='windowbg2']"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": True,
			"xpath":".//h5[re:test(@id,'subject_*')]/following-sibling::div[1]/text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":".//div[@class='poster']/h4/a/text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='post']/div[re:test(@id,'msg_*')]//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//h5[re:test(@id,'subject_*')]/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//ul/li[@class='last']/a//text()"
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
