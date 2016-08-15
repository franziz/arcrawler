from lib.forum_engine  import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS     = NetworkTools(use_proxy=False)
	TEMPLATE          = "crawler.arct"
	TEST_TEMPLATE     = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME    = "tsikot"
	CRAWLER_NAME      = "Tsikot Crawler"
	LINK_TO_CRAWL     = [
		"https://www.tsikot.com/forums/audi-cars-talk-132/",
		"https://www.tsikot.com/forums/bmw-cars-talk-125/",
		"https://www.tsikot.com/forums/cadillac-cars-talk-201/",
		"https://www.tsikot.com/forums/chery-cars-talk-202/",
		"https://www.tsikot.com/forums/chevrolet-cars-talk-128/",
		"https://www.tsikot.com/forums/chrysler-cars-talk-187/",
		"https://www.tsikot.com/forums/daewoo-cars-talk-204/",
		"https://www.tsikot.com/forums/daihatsu-cars-talk-192/",
		"https://www.tsikot.com/forums/dodge-cars-talk-188/",
		"https://www.tsikot.com/forums/ferrari-cars-talk-198/",
		"https://www.tsikot.com/forums/fiat-cars-talk-196/",
		"https://www.tsikot.com/forums/ford-cars-talk-78/",
		"https://www.tsikot.com/forums/foton-cars-talk-205/",
		"https://www.tsikot.com/forums/honda-cars-talk-81/",
		"https://www.tsikot.com/forums/hummer-cars-talk-190/",
		"https://www.tsikot.com/forums/hyundai-cars-talk-83/",
		"https://www.tsikot.com/forums/isuzu-cars-talk-79/",
		"https://www.tsikot.com/forums/jaguar-cars-talk-194/",
		"https://www.tsikot.com/forums/jeep-cars-talk-189/",
		"https://www.tsikot.com/forums/kia-cars-talk-129/",
		"https://www.tsikot.com/forums/land-rover-cars-talk-193/",
		"https://www.tsikot.com/forums/lexus-cars-talk-191/",
		"https://www.tsikot.com/forums/mazda-cars-talk-75/",
		"https://www.tsikot.com/forums/mercedes-benz-cars-talk-126/",
		"https://www.tsikot.com/forums/mini-cars-talk-199/",
		"https://www.tsikot.com/forums/mitsubishi-cars-talk-94/",
		"https://www.tsikot.com/forums/nissan-cars-talk-76/",
		"https://www.tsikot.com/forums/opel-cars-talk-200/",
		"https://www.tsikot.com/forums/peugeot-cars-talk-195/",
		"https://www.tsikot.com/forums/porsche-cars-talk-133/",
		"https://www.tsikot.com/forums/ssangyong-cars-talk-203/",
		"https://www.tsikot.com/forums/subaru-cars-talk-124/",
		"https://www.tsikot.com/forums/suzuki-cars-talk-82/",
		"https://www.tsikot.com/forums/toyota-cars-talk-80/",
		"https://www.tsikot.com/forums/volkswagen-cars-talk-197/",
		"https://www.tsikot.com/forums/volvo-cars-talk-127/",
		"https://www.tsikot.com/forums/philippine-cars-talk-169/",
		"https://www.tsikot.com/forums/chinese-cars-talk-130/",
		"https://www.tsikot.com/forums/other-american-cars-talk-97/",
		"https://www.tsikot.com/forums/other-european-cars-talk-77/",
		"https://www.tsikot.com/forums/other-japanese-cars-talk-98/",
		"https://www.tsikot.com/forums/other-car-brands-talk-131/",
		"https://www.tsikot.com/forums/car-comparisons-72/",
		"https://www.tsikot.com/forums/car-buying-talk-138/",
		"https://www.tsikot.com/forums/car-insurance-financing-auto-loans-talk-134/",
		"https://www.tsikot.com/forums/traffic-laws-infrastructure-parking-135/",
		"https://www.tsikot.com/forums/car-economy-fuel-talk-136/",
		"https://www.tsikot.com/forums/maps-navigation-directions-137/",
		"https://www.tsikot.com/forums/concept-classic-cars-talk-139/",
		"https://www.tsikot.com/forums/garage-150/",
		"https://www.tsikot.com/forums/workshop-8/",
		"https://www.tsikot.com/forums/engine-fuel-system-talk-140/",
		"https://www.tsikot.com/forums/transmission-talk-141/",
		"https://www.tsikot.com/forums/electricals-gauges-wiring-talk-142/",
		"https://www.tsikot.com/forums/aircon-temperature-talk-143/",
		"https://www.tsikot.com/forums/suspension-steering-brakes-talk-144/",
		"https://www.tsikot.com/forums/other-troubles-149/",
		"https://www.tsikot.com/forums/tech-specs-quick-reference-56/",
		"https://www.tsikot.com/forums/car-navigation-positioning-systems-156/",
		"https://www.tsikot.com/forums/car-audio-video-systems-153/",
		"https://www.tsikot.com/forums/car-security-safety-systems-154/",
		"https://www.tsikot.com/forums/more-than-looks-9/",
		"https://www.tsikot.com/forums/window-treatment-160/",
		"https://www.tsikot.com/forums/auto-painting-detailingtalk-157/",
		"https://www.tsikot.com/forums/interior-detailing-talk-158/",
		"https://www.tsikot.com/forums/car-lights-lamps-talk-155/",
		"https://www.tsikot.com/forums/mags-rims-wheels-159/",
		"https://www.tsikot.com/forums/thumbs-up-headquarters-101/",
		"https://www.tsikot.com/forums/goon-squad-hq-19/",
		"https://www.tsikot.com/forums/racing-off-roading-fun-run-talk-16/",
	]
	COUNTRY           = "PHL"
	THREAD_XPATH      = "//ol//li[re:test(@id,'thread*')]"
	THREAD_LINK_XPATH = ".//a[@class='title']/@href"
	LAST_PAGE_XPATH   = "//span[@class='first_last']/a/@href"
	PREV_XPATH        = "//a[@rel='prev']/@href"
	POST_XPATH        = "//ol//li[re:test(@class,'postbit*')]"
	FIELDS            = [
		{"published_date": {
			"single": True, 
			"data_type": "date", 
			"concat": True, 
			"xpath": ".//span[@class='date']//text()"
		}},
		{"permalink": {
			"single": True, 
			"data_type": "url", 
			"concat": False, 
			"xpath": ".//div[@class='postbody']//span[@class='nodecontrols']/a/@href"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":".//a[re:test(@class,'username*')]//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='content']//text()"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//span[@class='threadtitle']//text()"
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