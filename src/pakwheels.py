from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "pakwheels"
	CRAWLER_NAME = "Pakwheels Crawler"
	LINK_TO_CRAWL = [
       "http://www.pakwheels.com/forums/corolla/",
        "http://www.pakwheels.com/forums/vitz-yaris/",
        "http://www.pakwheels.com/forums/prius/",
        "http://www.pakwheels.com/forums/passo/",
        "http://www.pakwheels.com/forums/belta-platz-vios/",
        "http://www.pakwheels.com/forums/other-toyota-models/",
        "http://www.pakwheels.com/forums/civic/",
        "http://www.pakwheels.com/forums/city/",
        "http://www.pakwheels.com/forums/vezel/",        
        "http://www.pakwheels.com/forums/other-honda-models/",        
        "http://www.pakwheels.com/forums/cultus/",
        "http://www.pakwheels.com/forums/swift/",
        "http://www.pakwheels.com/forums/wagon-r/",
        "http://www.pakwheels.com/forums/liana/",
        "http://www.pakwheels.com/forums/alto/",
        "http://www.pakwheels.com/forums/margalla/",
        "http://www.pakwheels.com/forums/khyber/",
        "http://www.pakwheels.com/forums/baleno/",
        "http://www.pakwheels.com/forums/other-suzuki-models/",
        "http://www.pakwheels.com/forums/cuore-mira/",
        "http://www.pakwheels.com/forums/charade/",
        "http://www.pakwheels.com/forums/other-daihatsu-models/",
        "http://www.pakwheels.com/forums/mitsubishi/",
        "http://www.pakwheels.com/forums/volkswagen/",
        "http://www.pakwheels.com/forums/nissan-datsun/",        
        "http://www.pakwheels.com/forums/faw/",
        "http://www.pakwheels.com/forums/member-opinions-suggestions/",
        "http://www.pakwheels.com/forums/fraud-theft-alerts/",
        "http://www.pakwheels.com/forums/suzuki-bikes/",
        "http://www.pakwheels.com/forums/yamaha-bikes/",
        "http://www.pakwheels.com/forums/other-bike-makers/",
        "http://www.pakwheels.com/forums/general-motorcycle-discussion/",
        "http://www.pakwheels.com/forums/motorcycle-travel-diaries/",
        "http://www.pakwheels.com/forums/general-4x4-discussion/",
        "http://www.pakwheels.com/forums/mechanical-electrical/",
        "http://www.pakwheels.com/forums/body-work-appearance/",
        "http://www.pakwheels.com/forums/car-entertainment-ice/",
        "http://www.pakwheels.com/forums/d-i-y-projects/",
        "http://www.pakwheels.com/forums/news-articles-motorists-education/",
        "http://www.pakwheels.com/forums/exotics-classics/",
        "http://www.pakwheels.com/forums/vehicle-documentation-registration-import-lease/",
        "http://www.pakwheels.com/forums/site-feedback-suggestions/",
        "http://www.pakwheels.com/forums/members-member-rides/",
        "http://www.pakwheels.com/forums/get-togethers-motor-shows-motor-sports/",
        "http://www.pakwheels.com/forums/spotting-hobbies-other-stuff/",
        "http://www.pakwheels.com/forums/aircrafts-trains/",
        "http://www.pakwheels.com/forums/wheels-photography-videos/",
        "http://www.pakwheels.com/forums/buy-sell-exchange/",
        "http://www.pakwheels.com/forums/cars/",        
        "http://www.pakwheels.com/forums/engine-drivetrain-performance-parts/",
        "http://www.pakwheels.com/forums/wheels-tyres-suspension-parts/",
        "http://www.pakwheels.com/forums/interior-exterior-appearance-parts/",
        "http://www.pakwheels.com/forums/car-audio-video-electronics/",
        "http://www.pakwheels.com/forums/car-care-car-detailing-items/",
        "http://www.pakwheels.com/forums/oils-fluids-maintenance-items/",
        "http://www.pakwheels.com/forums/misc-items/",
        "http://www.pakwheels.com/forums/motorcycles-motorcycle-parts/",
        "http://www.pakwheels.com/forums/4x4s-4x4-parts/",
        "http://www.pakwheels.com/forums/non-auto-related-stuff/",
        "http://www.pakwheels.com/forums/non-wheels-discussions/",
        "http://www.pakwheels.com/forums/general-lounge/",
        "http://www.pakwheels.com/forums/career-education/",
        "http://www.pakwheels.com/forums/technology/",
        "http://www.pakwheels.com/forums/photography/",
        "http://www.pakwheels.com/forums/real-estate/",
        "http://www.pakwheels.com/forums/public-service-announcements/"
	]
	COUNTRY = "PAK"
	THREAD_XPATH = "//ol//li[re:test(@id,'thread*')]"
	THREAD_LINK_XPATH = ".//a[@class='title']/@href"
	LAST_PAGE_XPATH = "//span[@class='first_last']/a/@href"
	PREV_XPATH = "//span[@class='prev_next']/a[@rel='prev']/@href"
	POST_XPATH = "//ol//li[re:test(@id,'post*')]"
	FIELDS = [
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath": "concat(substring-before(substring-after(substring-after(concat(.//span[@class='date']/text(),' ', .//span[@class='time']/text()),'-'),'-'),' '),'/',substring-before(substring-after(concat(.//span[@class='date']/text(),' ', .//span[@class='time']/text()),'-'),'-'),'/',substring-before(substring-after(concat(.//span[@class='date']/text(),' ', .//span[@class='time']/text()),'-'),'-'),' ',substring-after(substring-after(substring-after(concat(.//span[@class='date']/text(),' ', .//span[@class='time']/text()),'-'),'-'),' '))"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//div[@class='posthead']//span[@class='nodecontrols']/a[@class='postcounter']/@href"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"normalize-space(.//a[re:test(@class,'username*')]//strong/text())"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='content']//div[re:test(@id,'post_*')]//text()"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":"//div[@class='pagetitle']//span[@class='threadtitle']//text()"
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
