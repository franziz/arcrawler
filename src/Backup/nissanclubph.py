from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "nissanclubph"
	CRAWLER_NAME = "Nissanclubph Crawler"
	LINK_TO_CRAWL = [
		"http://nissanclubph.proboards.com/board/9/general-board",
		"http://nissanclubph.proboards.com/board/18/newbie-help",
		"http://nissanclubph.proboards.com/board/27/updates",
		"http://nissanclubph.proboards.com/board/31/where-find-parts",
		"http://nissanclubph.proboards.com/board/14/user-manuals-repair",
		"http://nissanclubph.proboards.com/board/1/350z",
		"http://nissanclubph.proboards.com/board/2/adresort",
		"http://nissanclubph.proboards.com/board/3/altima",
		"http://nissanclubph.proboards.com/board/7/eagle",
		"http://nissanclubph.proboards.com/board/8/frontier",
		"http://nissanclubph.proboards.com/board/10/gt",
		"http://nissanclubph.proboards.com/board/11/livina",
		"http://nissanclubph.proboards.com/board/15/maxima",
		"http://nissanclubph.proboards.com/board/17/navarra",
		"http://nissanclubph.proboards.com/board/19/pathfinder",
		"http://nissanclubph.proboards.com/board/20/patrol",
		"http://nissanclubph.proboards.com/board/21/safari",
		"http://nissanclubph.proboards.com/board/22/sentra",
		"http://nissanclubph.proboards.com/board/24/silvia",
		"http://nissanclubph.proboards.com/board/25/skyline",
		"http://nissanclubph.proboards.com/board/26/terrano",
		"http://nissanclubph.proboards.com/board/32/xtrail",
		"http://nissanclubph.proboards.com/board/5/bnew-cars",
		"http://nissanclubph.proboards.com/board/29/used-cars",
		"http://nissanclubph.proboards.com/board/6/bnew-parts",
		"http://nissanclubph.proboards.com/board/30/used-parts",
		"http://nissanclubph.proboards.com/board/4/bnew-accessories",
		"http://nissanclubph.proboards.com/board/28/used-accessories",
		"http://nissanclubph.proboards.com/board/12/looking-bnew-parts-accessories",
		"http://nissanclubph.proboards.com/board/13/looking-used-parts-accessories",
		"http://nissanclubph.proboards.com/board/16/recommened-places-mechanics-get-fixed",
		"http://nissanclubph.proboards.com/board/23/recommended-places-car-serviced"
    ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//span[@class='link target']"
	THREAD_LINK_XPATH = "./a/@href"
	LAST_PAGE_XPATH = "(//ul[re:test(@class,'ui-pagination')]/li)[last()-1]/a/@href"
	PREV_XPATH = "//ul[re:test(@class,'ui-pagination')]/li[@class='ui-pagination-page ui-pagination-prev']/a/@href"
	POST_XPATH = "//tr[re:test(@id,'post-*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":"substring-before(.//span[@class='date']//text(),'GMT')"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": "concat(//span[@class='user-guest']/text(),.//a[re:test(@class,'user-link*')]/text())"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='message']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//a[@class='button quote-button ']/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"(//ul[@id='nav-tree']/li)[last()]//text()"
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
