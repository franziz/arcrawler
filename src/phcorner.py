from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "phcorner"
	CRAWLER_NAME = "Phcorner Crawler"
	LINK_TO_CRAWL = [
		"http://www.phcorner.net/announcements/", 
		"http://www.phcorner.net/f/new-members-corner.7/",
		"http://www.phcorner.net/f/feedbacks-suggestion.5/",
		"http://www.phcorner.net/f/site-assistance.235/",
		"http://www.phcorner.net/f/globe-telecom-touch-mobile.134/",
		"http://www.phcorner.net/f/globe-tm-questions.250/",
		"http://www.phcorner.net/f/smart-talk-n-text-sun.135/",
		"http://www.phcorner.net/f/smart-tnt-sun-questions.251/",
		"http://www.phcorner.net/f/general-mobile-network-tutorials.137/",
		"http://www.phcorner.net/f/mobile-network-questions.202/",
		"http://www.phcorner.net/f/free-internet-tricks.139/",
		"http://www.phcorner.net/f/internet-tricks-questions.59/",
		"http://www.phcorner.net/f/mobile-broadband-modems.203/",
		"http://www.phcorner.net/f/mobile-broadband-questions.234/",
		"http://www.phcorner.net/f/wimax-dsl-modems.230/",
		"http://www.phcorner.net/f/wimax-dsl-questions.233/",
		"http://www.phcorner.net/f/android-phones.60/",
		"http://www.phcorner.net/f/ios-iphone-ipad-ipod.64/",
		"http://www.phcorner.net/f/java-phone.179/",
		"http://www.phcorner.net/f/symbian-phone.180/",
		"http://www.phcorner.net/f/general-mobile-discussion.52/",
		"http://www.phcorner.net/f/modded-mobile-application.138/",
		"http://www.phcorner.net/f/mobile-modding-tools.140/",
		"http://www.phcorner.net/f/mobile-phone-questions.215/",
		"http://www.phcorner.net/f/computer-repair-questions.100/",
		"http://www.phcorner.net/f/windows-tools-tips.103/",
		"http://www.phcorner.net/f/drivers-hardware.101/",
		"http://www.phcorner.net/f/windows-themes.99/",
		"http://www.phcorner.net/f/windows-applications-freeware-only.90/",
		"http://www.phcorner.net/f/linux-distributions.112/",
		"http://www.phcorner.net/f/gfx-corner.107/",
		"http://www.phcorner.net/f/web-internet.104/",
		"http://www.phcorner.net/f/coding-programming.127/",
		"http://www.phcorner.net/f/clash-of-clans.249/",
		"http://www.phcorner.net/f/browser-games.97/",
		"http://www.phcorner.net/f/role-playing-game.237/",
		"http://www.phcorner.net/f/simulation-game.239/",
		"http://www.phcorner.net/f/handheld-game-console.171/",
		"http://www.phcorner.net/f/game-cheats.98/",
		"http://www.phcorner.net/f/academic-campus-talk.22/",
		"http://www.phcorner.net/f/arts-literature.226/",
		"http://www.phcorner.net/f/appliance-troubleshooting.229/",
		"http://www.phcorner.net/f/contests-freebies-giveaways.16/",
		"http://www.phcorner.net/f/jobs-employment.206/",
		"http://www.phcorner.net/f/lifestyle-healthy-living.12/",
		"http://www.phcorner.net/f/sports.15/",
		"http://www.phcorner.net/f/gags-jokes.21/",
		"http://www.phcorner.net/f/general-chat.18/"
        ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//ol[@class='discussionListItems']/li[re:test(@id,'thread-*')]"
	THREAD_LINK_XPATH = ".//h3[@class='title']/a[@class='PreviewTooltip']/@href"
	LAST_PAGE_XPATH = "(//div[@class='PageNav']//a)[last()-1]/@href"
	PREV_XPATH = "//div[@class='PageNav']//a[contains(text(),'< Prev')]/@href"
	POST_XPATH = "//ol[@class='messageList']/li"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":"concat(.//span[@class='DateTime']/@title,.//abbr[@class='DateTime']/text())"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":".//a[@class='username']//text()"
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
			"xpath": ".//a[@title='Permalink']/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"(//span[@class='crumbs']//a[@class='crumb'])[last()]/span/text()"
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
