from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "livingincebuforums"
	CRAWLER_NAME = "livingincebuforums crawler"
	LINK_TO_CRAWL = [
		"http://www.livingincebuforums.com/ipb/forum/237-rules-guidelines-all-advert-rates/",
		"http://www.livingincebuforums.com/ipb/forum/24-news-headlines-world-events/",
		"http://www.livingincebuforums.com/ipb/forum/174-philippines-weather-typhoons-earthquakes-other-natural-disasters/",
		"http://www.livingincebuforums.com/ipb/forum/205-storm-damage-assistance-contact-threads/",
		"http://www.livingincebuforums.com/ipb/forum/5-announcements-current-events/",
		"http://www.livingincebuforums.com/ipb/forum/19-businesses-products-services/",
		"http://www.livingincebuforums.com/ipb/forum/38-cebu-classified-advertisements/",
		"http://www.livingincebuforums.com/ipb/forum/6-general-advice/",
		"http://www.livingincebuforums.com/ipb/forum/14-living-in-cebu/",
		"http://www.livingincebuforums.com/ipb/forum/102-insurance-health-medical-life-home-auto-etc/",
		"http://www.livingincebuforums.com/ipb/forum/31-shipping-anything-to-from-and-within-the-philippines/",
		"http://www.livingincebuforums.com/ipb/forum/168-social-security-super-disability-age-pension-etc/",
		"http://www.livingincebuforums.com/ipb/forum/35-spoken-languages-english-cebuano-etc/",
		"http://www.livingincebuforums.com/ipb/forum/13-banking-and-foreign-exchange/",
		"http://www.livingincebuforums.com/ipb/forum/193-money-talk-investing-discussions/",
		"http://www.livingincebuforums.com/ipb/forum/21-sending-money-to-within-the-philippines/",
		"http://www.livingincebuforums.com/ipb/forum/175-boat-construction/",
		"http://www.livingincebuforums.com/ipb/forum/12-boating-swimming-diving-fishing-in-the-philippines/",
		"http://www.livingincebuforums.com/ipb/forum/20-buying-building-homes-rental-property-land-etc/",
		"http://www.livingincebuforums.com/ipb/forum/224-construction-threads-home-rest-house-etc/",
		"http://www.livingincebuforums.com/ipb/forum/26-living-in-the-philippines/",
		"http://www.livingincebuforums.com/ipb/forum/110-hobbies-other-interests/",
		"http://www.livingincebuforums.com/ipb/forum/61-military-active-reserve-disabled-or-retired-veterans/",		
		"http://www.livingincebuforums.com/ipb/forum/68-sports-game-events/",
		"http://www.livingincebuforums.com/ipb/forum/7-vehicles-driving-licensing-information/",
		"http://www.livingincebuforums.com/ipb/forum/108-general-items/",
		"http://www.livingincebuforums.com/ipb/forum/189-services/",
		"http://www.livingincebuforums.com/ipb/forum/64-drinks-mixes-recipes-local-suppliers/",
		"http://www.livingincebuforums.com/ipb/forum/65-food-grocery-shopping-restaurants/",
		"http://www.livingincebuforums.com/ipb/forum/57-recipes-food-dishes/",
		"http://www.livingincebuforums.com/ipb/forum/50-health-medical-dental-fitness-diet/",
		"http://www.livingincebuforums.com/ipb/forum/28-philippines-safe-not-safe/",
		"http://www.livingincebuforums.com/ipb/forum/170-warnings-dangers-in-the-philippines/",
		"http://www.livingincebuforums.com/ipb/forum/67-embassy-news/",
		"http://www.livingincebuforums.com/ipb/forum/30-passports-visas-permits-immigration/",
		"http://www.livingincebuforums.com/ipb/forum/230-passports-visas-permits-immigration-important-threads/",
		"http://www.livingincebuforums.com/ipb/forum/111-traveling-aboard-ships-boats-in-the-philippines/",
		"http://www.livingincebuforums.com/ipb/forum/52-trip-information-airline-hotel-resort-restaurant-travel-reviews/",
		"http://www.livingincebuforums.com/ipb/forum/83-trip-information-airports-airlines-reservations-ticketing/",
		"http://www.livingincebuforums.com/ipb/forum/29-trip-information-where-should-we-stay-what-should-we-do/",
		"http://www.livingincebuforums.com/ipb/forum/180-schools-and-educating-children-in-the-philippines/",
		"http://www.livingincebuforums.com/ipb/forum/181-children-medical-issues-in-the-philippines/",
		"http://www.livingincebuforums.com/ipb/forum/182-children-adjusting-to-life-in-the-philippines/",
		"http://www.livingincebuforums.com/ipb/forum/183-warnings-dangers-for-kids-in-the-philippines/",
		"http://www.livingincebuforums.com/ipb/forum/241-outlaw-forums-announcements/",	
		"http://www.livingincebuforums.com/ipb/forum/200-religion-other-debated-topics/",
		"http://www.livingincebuforums.com/ipb/forum/229-outlaw-off-topic/",
		"http://www.livingincebuforums.com/ipb/forum/58-birth-control-contraceptives/",
		"http://www.livingincebuforums.com/ipb/forum/33-filipino-culture/",
		"http://www.livingincebuforums.com/ipb/forum/36-filipino-mannerisms-logic/",
		"http://www.livingincebuforums.com/ipb/forum/39-filipino-speaking-forum/",
		"http://www.livingincebuforums.com/ipb/forum/34-romance-dating-marriage-family/",
		"http://www.livingincebuforums.com/ipb/forum/47-self-sufficiency/",
		"http://www.livingincebuforums.com/ipb/forum/106-philippines-energy-mains-solar-hydro-wind-power/",
		"http://www.livingincebuforums.com/ipb/forum/85-farming-gardening/",
		"http://www.livingincebuforums.com/ipb/forum/204-miscellaneous-green-topics/",
		"http://www.livingincebuforums.com/ipb/forum/92-philippines-charity-information/",
		"http://www.livingincebuforums.com/ipb/forum/97-expats-ladies-charities/",
		"http://www.livingincebuforums.com/ipb/forum/115-iro-island-rescue-organization/",
		"http://www.livingincebuforums.com/ipb/forum/96-sos-philippines/",
		"http://www.livingincebuforums.com/ipb/forum/18-computers-software-electronics/",
		"http://www.livingincebuforums.com/ipb/forum/99-technical-computer-repair/",
		"http://www.livingincebuforums.com/ipb/forum/25-texting-calling-cell-phones/",
		"http://www.livingincebuforums.com/ipb/forum/77-german-speaking-forum/",
		"http://www.livingincebuforums.com/ipb/forum/76-nordic-languages-forum/",
		"http://www.livingincebuforums.com/ipb/forum/228-barter-trade-forum/",
		"http://www.livingincebuforums.com/ipb/forum/235-the-cellar/",
		"http://www.livingincebuforums.com/ipb/forum/91-dirty-kitchen/",
		"http://www.livingincebuforums.com/ipb/forum/40-jokes-humor/",
		"http://www.livingincebuforums.com/ipb/forum/66-outside-the-philippines/",
		"http://www.livingincebuforums.com/ipb/forum/231-pauls-forum/",
		"http://www.livingincebuforums.com/ipb/forum/90-videos-to-share/",
		"http://www.livingincebuforums.com/ipb/forum/225-announcements-current-events/",
		"http://www.livingincebuforums.com/ipb/forum/218-banking-and-foreign-exchange/",
		"http://www.livingincebuforums.com/ipb/forum/213-businesses-products-services/",
		"http://www.livingincebuforums.com/ipb/forum/219-buying-building-homes-rental-property-land-etc/",
		"http://www.livingincebuforums.com/ipb/forum/227-computers-software-electronics/",
		"http://www.livingincebuforums.com/ipb/forum/221-filipino-culture/",
		"http://www.livingincebuforums.com/ipb/forum/222-food-grocery-shopping-restaurants/",
		"http://www.livingincebuforums.com/ipb/forum/214-general-advice/",
		"http://www.livingincebuforums.com/ipb/forum/216-hello-introduction-forum/",
		"http://www.livingincebuforums.com/ipb/forum/215-living-in-cebu/",
		"http://www.livingincebuforums.com/ipb/forum/212-news-headlines-world-events/",
		"http://www.livingincebuforums.com/ipb/forum/210-off-topic-archive/",
		"http://www.livingincebuforums.com/ipb/forum/217-passports-visas-permits-immigration-information/",
		"http://www.livingincebuforums.com/ipb/forum/220-romance-dating-marriage-family/",
		"http://www.livingincebuforums.com/ipb/forum/226-sports-game-events/",
		"http://www.livingincebuforums.com/ipb/forum/223-vehicles-driving-licensing-information/",
		"http://www.livingincebuforums.com/ipb/forum/123-archives-the-living-in-cebu-forums/",
		"http://www.livingincebuforums.com/ipb/forum/140-archives-board-announcements-information/",
		"http://www.livingincebuforums.com/ipb/forum/121-archives-cebu-specific-information/",
		"http://www.livingincebuforums.com/ipb/forum/162-archives-sos-philippines/",
		"http://www.livingincebuforums.com/ipb/forum/129-archives-living-in-cebu/",
		"http://www.livingincebuforums.com/ipb/forum/137-archives-announcements-current-events/",
		"http://www.livingincebuforums.com/ipb/forum/151-archives-general-advice/",
		"http://www.livingincebuforums.com/ipb/forum/144-archives-computers-software-electronics/",
		"http://www.livingincebuforums.com/ipb/forum/134-archives-businesses-products-services/",
		"http://www.livingincebuforums.com/ipb/forum/138-archives-driving-riding-licensing-in-cebu/",
		"http://www.livingincebuforums.com/ipb/forum/122-archives-general-philippines-information",
		"http://www.livingincebuforums.com/ipb/forum/142-archives-boating-diving/",
		"http://www.livingincebuforums.com/ipb/forum/155-archives-banking-investing/",
		"http://www.livingincebuforums.com/ipb/forum/141-archives-building-tips-property-etc/",
		"http://www.livingincebuforums.com/ipb/forum/161-archives-sending-money/",
		"http://www.livingincebuforums.com/ipb/forum/130-archives-cell-phones-texting-calling/",
		"http://www.livingincebuforums.com/ipb/forum/160-archives-other-area-information/",
		"http://www.livingincebuforums.com/ipb/forum/125-archives-tourist-and-visitor-information/",
		"http://www.livingincebuforums.com/ipb/forum/150-archives-philippines-travel-safe-or-not/",
		"http://www.livingincebuforums.com/ipb/forum/146-archives-trip-reports-flights-hotels-pension-houses/",
		"http://www.livingincebuforums.com/ipb/forum/148-archives-visa-information-philippines-and-elsewhere/",
		"http://www.livingincebuforums.com/ipb/forum/149-archives-links-to-picture-movie-sites/",
		"http://www.livingincebuforums.com/ipb/forum/147-archives-shipping-to-from-and-within-the-philippines/",
		"http://www.livingincebuforums.com/ipb/forum/136-archives-weddings-filing-requirements/",
		"http://www.livingincebuforums.com/ipb/forum/126-archives-filipino-culture/",
		"http://www.livingincebuforums.com/ipb/forum/157-archives-philippines-romance-101/",
		"http://www.livingincebuforums.com/ipb/forum/133-archives-food-mannerisms-logic/",
		"http://www.livingincebuforums.com/ipb/forum/131-archives-philippines-languages/",
		"http://www.livingincebuforums.com/ipb/forum/124-archives-off-topic-etc/",
		"http://www.livingincebuforums.com/ipb/forum/164-archives-news-section/",
		"http://www.livingincebuforums.com/ipb/forum/143-archives-for-sale-wanted/",
		"http://www.livingincebuforums.com/ipb/forum/132-archives-off-topic-forum/",
		"http://www.livingincebuforums.com/ipb/forum/152-archives-pointman-cebu-comments/",
		"http://www.livingincebuforums.com/ipb/forum/153-archives-weather/",
		"http://www.livingincebuforums.com/ipb/forum/139-archives-links-polls-only/",
		"http://www.livingincebuforums.com/ipb/forum/156-archives-jokes-humor/",
		
        ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//div[@class='ipsBox']//tr[re:test(@id,'trow_*')]"
	THREAD_LINK_XPATH = ".//a[@itemprop='url']/@href"
	LAST_PAGE_XPATH = "(//div[@class='pagination clearfix left ']//a[not(contains(text(),'Next'))])[last()]/@href"
	PREV_XPATH = "//ul[@class='ipsList_inline left pages']//li[@class='page active']/preceding-sibling::li[1]/a/@href"
	POST_XPATH = "//div[re:test(@id,'post_id_*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": True,
			"xpath":".//abbr[@itemprop='commentTime']/text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": "concat(.//span[@class='author vcard']/text(),.//div[@class='author_info']/preceding-sibling::h3/text()[last()])"
		}},
		{"content":{
			"single":False,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='post entry-content ']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//a[@itemprop='replyToUrl']/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"(//div[@id='secondary_navigation']//li)[last()]/a//text()"
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
