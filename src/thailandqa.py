from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "thailandqa"
	CRAWLER_NAME = "Thailandqa Crawler"
	LINK_TO_CRAWL = [
		"http://www.thailandqa.com/forum/forumdisplay.php?18-Thailand-News-Stories",		
		"http://www.thailandqa.com/forum/forumdisplay.php?79-Member-s-Trip-Reports",
		"http://www.thailandqa.com/forum/forumdisplay.php?11-Thailand-Guidebook",
		"http://www.thailandqa.com/forum/forumdisplay.php?42-Bangkok-Guidebook",
		"http://www.thailandqa.com/forum/forumdisplay.php?77-Isaan-Guidebook",
		"http://www.thailandqa.com/forum/forumdisplay.php?48-Chiang-Mai-and-Northern-Thailand",
		"http://www.thailandqa.com/forum/forumdisplay.php?36-Shopping-in-Bangkok",
		"http://www.thailandqa.com/forum/forumdisplay.php?64-South-East-Asia-Guidebooks",
		"http://www.thailandqa.com/forum/forumdisplay.php?90-Vietnam",
		"http://www.thailandqa.com/forum/forumdisplay.php?78-Malaysia-amp-Singapore",
		"http://www.thailandqa.com/forum/forumdisplay.php?65-Myanmar-(Burma)",
		"http://www.thailandqa.com/forum/forumdisplay.php?66-Laos",
		"http://www.thailandqa.com/forum/forumdisplay.php?67-Cambodia",
		"http://www.thailandqa.com/forum/forumdisplay.php?62-Samut-Prakan",
		"http://www.thailandqa.com/forum/forumdisplay.php?80-Restaurants",
		"http://www.thailandqa.com/forum/forumdisplay.php?13-Thai-for-Beginners",
		"http://www.thailandqa.com/forum/forumdisplay.php?81-Learning-Thai-Highlights",		
		"http://www.thailandqa.com/forum/forumdisplay.php?44-Thai-Songs-in-English",
		"http://www.thailandqa.com/forum/forumdisplay.php?38-Thai-Grammar",
		"http://www.thailandqa.com/forum/forumdisplay.php?15-Thailand-Life-and-Culture",
		"http://www.thailandqa.com/forum/forumdisplay.php?60-Thai-Relationships-and-Marriage",
		"http://www.thailandqa.com/forum/forumdisplay.php?22-Living-and-Working-in-Thailand",
		"http://www.thailandqa.com/forum/forumdisplay.php?25-Thai-Music",
		"http://www.thailandqa.com/forum/forumdisplay.php?37-Thai-TV-Internet-amp-Technology",
		"http://www.thailandqa.com/forum/forumdisplay.php?35-Thai-Movies-and-TV-Lakorn",
		"http://www.thailandqa.com/forum/forumdisplay.php?41-Enjoy-Thai-Food",
		"http://www.thailandqa.com/forum/forumdisplay.php?33-Thai-Buddhism",		
		"http://www.thailandqa.com/forum/forumdisplay.php?31-Off-Topic-Forum-(English-Language-Only)",
		"http://www.thailandqa.com/forum/forumdisplay.php?32-Off-Topic-Forum-(Thai-Language-Only)"
    ]
	COUNTRY = "THA"
	THREAD_XPATH = "//div[@class='threadlist']//ol[@id='stickies' or @id='threads']/li"
	THREAD_LINK_XPATH = "concat(substring(concat('forum/',.//a[@class='title']/@href),1 div contains(.//a[@class='title']/@href,'showthread')),substring('',1 div not(contains(.//a[@class='title']/@href,'showthread'))))"
	LAST_PAGE_XPATH = "concat(substring(concat('forum/',//div[@class='pagination_top']//span[@class='first_last']/a/@href),1 div contains(//div[@class='pagination_top']//span[@class='first_last']/a/@href,'showthread')),substring('',1 div not(contains(//div[@class='pagination_top']//span[@class='first_last']/a/@href,'showthread'))))"
	PREV_XPATH = "concat(substring(concat('forum/',//div[@class='pagination_top']//span[@class='prev_next']/a/@href),1 div contains(//div[@class='pagination_top']//span[@class='prev_next']/a/@href,'showthread')),substring('',1 div not(contains(//div[@class='pagination_top']//span[@class='prev_next']/a/@href,'showthread'))))"
	POST_XPATH = "//ol[@id='posts']/li[@class='postbit postbitim postcontainer old']"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": True,
			"xpath":".//span[@class='date']//text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//div[@class='username_container']//strong[1]//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='postbody']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": "concat('forum/',.//a[@class='postcounter']/@href)"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@class='breadcrumb']//li[@class='navbit lastnavbit']/span/text()"
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
