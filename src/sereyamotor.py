from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
        NETWORK_TOOLS = NetworkTools(use_proxy=False)
        TEMPLATE = "crawler.arct"
        TEST_TEMPLATE = "crawler_test.arct"
        DB_SERVER_ADDRESS = "mongo:27017"
        DB_SERVER_NAME = "serayamotor"
        CRAWLER_NAME = "Serayamotor Crawler"
        LINK_TO_CRAWL = [
                "https://www.serayamotor.com/diskusi/viewforum.php?f=27",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=4",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=25",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=17",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=82",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=64"
                "https://www.serayamotor.com/diskusi/viewforum.php?f=40",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=82",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=19",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=18",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=3",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=5",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=9",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=8",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=12",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=52",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=11",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=6",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=7",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=22",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=23",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=24",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=51",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=43",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=2",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=16",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=44",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=42",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=46",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=81",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=37",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=73",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=54",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=62",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=55",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=56",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=57",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=58",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=59",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=74",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=75",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=76",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=77",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=78",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=66",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=67",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=68",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=69",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=70",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=34",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=63",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=1",
                "https://www.serayamotor.com/diskusi/viewforum.php?f=13"
        ]

        COUNTRY = "IDN"
        THREAD_XPATH ="//ul[@class='topiclist topics']//li[re:test(@class,'row bg*')]//a[@class='topictitle']"
        THREAD_LINK_XPATH ="concat('diskusi/',./@href)"
        LAST_PAGE_XPATH ="concat(substring(concat('diskusi/',(//div[@class='pagination']//ul//li[not(contains(@class,'next'))]//a)[last()]//@href),1 div contains((//div[@class='pagination']//ul//li[not(contains(@class,'next'))]//a)[last()]//@href,'./viewtopic')),substring('',1 div not(contains((//div[@class='pagination']//ul//li[not(contains(@class,'next'))]//a)[last()]//@href,'./viewtopic'))))"
        PREV_XPATH ="concat(substring(concat('diskusi/',//div[@class='pagination']//ul//li//a[@rel='prev']//@href),1 div contains(//div[@class='pagination']//ul//li//a[@rel='prev']//@href,'./viewtopic')),substring('',1 div not(contains(//div[@class='pagination']//ul//li//a[@rel='prev']//@href,'./viewtopic'))))"
        POST_XPATH ="//div[re:test(@id,'p*') and re:test(@class,'post has-profile bg*')]"
        FIELDS = [
		{"published_date": {
			"single": True, 
			"data_type": "date",
			"concat": False, 
                        "xpath":".//p[@class='author']/text()"
		}},
		{"permalink": {
			"single": True, 
			"data_type": "url", 
			"concat": False, 
                        "xpath":"concat('diskusi/',//h2[@class='topic-title']/a/@href,.//h3/a/@href)"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":".//strong/a[re:test(@class,'username*')]//text()"
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
			"xpath":"//h2[@class='topic-title']//text()"
		}}
	]
        CONDITIONS={
                "has_to_have_content":{
                        "condition":'"content" in document',
                        "exception":'"content is not defined"'
                },
                "has_to_have_published_date":{
                        "condition":'"published_date" in document',
                        "exception":'"published_date is not defined"'
                },
                "has_to_have_title":{
                        "condition":'"title" in document',
                        "exception":'"title is not defined"'
                },
                "has_to_have_author_name":{
                        "condition":'"author_name" in document',
                        "exception":'"author_name is not defined"'
                },
                "has_to_have_permalink":{
                        "condition":'"permalink" in document',
                        "exception":'"permalink is not defined"'
                },
                "content_cannot_be_empty":{
                        "condition":'len(document["content"]) > 0',
                        "exception":'"content cannot be empty"'
                },
                "published_date_cannot_be_empty":{
                        "condition":'document["published_date"] is not None',
                        "exception":'"published_date cannot be empty"'
                },
                "title_cannot_be_empty":{
                        "condition":'len(document["title"]) > 0',
                        "exception":'"title cannot be empty"'
                },
                "author_name_cannot_be_empty":{
                        "condition":'len(document["author_name"]) > 0',
                        "exception":'"author_name cannot be empty"'
                },
                "permalink_cannot_be_empty":{
                        "condition":'len(document["permalink"]) > 0',
                        "exception":'"permalink cannot be empty"'
                },
        }
#end class
