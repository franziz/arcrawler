from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "xdtalk"
	CRAWLER_NAME = "Xdtalk Crawler"
	LINK_TO_CRAWL = [
		"http://www.xdtalk.com/forum/springfield-xd-xd-m-talk-announcements.17/",
		"http://www.xdtalk.com/forum/springfield-xd-xd-m-range-reports.8/",
		"http://www.xdtalk.com/forum/springfield-xd-xd-m-faq-stickies.10/",
		"http://www.xdtalk.com/forum/new-member-welcome-center.31/",
		"http://www.xdtalk.com/forum/general-springfield-xd-xd-m-talk.25/",
		"http://www.xdtalk.com/forum/springfield-xd-xd-m-accessories.9/",
		"http://www.xdtalk.com/forum/xd-mod-2.275/",
		"http://www.xdtalk.com/forum/xd-m-discussion-room-xd-m.54/",
		"http://www.xdtalk.com/forum/xd-45acp-discussion-room.29/",
		"http://www.xdtalk.com/forum/xd-s-discussion-room.122/",
		"http://www.xdtalk.com/forum/xd-gunsmithing-and-maintenance.89/",
		"http://www.xdtalk.com/forum/xdtalk-chatter-box.11/",
		"http://www.xdtalk.com/forum/m1a-series.281/",
		"http://www.xdtalk.com/forum/non-xd-handguns.30/",
		"http://www.xdtalk.com/forum/m1911.41/",
		"http://www.xdtalk.com/forum/wheelguns.71/",
		"http://www.xdtalk.com/forum/m1a-m14-talk.61/",
		"http://www.xdtalk.com/forum/ar-talk.47/",
		"http://www.xdtalk.com/forum/ak-47-talk.49/",
		"http://www.xdtalk.com/forum/shotgun-talk.65/",
		"http://www.xdtalk.com/forum/fal-talk.63/",
		"http://www.xdtalk.com/forum/garand-talk.62/",
		"http://www.xdtalk.com/forum/bullpup-talk.64/",
		"http://www.xdtalk.com/forum/modern-sporting-rifles.185/",
		"http://www.xdtalk.com/forum/bolt-guns-precision-rifles.68/",
		"http://www.xdtalk.com/forum/the-big-bang-50-bmg.67/",
		"http://www.xdtalk.com/forum/other-long-gun-talk.93/",
		"http://www.xdtalk.com/forum/the-ammo-can.26/",
		"http://www.xdtalk.com/forum/factory-loaded-ammunition.164/",
		"http://www.xdtalk.com/forum/hand-loaded-ammunition.165/",
		"http://www.xdtalk.com/forum/optics-and-glass.59/",
		"http://www.xdtalk.com/forum/gear-talk.86/",
		"http://www.xdtalk.com/forum/cold-steel.72/",
		"http://www.xdtalk.com/forum/nfa-talk.91/",
		"http://www.xdtalk.com/forum/c-r-talk.66/",
		"http://www.xdtalk.com/forum/gun-games-shooting-competition.14/",
		"http://www.xdtalk.com/forum/the-classroom.87/",
		"http://www.xdtalk.com/forum/ccw-and-open-carry-talk.88/",
		"http://www.xdtalk.com/forum/shtf-survival-disaster-preparedness.58/",
		"http://www.xdtalk.com/forum/general-firearms-maintenance-and-troubleshooting.90/",
		"http://www.xdtalk.com/forum/hunting.92/",
		"http://www.xdtalk.com/forum/photo-gallery.32/",
		"http://www.xdtalk.com/forum/shooters-calendar.13/",
		"http://www.xdtalk.com/forum/rusty-tales.27/",
		"http://www.xdtalk.com/forum/the-polling-place.28/",
		"http://www.xdtalk.com/forum/leo-talk.16/",
		"http://www.xdtalk.com/forum/u-s-military-services-veterans.45/",
		"http://www.xdtalk.com/forum/crossbreed-firearms-academy.101/",
		"http://www.xdtalk.com/forum/xdtalk-sponsor-announcements-showcase.39/",
		"http://www.xdtalk.com/forum/3-speed-holster.123/",
		"http://www.xdtalk.com/forum/alien-gear-holsters.170/",
		"http://www.xdtalk.com/forum/bigfoot-gun-belts.291/",
		"http://www.xdtalk.com/forum/black-arch-holsters.143/",
		"http://www.xdtalk.com/forum/boyds-gunstock-industries.163/",
		"http://www.xdtalk.com/forum/camera-land.121/",
		"http://www.xdtalk.com/forum/cheaper-than-dirt.139/",
		"http://www.xdtalk.com/forum/clinger-holsters.285/",
		"http://www.xdtalk.com/forum/crossbreed-holsters.52/",
		"http://www.xdtalk.com/forum/gearhog.129/",
		"http://www.xdtalk.com/forum/glow-on.118/",
		"http://www.xdtalk.com/forum/grabagun-com.126/",
		"http://www.xdtalk.com/forum/gunrange-com.301/",
		"http://www.xdtalk.com/forum/gun-mag-warehouse.183/",
		"http://www.xdtalk.com/forum/masc-holsters.277/",
		"http://www.xdtalk.com/forum/nereloading-com.286/",
		"http://www.xdtalk.com/forum/opticsplanet-com.151/",
		"http://www.xdtalk.com/forum/omaha-outdoors.293/",
		"http://www.xdtalk.com/forum/pistolgear-com.24/",
		"http://www.xdtalk.com/forum/powder-river-precision.104/",
		"http://www.xdtalk.com/forum/shooting-org.276/",
		"http://www.xdtalk.com/forum/silencer-shop.184/",
		"http://www.xdtalk.com/forum/slickguns-com.124/",
		"http://www.xdtalk.com/forum/springfield-armory.112/",
		"http://www.xdtalk.com/forum/swab-its.302/",
		"http://www.xdtalk.com/forum/tactical-performance-center.289/",
		"http://www.xdtalk.com/forum/tagua-gunleather.299/",
		"http://www.xdtalk.com/forum/tennessee-holster-company.20/",
		"http://www.xdtalk.com/forum/tucker-gunleather.108/",
		"http://www.xdtalk.com/forum/white-hat-holsters.125/",
		"http://www.xdtalk.com/forum/wikiarms-com.155/",
		"http://www.xdtalk.com/forum/xd-firearms-for-sale.77/",
		"http://www.xdtalk.com/forum/xd-accessories-for-sale.78/",
		"http://www.xdtalk.com/forum/other-firearms-for-sale.12/",
		"http://www.xdtalk.com/forum/other-firearms-accessories-for-sale.79/",
		"http://www.xdtalk.com/forum/optics-for-sale-or-trade.279/",
		"http://www.xdtalk.com/forum/non-firearms-related-for-sale.83/",
		"http://www.xdtalk.com/forum/want-to-buy.53/",
		"http://www.xdtalk.com/forum/want-to-trade.80/",
		"http://www.xdtalk.com/forum/rkba-news-and-information.82/",
		"http://www.xdtalk.com/forum/test-posting.22/",
		"http://www.xdtalk.com/forum/forum-feedback-issues.109/",
		"http://www.xdtalk.com/forum/video-gaming-central.48/",
		"http://www.xdtalk.com/forum/motor-sports.73/",
		"http://www.xdtalk.com/forum/outdoor-sports.75/",
		"http://www.xdtalk.com/forum/film-and-television.74/",
		"http://www.xdtalk.com/forum/cooking-recipes.117/"
        ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//ol[@class='discussionListItems']/li[re:test(@id,'thread-*')]"
	THREAD_LINK_XPATH = ".//a[@class='PreviewTooltip']/@href"
	LAST_PAGE_XPATH = "(//div[@class='PageNav']//a[not (contains(text(),'Next >'))])[last()]/@href"
	PREV_XPATH = "//div[@class='PageNav']//a[contains(text(),'< Prev')]/@href"
	POST_XPATH = "//ol[@id='messageList']/li[re:test(@id,'post-*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":"concat(.//span[@class='leftSide']/span[@class='DateTime']/span[@class='DateTime']/@title,.//span[@class='leftSide']/span[@class='DateTime']/abbr[@class='DateTime']/text())"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//h3[@class='userText']//a//text()"
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
			"xpath":"//div[@class='titleBar']/h1//text()"
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
