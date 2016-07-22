from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "aethailand"
	CRAWLER_NAME = "Aethailand Crawler"
	LINK_TO_CRAWL = [
		'http://www.aethailand.com/forum/index.php?board=13.0',
		'http://www.aethailand.com/forum/index.php?board=12.0',
		'http://www.aethailand.com/forum/index.php?board=1.0',
		'http://www.aethailand.com/forum/index.php?board=30.0',
		'http://www.aethailand.com/forum/index.php?board=19.0',
		'http://www.aethailand.com/forum/index.php?board=20.0',
		'http://www.aethailand.com/forum/index.php?board=21.0',
		'http://www.aethailand.com/forum/index.php?board=22.0',
		'http://www.aethailand.com/forum/index.php?board=27.0',
		'http://www.aethailand.com/forum/index.php?board=23.0',
		'http://www.aethailand.com/forum/index.php?board=24.0',
		'http://www.aethailand.com/forum/index.php?board=25.0',
		'http://www.aethailand.com/forum/index.php?board=26.0',
		'http://www.aethailand.com/forum/index.php?board=28.0',
		'http://www.aethailand.com/forum/index.php?board=7.0',  ## High Frequency ##
		'http://www.aethailand.com/forum/index.php?board=8.0',
		'http://www.aethailand.com/forum/index.php?board=9.0',
		'http://www.aethailand.com/forum/index.php?board=31.0',
		'http://www.aethailand.com/forum/index.php?board=4.0',
		'http://www.aethailand.com/forum/index.php?board=5.0',
		'http://swww.aethailand.com/forum/index.php?board=6.0',
		'http://www.aethailand.com/forum/index.php?board=15.0',
		'http://www.aethailand.com/forum/index.php?board=17.0',
        ]
	COUNTRY = "THA"
	THREAD_XPATH = "//td[re:test(@class,'windowbg*') and @valign='middle' and not(contains(@width, '4%'))]//span[re:test(@id,'msg_*')]"
	THREAD_LINK_XPATH = "./a/@href"
	LAST_PAGE_XPATH = "//td[@class='middletext']//a[@class='navPages'][last()]/@href"
	PREV_XPATH = "//td[@class='middletext']/b/preceding-sibling::a[1]/@href"
	POST_XPATH = "//form[@id='quickModForm']//td[@class='windowbg' or @class='windowbg2']"
	FIELDS = [
		 {"published_date": {
		 	"single": True,
		 	"data_type": "date",
		 	"concat": False,
		 	"xpath": "substring-before(concat(..//td[@valign='middle']//div[@class='smalltext']/text()[2],..//td[@valign='middle']//div[@class='smalltext']/text()[3]),'»')"
		 }},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//div[re:test(@id,'subject_*')]/a/@href"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"normalize-space(.//td[@rowspan=2]/b/a/text())"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='post']//text()"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"normalize-space(//div[@class='nav']//b[last()]//a[@class='nav']//text())"
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
