from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "captiva-club"
	CRAWLER_NAME = "Captiva-club Crawler"
	LINK_TO_CRAWL = [
                "http://www.captiva-club.com/cctforum/index.php?board=2.0",
                "http://www.captiva-club.com/cctforum/index.php?board=3.0",
                "http://www.captiva-club.com/cctforum/index.php?board=1.0",
                "http://www.captiva-club.com/cctforum/index.php?board=24.0",
                "http://www.captiva-club.com/cctforum/index.php?board=4.0",
                "http://www.captiva-club.com/cctforum/index.php?board=10.0",
                "http://www.captiva-club.com/cctforum/index.php?board=7.0",
                "http://www.captiva-club.com/cctforum/index.php?board=6.0",
                "http://www.captiva-club.com/cctforum/index.php?board=9.0",
				"http://www.captiva-club.com/cctforum/index.php?board=8.0",
                "http://www.captiva-club.com/cctforum/index.php?board=11.0",
                "http://www.captiva-club.com/cctforum/index.php?board=13.0",
                "http://www.captiva-club.com/cctforum/index.php?board=12.0"
        ]
	COUNTRY = "THA"
	THREAD_XPATH = "//span[re:test(@id,'msg_*')]"
	THREAD_LINK_XPATH = "./a/@href"
	LAST_PAGE_XPATH = "(//div[re:test(@class,'pagelinks*')]//a[@class='navPages'])[last()]/@href"
	PREV_XPATH = "(//div[@class='pagesection']//div[@class='pagelinks floatleft']//strong)[1]//preceding-sibling::a[@class='navPages'][1]/@href"
	POST_XPATH = "//form[@id='quickModForm']//div[re:test(@class,'windowbg*')]"
	FIELDS = [
        {"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":"concat(./preceding-sibling::div[@class='topbar_post']/div[@class='smalltext']/b/text(),' ',translate((./preceding-sibling::div[@class='topbar_post']/div[@class='smalltext']/text())[last()],' เวลา ',''))"
			# "xpath":"(.//preceding-sibling::div[@class='topbar_post']//div[@class='smalltext']//text())[last()]"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//div[@class='poster']//h4//a//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":".//div[@class='post']//div[@class='inner']//text()"
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
                        "xpath":"normalize-space(substring-before(substring-after(//h3[@class='catbg']//text()[3],': '),'('))"
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
