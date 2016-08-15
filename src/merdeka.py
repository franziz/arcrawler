from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "merdeka"
	CRAWLER_NAME = "Merdeka Crawler"
	LINK_TO_CRAWL = [
		"http://forums.merdeka.com/forums/2-Hello-World!",
		"http://forums.merdeka.com/forums/4-Aturan-Main-Saran-amp-Laporan",
		"http://forums.merdeka.com/forums/5-Jual-Beli",
		"http://forums.merdeka.com/forums/55-Lowongan-Pekerjaan",
		"http://forums.merdeka.com/forums/7-Apa-Kata-Dunia",
		"http://forums.merdeka.com/forums/8-Kesehatan",
		"http://forums.merdeka.com/forums/9-Olahraga",
		"http://forums.merdeka.com/forums/10-Teknologi",
		"http://forums.merdeka.com/forums/11-Games",
		"http://forums.merdeka.com/forums/12-Fotografi",
		"http://forums.merdeka.com/forums/13-Humor",
		"http://forums.merdeka.com/forums/14-Ih-Serem",
		"http://forums.merdeka.com/forums/54-Curhat",
		"http://forums.merdeka.com/forums/21-Hot-News",
		"http://forums.merdeka.com/forums/22-Layar-Tancap",
		"http://forums.merdeka.com/forums/23-Music-Corner",
		"http://forums.merdeka.com/forums/53-KapanLagi-Plus",
		"http://forums.merdeka.com/forums/29-Body-amp-Mind",
		"http://forums.merdeka.com/forums/32-Love-amp-Relationship",
		"http://forums.merdeka.com/forums/35-Fashion",
		"http://forums.merdeka.com/forums/37-Kuliner",
		"http://forums.merdeka.com/forums/39-Oto-Lounge",
		"http://forums.merdeka.com/forums/40-Tips-amp-Trick-amp-Perawatan-Mobil",
		"http://forums.merdeka.com/forums/41-Galeri-Modifikasi",
		"http://forums.merdeka.com/forums/42-Jual-Beli-Mobil",
		"http://forums.merdeka.com/forums/44-Internasional",
		"http://forums.merdeka.com/forums/50-Indonesia",
		"http://forums.merdeka.com/forums/51-Ragam",
		"http://forums.merdeka.com/forums/52-Babes"
    ]
	COUNTRY = "IDN"
	THREAD_XPATH = "//a[re:test(@id,'thread_title_*')]"
	THREAD_LINK_XPATH = "./@href"
	LAST_PAGE_XPATH = "//div[@class='pagination_top']//span[@class='first_last']/a/@href"
	PREV_XPATH = "//div[@class='pagination_top']//span[@class='prev_next']/a[@rel='prev']/@href"
	POST_XPATH = "//ol[@id='posts']/li[re:test(@id,'post_*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath": "concat(.//span[@class='date']/text(),.//span[@class='date']/span/text())"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//div[@class='username_container']/div[1]/a[1]//text()"
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
			"xpath": ".//a[@class='postcounter']/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//li[@class='navbit lastnavbit']/span/text()"
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
