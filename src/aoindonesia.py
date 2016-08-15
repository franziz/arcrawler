from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "aoindonesia"
	CRAWLER_NAME = "Aoindonesia Crawler"
	LINK_TO_CRAWL = [
		"http://aoindonesia.net/forums/introduce-yourself.37/",		
		"http://aoindonesia.net/forums/aoi-dictionary.54/",
		"http://aoindonesia.net/forums/aoi-international-lounge.47/",		
		"http://aoindonesia.net/forums/event.49/",
		"http://aoindonesia.net/forums/past-event.113/",
		"http://aoindonesia.net/forums/anime-rg-fansub.48/",		
		"http://aoindonesia.net/forums/aoi-magazine.115/",
		"http://aoindonesia.net/forums/aoi-reviewer-corner.135/",		
		"http://aoindonesia.net/forums/anime-discussion.6/",
		"http://aoindonesia.net/forums/anime-review.5/",
		"http://aoindonesia.net/forums/anime-project.117/",		
		"http://aoindonesia.net/forums/manga-review.8/",
		"http://aoindonesia.net/forums/manga-discussion.9/",		
		"http://aoindonesia.net/forums/japan-today.56/",
		"http://aoindonesia.net/forums/nihongo-no-kaiwa-no-kiso.18/",		
		"http://aoindonesia.net/forums/boundary-of-gensoukyo.66/",
		"http://aoindonesia.net/forums/touhou-challenge.100/",
		"http://aoindonesia.net/forums/touhou-based-doujin-game.116/",
		"http://aoindonesia.net/forums/touhou-doujin.81/",
		"http://aoindonesia.net/forums/touhou-game.79/",
		"http://aoindonesia.net/forums/touhou-music.78/",
		"http://aoindonesia.net/forums/touhou-video.80/",		
		"http://aoindonesia.net/forums/share-mp3.70/",
		"http://aoindonesia.net/forums/introduce-yourself.37/"
	]
	COUNTRY = "IDN"
	THREAD_XPATH = "//ol[@class='discussionListItems']/li[re:test(@id,'thread-*')]"
	THREAD_LINK_XPATH = ".//a[@class='PreviewTooltip']/@href"
	LAST_PAGE_XPATH = "(//div[@class='PageNav']//a)[last()-1]/@href"
	PREV_XPATH = "//div[@class='PageNav']//a[@class='currentPage ']/preceding-sibling::a[1]/@href"
	POST_XPATH = "//ol[@id='messageList']/li[re:test(@id,'post-*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath": ".//span[@class='authorEnd']/following-sibling::a[@class='datePermalink']//text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//h3[@class='userText']/a/text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='messageContent']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//div[@class='publicControls']/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"(//span[@class='crumbs']//a[@class='crumb'])[last()]//text()"
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
