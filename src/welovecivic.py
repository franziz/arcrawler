from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "welovecivic"
	CRAWLER_NAME = "Welovecivic Crawler"
	LINK_TO_CRAWL = [
		"http://www.welovecivic.com/forum/index.php?board=1.0",
		"http://www.welovecivic.com/forum/index.php?board=30.0",
		"http://www.welovecivic.com/forum/index.php?board=10.0",
		"http://www.welovecivic.com/forum/index.php?board=48.0",
		"http://www.welovecivic.com/forum/index.php?board=49.0",
		"http://www.welovecivic.com/forum/index.php?board=50.0",
		"http://www.welovecivic.com/forum/index.php?board=51.0",
		"http://www.welovecivic.com/forum/index.php?board=52.0",
		"http://www.welovecivic.com/forum/index.php?board=53.0",
		"http://www.welovecivic.com/forum/index.php?board=2.0",
		"http://www.welovecivic.com/forum/index.php?board=3.0",
		"http://www.welovecivic.com/forum/index.php?board=5.0",
		"http://www.welovecivic.com/forum/index.php?board=4.0",
		"http://www.welovecivic.com/forum/index.php?board=57.0",
		"http://www.welovecivic.com/forum/index.php?board=54.0",
		"http://www.welovecivic.com/forum/index.php?board=58.0",
		"http://www.welovecivic.com/forum/index.php?board=8.0",
		"http://www.welovecivic.com/forum/index.php?board=7.0",
		"http://www.welovecivic.com/forum/index.php?board=6.0",
		"http://www.welovecivic.com/forum/index.php?board=9.0",
		"http://www.welovecivic.com/forum/index.php?board=39.0",
		"http://www.welovecivic.com/forum/index.php?board=43.0",
		"http://www.welovecivic.com/forum/index.php?board=34.0"
    ]
	COUNTRY = "THA"
	THREAD_XPATH ="//td[re:test(@class,'windowbg*') and @valign='middle' and @width='42%']"
	THREAD_LINK_XPATH = "./a/@href"
	LAST_PAGE_XPATH = "//td[@class='catbg']//a[@class='navPages'][last()]//@href"
	PREV_XPATH = "//td[@class='catbg']//td[1]//b[not(contains(text(),' ... '))][last()]//preceding-sibling::a[@class='navPages'][1]/@href"
	POST_XPATH = "//form[@id='quickModForm']//td[re:test(@class,'windowbg*')]"
	FIELDS = [
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath": "concat(.//div[re:test(@id,'subject*')]/following-sibling::span/text()[2],.//div[re:test(@id,'subject*')]/following-sibling::span/text()[3])"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"normalize-space(.//td[@rowspan='2']/b/a//text())"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='post']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//div[re:test(@id,'subject_*')]/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"normalize-space(substring-before(substring-after(//tr[@class='titlebg']//td[@id='top_subject']//text(),':'),'('))"
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
