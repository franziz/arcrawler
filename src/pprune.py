from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "pprune"
	CRAWLER_NAME = "Pprune Crawler"
	LINK_TO_CRAWL = [
		"http://www.pprune.org/rumours-news-13/",
		"http://www.pprune.org/tech-log-15/",
		"http://www.pprune.org/terms-endearment-38/",
		"http://www.pprune.org/australia-new-zealand-pacific-90/",
		"http://www.pprune.org/pacific-general-aviation-questions-91/",
		"http://www.pprune.org/fragrant-harbour-19/",
		"http://www.pprune.org/african-aviation-37/",
		"http://www.pprune.org/canada-42/",
		"http://www.pprune.org/north-america-43/",
		"http://www.pprune.org/middle-east-44/",
		"http://www.pprune.org/south-asia-far-east-45/",
		"http://www.pprune.org/caribbean-latin-america-64/",
		"http://www.pprune.org/nordic-forum-72/",
		"http://www.pprune.org/french-forum-73/",
		"http://www.pprune.org/spanish-forum-74/",
		"http://www.pprune.org/italian-forum-94/",
		"http://www.pprune.org/freight-dogs-41/",
		"http://www.pprune.org/rotorheads-23/",
		"http://www.pprune.org/biz-jets-ag-flying-ga-etc-36/",
		"http://www.pprune.org/military-aviation-57/",
		"http://www.pprune.org/flying-instructors-examiners-17/",
		"http://www.pprune.org/cabin-crew-131/",
		"http://www.pprune.org/flight-testing-50/",
		"http://www.pprune.org/professional-pilot-training-includes-ground-studies-14/",
		"http://www.pprune.org/interviews-jobs-sponsorship-104/",
		"http://www.pprune.org/cabin-crew-wannabes-130/",
		"http://www.pprune.org/south-asia-far-east-wannabes-99/",
		"http://www.pprune.org/atc-issues-18/",
		"http://www.pprune.org/engineers-technicians-22/",
		"http://www.pprune.org/flight-ground-ops-crewing-dispatch-39/",
		"http://www.pprune.org/safety-crm-qa-emergency-response-planning-93/",
		"http://www.pprune.org/medical-health-62/",
		"http://www.pprune.org/questions-67/",
		"http://www.pprune.org/private-flying-63/",
		"http://www.pprune.org/accidents-close-calls-139/",
		"http://www.pprune.org/non-airline-transport-stuff-58/",
		"http://www.pprune.org/airlines-airports-routes-85/",
		"http://www.pprune.org/spectators-balcony-spotters-corner-52/",
		"http://www.pprune.org/aviation-history-nostalgia-86/",
		"http://www.pprune.org/passengers-slf-self-loading-freight-61/",
		"http://www.pprune.org/computer-internet-issues-troubleshooting-46/",
		"http://www.pprune.org/jet-blast-16/",
		"http://www.pprune.org/night-stop-21/",
		"http://www.pprune.org/where-they-now-20/",
        ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//a[re:test(@id,'thread_title_*')]"
	THREAD_LINK_XPATH = "./@href"
	LAST_PAGE_XPATH = "(//div[@class='pagenav']//td[@class='vbmenu_control'])[last()]//preceding::a[re:test(@title,'Last Page*') or re:test(@title,'Show results*')][1]/@href"
	PREV_XPATH = "//div[@class='pagenav']//a[@rel='prev']/@href"
	POST_XPATH = "//div[@id='posts']//table[re:test(@id,'post*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": True,
			"xpath":".//a[re:test(@name,'post*')]/following-sibling::text()[1]"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//a[@class='bigusername']//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[re:test(@id,'post_message_*')]//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//a[re:test(@id,'postcount*')]/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//td[@class='navbar']/strong/text()"
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
