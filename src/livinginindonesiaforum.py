from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "livinginindonesiaforum"
	CRAWLER_NAME = "Livinginindonesiaforum Crawler"
	LINK_TO_CRAWL = [
		"http://www.livinginindonesiaforum.org/forum/family-corner/family-life-in-indonesia",
		"http://www.livinginindonesiaforum.org/forum/family-corner/education",
		"http://www.livinginindonesiaforum.org/forum/family-corner/expat-indonesian-marriages",
		"http://www.livinginindonesiaforum.org/forum/general/expat-chat",
		"http://www.livinginindonesiaforum.org/forum/general/noobie-s-nook",
		"http://www.livinginindonesiaforum.org/forum/general/general-advice",
		"http://www.livinginindonesiaforum.org/forum/general/health-medical-and-healthy-living",
		"http://www.livinginindonesiaforum.org/forum/general/laws-visas-money-matters-and-documents",
		"http://www.livinginindonesiaforum.org/forum/general/where-to-find",
		"http://www.livinginindonesiaforum.org/forum/general/politics-current-events",
		"http://www.livinginindonesiaforum.org/forum/general/teachers-chat",
		"http://www.livinginindonesiaforum.org/forum/general/pets-and-animals",
		"http://www.livinginindonesiaforum.org/forum/general/community-events",
		"http://www.livinginindonesiaforum.org/forum/general/living-outside-of-jakarta",
		"http://www.livinginindonesiaforum.org/forum/general/telecommunications-and-related-technology",
		"http://www.livinginindonesiaforum.org/forum/general/ladies-chat",
		"http://www.livinginindonesiaforum.org/forum/general/learning-bahasa-indonesia",
		"http://www.livinginindonesiaforum.org/forum/general/people-search",
		"http://www.livinginindonesiaforum.org/forum/general/forum-life",
		"http://www.livinginindonesiaforum.org/forum/general/personals",
		"http://www.livinginindonesiaforum.org/forum/lifestyle/dining-out-food-drink",
		"http://www.livinginindonesiaforum.org/forum/lifestyle/travel",
		"http://www.livinginindonesiaforum.org/forum/lifestyle/music-theater-art-culture",
		"http://www.livinginindonesiaforum.org/forum/lifestyle/hobbies",
		"http://www.livinginindonesiaforum.org/forum/lifestyle/sports-and-fitness",
		"http://www.livinginindonesiaforum.org/forum/housing/home-search",
		"http://www.livinginindonesiaforum.org/forum/housing/housing-listings",
		"http://www.livinginindonesiaforum.org/forum/housing/household-staff",
		"http://www.livinginindonesiaforum.org/forum/cyber-garage-sale/electronics",
		"http://www.livinginindonesiaforum.org/forum/cyber-garage-sale/household-furnishings-appliances",
		"http://www.livinginindonesiaforum.org/forum/cyber-garage-sale/cars-other-vehicles",
		"http://www.livinginindonesiaforum.org/forum/cyber-garage-sale/miscellaneous",
		"http://www.livinginindonesiaforum.org/forum/cyber-garage-sale/free-stuff",
		"http://www.livinginindonesiaforum.org/forum/job-seekers/available-job-listings",
		"http://www.livinginindonesiaforum.org/forum/job-seekers/expats-seeking-employment",
		"http://www.livinginindonesiaforum.org/forum/job-seekers/indonesians-seeking-employment",
		"http://www.livinginindonesiaforum.org/forum/job-seekers/available-jobs-for-indonesians",
		"http://www.livinginindonesiaforum.org/forum/job-seekers/business-opportunities"
	]      
	COUNTRY = "IDN"
	THREAD_XPATH = "//tbody[@class='topic-list ']//a[@class='topic-title js-topic-title']"
	THREAD_LINK_XPATH = "./@href"
	LAST_PAGE_XPATH = "(//div[@class='js-pagenav pagenav h-right']/a)[last()]/preceding-sibling::a[1]/@href"
	PREV_XPATH = "//div[@class='js-pagenav pagenav h-right']/a[@class='js-pagenav-button js-pagenav-prev-button b-button b-button--secondary']/@href"
	POST_XPATH = "//div[@class='l-row l-row__fixed--left']"
	FIELDS = [
		{"published_date": {
			"single": True, 
			"data_type": "date", 
			"concat": False, 
			"xpath": ".//time[@itemprop='dateCreated']/@datetime"
		}},
		{"permalink": {
			"single": True, 
			"data_type": "url", 
			"concat": False, 
			"xpath": ".//a[@class='b-post__count']/@href"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//div[@class='b-userinfo__details']//a/@href"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@itemprop='text']//text()"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@id='widget_19']//h1/text()"
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
