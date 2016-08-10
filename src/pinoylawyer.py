from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "pinoylawyer"
	CRAWLER_NAME = "Pinoylawyer Crawler"
	LINK_TO_CRAWL = [
		"http://www.pinoylawyer.org/f90-free-bar-review-materials-download",
		"http://www.pinoylawyer.org/f101-the-bench",
		"http://www.pinoylawyer.org/f102-the-bar",
		"http://www.pinoylawyer.org/f103-students-of-law",
		"http://www.pinoylawyer.org/f19-all-about-the-bar-exams",
		"http://www.pinoylawyer.org/f1-academic-discussions",
		"http://www.pinoylawyer.org/f2-groups-or-quasi-groups",
		"http://www.pinoylawyer.org/f20-labor-and-employment",
		"http://www.pinoylawyer.org/f21-family-and-marriage",
		"http://www.pinoylawyer.org/f22-property",
		"http://www.pinoylawyer.org/f48-obligations-contracts-credit-transactions",
		"http://www.pinoylawyer.org/f23-crime",
		"http://www.pinoylawyer.org/f24-name-and-surname-problems",
		"http://www.pinoylawyer.org/f77-business-and-trade",
		"http://www.pinoylawyer.org/f100-nbi-clearance",
		"http://www.pinoylawyer.org/f25-others",
		"http://www.pinoylawyer.org/f27-free-legal-advice",
		"http://www.pinoylawyer.org/f29-forum-rules",
		"http://www.pinoylawyer.org/f30-introduce-yourself",
		"http://www.pinoylawyer.org/f49-comments-and-suggestions",
		"http://www.pinoylawyer.org/f3-events-eb-s-gatherings",
		"http://www.pinoylawyer.org/f18-general-principles-updates"
        ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//td[@class='tcl tdtopics']"
	THREAD_LINK_XPATH = ".//a[@class='topictitle']/@href"
	LAST_PAGE_XPATH = "(//p[@class='paging']/a)[last()-1]/@href"
	PREV_XPATH = "//p[@class='paging']//img[@alt='Previous']//parent::a/@href"
	POST_XPATH = "//div[re:test(@class,'post post--*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":".//div[@class='posthead']/h2/text()[2]"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//h4[@class='username']//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='entry-content']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//div[@class='posthead']/h2/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"(//span[@class='crumbs']//a)[last()]//text()"
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
