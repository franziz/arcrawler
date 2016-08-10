from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "ligagame"
	CRAWLER_NAME = "Ligagame Crawler"
	LINK_TO_CRAWL = [
		"http://www.ligagame.com/forum/index.php?board=425.0",
		"http://www.ligagame.com/forum/index.php?board=454.0",
		"http://www.ligagame.com/forum/index.php?board=18.0",
		"http://www.ligagame.com/forum/index.php?board=166.0",
		"http://www.ligagame.com/forum/index.php?board=169.0",
		"http://www.ligagame.com/forum/index.php?board=29.0",
		"http://www.ligagame.com/forum/index.php?board=453.0",
		"http://www.ligagame.com/forum/index.php?board=164.0",
		"http://www.ligagame.com/forum/index.php?board=248.0",
		"http://www.ligagame.com/forum/index.php?board=300.0",
		"http://www.ligagame.com/forum/index.php?board=305.0",
		"http://www.ligagame.com/forum/index.php?board=432.0",
		"http://www.ligagame.com/forum/index.php?board=433.0",
		"http://www.ligagame.com/forum/index.php?board=392.0",
		"http://www.ligagame.com/forum/index.php?board=295.0",
		"http://www.ligagame.com/forum/index.php?board=340.0",
		"http://www.ligagame.com/forum/index.php?board=264.0",
		"http://www.ligagame.com/forum/index.php?board=81.0",
		"http://www.ligagame.com/forum/index.php?board=140.0",
		"http://www.ligagame.com/forum/index.php?board=130.0",
		"http://www.ligagame.com/forum/index.php?board=437.0",
		"http://www.ligagame.com/forum/index.php?board=293.0",
		"http://www.ligagame.com/forum/index.php?board=136.0",
		"http://www.ligagame.com/forum/index.php?board=252.0",
		"http://www.ligagame.com/forum/index.php?board=324.0",
		"http://www.ligagame.com/forum/index.php?board=250.0",
		"http://www.ligagame.com/forum/index.php?board=167.0",
		"http://www.ligagame.com/forum/index.php?board=235.0",
		"http://www.ligagame.com/forum/index.php?board=236.0",
		"http://www.ligagame.com/forum/index.php?board=171.0",
		"http://www.ligagame.com/forum/index.php?board=312.0",
		"http://www.ligagame.com/forum/index.php?board=314.0",
		"http://www.ligagame.com/forum/index.php?board=313.0",
		"http://www.ligagame.com/forum/index.php?board=315.0",
		"http://www.ligagame.com/forum/index.php?board=316.0",
		"http://www.ligagame.com/forum/index.php?board=135.0",
		"http://www.ligagame.com/forum/index.php?board=387.0",
		"http://www.ligagame.com/forum/index.php?board=279.0",
		"http://www.ligagame.com/forum/index.php?board=331.0",
		"http://www.ligagame.com/forum/index.php?board=332.0",
		"http://www.ligagame.com/forum/index.php?board=307.0",
		"http://www.ligagame.com/forum/index.php?board=449.0",
		"http://www.ligagame.com/forum/index.php?board=163.0",
		"http://www.ligagame.com/forum/index.php?board=257.0",
		"http://www.ligagame.com/forum/index.php?board=403.0",
		"http://www.ligagame.com/forum/index.php?board=326.0",
		"http://www.ligagame.com/forum/index.php?board=350.0",
		"http://www.ligagame.com/forum/index.php?board=301.0",
		"http://www.ligagame.com/forum/index.php?board=309.0",
		"http://www.ligagame.com/forum/index.php?board=343.0",
		"http://www.ligagame.com/forum/index.php?board=237.0",
		"http://www.ligagame.com/forum/index.php?board=345.0",
		"http://www.ligagame.com/forum/index.php?board=346.0",
		"http://www.ligagame.com/forum/index.php?board=266.0",
		"http://www.ligagame.com/forum/index.php?board=253.0",
		"http://www.ligagame.com/forum/index.php?board=244.0",
		"http://www.ligagame.com/forum/index.php?board=308.0",
		"http://www.ligagame.com/forum/index.php?board=420.0",
		"http://www.ligagame.com/forum/index.php?board=125.0",
		"http://www.ligagame.com/forum/index.php?board=148.0",
		"http://www.ligagame.com/forum/index.php?board=242.0",
		"http://www.ligagame.com/forum/index.php?board=134.0",
		"http://www.ligagame.com/forum/index.php?board=234.0",
		"http://www.ligagame.com/forum/index.php?board=239.0",
		"http://www.ligagame.com/forum/index.php?board=240.0",
		"http://www.ligagame.com/forum/index.php?board=241.0",
		"http://www.ligagame.com/forum/index.php?board=321.0",
		"http://www.ligagame.com/forum/index.php?board=255.0",
		"http://www.ligagame.com/forum/index.php?board=260.0",
		"http://www.ligagame.com/forum/index.php?board=297.0",
		"http://www.ligagame.com/forum/index.php?board=338.0",
		"http://www.ligagame.com/forum/index.php?board=153.0",
		"http://www.ligagame.com/forum/index.php?board=178.0",
		"http://www.ligagame.com/forum/index.php?board=339.0",
		"http://www.ligagame.com/forum/index.php?board=361.0",
		"http://www.ligagame.com/forum/index.php?board=389.0",
		"http://www.ligagame.com/forum/index.php?board=445.0",
		"http://www.ligagame.com/forum/index.php?board=446.0",
		"http://www.ligagame.com/forum/index.php?board=327.0",
		"http://www.ligagame.com/forum/index.php?board=452.0",
		"http://www.ligagame.com/forum/index.php?board=448.0",
		"http://www.ligagame.com/forum/index.php?board=439.0",
		"http://www.ligagame.com/forum/index.php?board=179.0",
		"http://www.ligagame.com/forum/index.php?board=328.0",
		"http://www.ligagame.com/forum/index.php?board=384.0",
		"http://www.ligagame.com/forum/index.php?board=406.0",
		"http://www.ligagame.com/forum/index.php?board=430.0",
		"http://www.ligagame.com/forum/index.php?board=358.0",
		"http://www.ligagame.com/forum/index.php?board=302.0",
		"http://www.ligagame.com/forum/index.php?board=367.0",
		"http://www.ligagame.com/forum/index.php?board=262.0",
		"http://www.ligagame.com/forum/index.php?board=330.0",
		"http://www.ligagame.com/forum/index.php?board=129.0",
		"http://www.ligagame.com/forum/index.php?board=282.0",
		"http://www.ligagame.com/forum/index.php?board=374.0",
		"http://www.ligagame.com/forum/index.php?board=391.0",
		"http://www.ligagame.com/forum/index.php?board=411.0",
		"http://www.ligagame.com/forum/index.php?board=378.0",
		"http://www.ligagame.com/forum/index.php?board=373.0",
		"http://www.ligagame.com/forum/index.php?board=418.0",
		"http://www.ligagame.com/forum/index.php?board=351.0",
		"http://www.ligagame.com/forum/index.php?board=333.0",
		"http://www.ligagame.com/forum/index.php?board=399.0",
		"http://www.ligagame.com/forum/index.php?board=402.0",
		"http://www.ligagame.com/forum/index.php?board=407.0",
		"http://www.ligagame.com/forum/index.php?board=431.0",
		"http://www.ligagame.com/forum/index.php?board=254.0",
		"http://www.ligagame.com/forum/index.php?board=4.0",
		"http://www.ligagame.com/forum/index.php?board=5.0",
		"http://www.ligagame.com/forum/index.php?board=14.0",
		"http://www.ligagame.com/forum/index.php?board=108.0",
		"http://www.ligagame.com/forum/index.php?board=109.0",
		"http://www.ligagame.com/forum/index.php?board=113.0",
		"http://www.ligagame.com/forum/index.php?board=372.0",
		"http://www.ligagame.com/forum/index.php?board=370.0",
        ]
	COUNTRY = "IDN"
	THREAD_XPATH = "//span[re:test(@id,'msg_*')]"
	THREAD_LINK_XPATH = "./a/@href"
	LAST_PAGE_XPATH = "(//td[@class='middletext']/a[@class='navPages'])[last()]/@href"
	PREV_XPATH = "//td[@class='middletext']/b/preceding-sibling::a[1]/@href"
	POST_XPATH = "//form[@id='quickModForm']//td[@class='windowbg' or @class='windowbg2']"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": True,
			"xpath": ".//div[re:test(@id,'subject_*')]/following-sibling::div[1]/text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//a[re:test(@title,'View the profile*')]/text()"
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
			"xpath": ".//div[re:test(@id,'subject_*')]/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"(//div[@class='nav']//a[@class='nav'])[last()]/text()"
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
