from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "yamahat135"
	CRAWLER_NAME = "Yamahat135 Crawler"
	LINK_TO_CRAWL = [
		"http://www.yamahat135.com/forums/t150-t135-general-topics.21/",
		"http://www.yamahat135.com/forums/safety-riding-gears-equipments.64/",
		"http://www.yamahat135.com/forums/electrical.65/",
		"http://www.yamahat135.com/forums/modification.22/",
		"http://www.yamahat135.com/forums/engine.23/",
		"http://www.yamahat135.com/forums/tips-and-tricks.24/",
		"http://www.yamahat135.com/forums/parts-accessories.26/",
		"http://www.yamahat135.com/forums/yamaha-r25.104/",
		"http://www.yamahat135.com/forums/yamaha-yzf-r15.36/",
		"http://www.yamahat135.com/forums/yamaha-vixion-fz150i.35/",
		"http://www.yamahat135.com/forums/yamaha-yzf-r125.37/",
		"http://www.yamahat135.com/forums/yamaha-mio-mx-nouvo-elegance-nouvolc.39/",
		"http://www.yamahat135.com/forums/yamaha-crypton-jupiter-z-z1-x1-lagenda-yz125.40/",
		"http://www.yamahat135.com/forums/all-other-bikes.41/",
		"http://www.yamahat135.com/forums/manuals-parts-catalog-service-manuals.54/",
		"http://www.yamahat135.com/forums/touring-and-rides.27/",
		"http://www.yamahat135.com/forums/racing.30/",
		"http://www.yamahat135.com/forums/off-topics.25/",
		"http://www.yamahat135.com/forums/t150-t135-riders-blog-showbike-area.19/",
		"http://www.yamahat135.com/forums/japan-t150-t135-spark-135i.7/",
		"http://www.yamahat135.com/forums/greece-yamaha-crypton-x-150-135.8/",
		"http://www.yamahat135.com/forums/vietnam-exciter-150-t150-rc-135-gp.9/",
		"http://www.yamahat135.com/forums/philippines-sniper-mx-150-135-x1r.10/",
		"http://www.yamahat135.com/forums/maldives-t150-t135-owners.11/",
		"http://www.yamahat135.com/forums/bermuda-150-135-sniper-owners.12/",
		"http://www.yamahat135.com/forums/malaysia-lc150-135lc-owners.13/",
		"http://www.yamahat135.com/forums/brunei-spark-150-135.14/",
		"http://www.yamahat135.com/forums/thailand-spark-150-135-x1r.15/",
		"http://www.yamahat135.com/forums/singapore-spark-150-135.16/",
		"http://www.yamahat135.com/forums/indonesia-jupiter-mx-150-135.17/",
		"http://www.yamahat135.com/forums/csc-caraga-sniper-club.70/",
		"http://www.yamahat135.com/forums/clab-q-sniper-owners-club.74/",
		"http://www.yamahat135.com/forums/dsg-davao-sniper-guild.62/",
		"http://www.yamahat135.com/forums/msc-mindanao-sniper-club.61/",
		"http://www.yamahat135.com/forums/rpm-rizal-pasig-marikina-sniper-club.103/",
		"http://www.yamahat135.com/forums/scot-sniper-club-of-tarlac.69/",
		"http://www.yamahat135.com/forums/soc-sniper-mx-owners-club.72/",
		"http://www.yamahat135.com/forums/socno-sniper-owners-club-of-negros-oriental.66/",
		"http://www.yamahat135.com/forums/sorx-sniper-owners-of-region-x.60/",
		"http://www.yamahat135.com/forums/sos-sniper-owners-society.48/",
		"http://www.yamahat135.com/forums/smxp-sniper-mx-phils-inc.99/",
		"http://www.yamahat135.com/forums/uscc-united-snipers-club-cebu.100/",
		"http://www.yamahat135.com/forums/xos-x1r-owners-society.49/",
		"http://www.yamahat135.com/forums/ysc-yamaha-sniper-owners-club-bacolod.82/",
		"http://www.yamahat135.com/forums/for-sale.43/",
		"http://www.yamahat135.com/forums/looking-for.44/",
		"http://www.yamahat135.com/forums/other-items.45/",
		"http://www.yamahat135.com/forums/feedback-ratings.46/",
		"http://www.yamahat135.com/forums/news-info-and-events.4/"        ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//ol[@class='discussionListItems']/li[re:test(@id,'thread-*')]"
	THREAD_LINK_XPATH = ".//a[@class='PreviewTooltip']/@href"
	LAST_PAGE_XPATH = "(//div[@class='PageNav']//a[not(contains(text(),'Next >'))])[last()]/@href"
	PREV_XPATH = "//div[@class='PageNav']//a[contains(text(),'< Prev')]/@href"
	POST_XPATH = "//ol[@class='messageList']/li[re:test(@id,'post-*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":"concat(.//a[@class='datePermalink']/span/@title,.//a[@class='datePermalink']/abbr/text())"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath": ".//a[@class='username']//text()"
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
