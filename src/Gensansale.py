from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "Gensansale"
	CRAWLER_NAME = "Gensansale Crawler"
	LINK_TO_CRAWL = [
		"http://www.gensansale.com/forums/100-libre-items.77/",		
		"http://www.gensansale.com/forums/automotive.6/",
		"http://www.gensansale.com/forums/wheels-discussions-to-car-motorcycle-bikes-rc.57/",
		"http://www.gensansale.com/forums/motorcycle.19/",
		"http://www.gensansale.com/forums/baby-infant-kids-section.75/",
		"http://www.gensansale.com/forums/barter-trade-swap.22/",
		"http://www.gensansale.com/forums/bikes-hobbies-sports-toys-gaming-consoles.13/",
		"http://www.gensansale.com/forums/books-magazines.7/",
		"http://www.gensansale.com/forums/cameras-and-mp3-mp4-player.8/",
		"http://www.gensansale.com/forums/cell-phones-tablet-devices.10/",
		"http://www.gensansale.com/forums/clothing-shoes-personal-accessories.11/",
		"http://www.gensansale.com/forums/computers-accessories.9/",
		"http://www.gensansale.com/forums/electronics-appliances-instruments.12/",
		"http://www.gensansale.com/forums/food-beverage.76/",
		"http://www.gensansale.com/forums/health-beauty.14/",
		"http://www.gensansale.com/forums/homeware-garden-plants.78/",
		"http://www.gensansale.com/forums/pets-and-animals.18/",
		"http://www.gensansale.com/forums/real-estate-apartments.17/",
		"http://www.gensansale.com/forums/machinery-tools.69/",
		"http://www.gensansale.com/forums/misc-other-items.15/",
		"http://www.gensansale.com/forums/services.16/",
		"http://www.gensansale.com/forums/jobs-work.21/",
		"http://www.gensansale.com/forums/lost-found.65/",
		"http://www.gensansale.com/forums/general-discussions.20/",
		"http://www.gensansale.com/forums/tech-talk.56/",
		"http://www.gensansale.com/forums/wheels-discussions-to-car-motorcycle-bikes-rc.57/",
		"http://www.gensansale.com/forums/current-events.51/",
		"http://www.gensansale.com/forums/entertainment-movie-discussions.71/"
		"http://www.gensansale.com/forums/gensan-youtubers.63/"
		"http://www.gensansale.com/forums/humor.52/,"		
		"http://www.gensansale.com/forums/cbr150-club.44/",
		"http://www.gensansale.com/forums/dj-club.29/",
		"http://www.gensansale.com/forums/fish-club.70/",
		"http://www.gensansale.com/forums/gensansale-canine-club.33/",
		"http://www.gensansale.com/forums/gensan-rc-owners-racers.42/",
		"http://www.gensansale.com/forums/gensan-mio-club.32/",
		"http://www.gensansale.com/forums/gensan-tuna-modified-xrm-gtmx-club.34/",
		"http://www.gensansale.com/forums/kiwanis-club-of-synergy-gensan.28/",
		"http://www.gensansale.com/forums/moto-club-familia.73/",
		"http://www.gensansale.com/forums/mountaineers-club.27/",
		"http://www.gensansale.com/forums/soccsksargen-rs-club.74/",
		"http://www.gensansale.com/forums/swat-gensan-airsoft-team.30/",
		"http://www.gensansale.com/forums/suzuki-raiders-club.31/",
		"http://www.gensansale.com/forums/toyota-auto-club-gensan.43/"
	]        
	COUNTRY = "PHL"
	THREAD_XPATH = "//li[re:test(@id,'thread-*')]"
	THREAD_LINK_XPATH = ".//h3/a/@href"
	LAST_PAGE_XPATH = "(//div[@class='PageNav']/nav/a)[last()]/preceding-sibling::a[1]/@href"
	PREV_XPATH = "(//div[@class='PageNav']/nav/a[@class='currentPage '])[last()]/preceding-sibling::a[1]/@href"
	POST_XPATH = "//ol//li[re:test(@id,'post-*')]"
	FIELDS = [
		{"published_date": {
			"single": True, 
			"data_type": "date",
			"concat": False, 
			"xpath": "concat(.//a[@class='datePermalink']/span//@title,.//a[@class='datePermalink']/abbr//text())"
		}},
		{"permalink": {
			"single": True, 
			"data_type": "url", 
			"concat": False, 
			"xpath": ".//div[@class='publicControls']/a[@title='Permalink']/@href"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"normalize-space(.//a[re:test(@class,'username')]//text())"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='messageContent']//text()"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"normalize-space(//div[@class='titleBar']//h1//text())"
		}}
	]
	CONDITIONS={
		"has_to_have_content":{
			"condition":'"content" in document',
			"exception":'"content is not defined"'
		},
		"content_cannot_be_empty":{
			"condition":'len(document["content"]) > 0',
			"exception":'"content cannot be empty"'
		}
	}
#end class
