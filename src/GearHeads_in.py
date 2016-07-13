from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "gearheads"
	CRAWLER_NAME = "Gearheads Crawler"
	LINK_TO_CRAWL = [
		"http://gearheads.in/forumdisplay.php?108-Hyundai",
		"http://gearheads.in/forumdisplay.php?144-Verna",
		"http://gearheads.in/forumdisplay.php?339-Creta",
		"http://gearheads.in/forumdisplay.php?141-Santro",
                "http://gearheads.in/forumdisplay.php?105-Maruti",
                "http://gearheads.in/forumdisplay.php?322-Celerio",
                "http://gearheads.in/forumdisplay.php?344-Baleno",
                "http://gearheads.in/forumdisplay.php?330-Ciaz",
                "http://gearheads.in/forumdisplay.php?340-S-Cross",
                "http://gearheads.in/forumdisplay.php?343-Vitara-Brezza",
                "http://gearheads.in/forumdisplay.php?165-Swift",
                "http://gearheads.in/forumdisplay.php?164-Ritz",
                "http://gearheads.in/forumdisplay.php?161-Alto",
                "http://gearheads.in/forumdisplay.php?259-WagonR",
                "http://gearheads.in/forumdisplay.php?158-M800",
                "http://gearheads.in/forumdisplay.php?159-Omni",
                "http://gearheads.in/forumdisplay.php?162-Estilo",
                "http://gearheads.in/forumdisplay.php?163-A-Star",
                "http://gearheads.in/forumdisplay.php?251-Gypsy",
                "http://gearheads.in/forumdisplay.php?167-SX-4",
                "http://gearheads.in/forumdisplay.php?168-Grand-Vitara",
                "http://gearheads.in/forumdisplay.php?258-Kizashi",
                "http://gearheads.in/forumdisplay.php?323-Eeco",
                "http://gearheads.in/forumdisplay.php?173-Dealers",
                "http://gearheads.in/forumdisplay.php?169-Discontinued",
                "http://gearheads.in/forumdisplay.php?171-Zen",
                "http://gearheads.in/forumdisplay.php?172-Baleno",
                "http://gearheads.in/forumdisplay.php?301-Esteem"
        ]        
	COUNTRY = "IND"
	THREAD_XPATH = "//ol//li[re:test(@id,'thread*')]"
	THREAD_LINK_XPATH = ".//a[@class='title']/@href"
	LAST_PAGE_XPATH = "//span[@class='first_last']/a/@href"
	PREV_XPATH = "//a[@rel='prev']/@href"
	POST_XPATH = "//ol//li[re:test(@id,'post_*')]"
	FIELDS = [
		{"published_date": {
			"single": True, 
			"data_type": "date", 
			"concat": False, 
			"xpath": ".//span[@class='date']//text()"
		}},
		{"permalink": {
			"single": True, 
			"data_type": "url", 
			"concat": False, 
			"xpath": ".//span[@class='nodecontrols']/a/@href"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":".//a[re:test(@class,'username')]//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='content']//text()"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//span[@class='threadtitle']//text()"
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
