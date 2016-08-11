from lib.forum_engine  import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS     = NetworkTools(use_proxy=False) 
	TEMPLATE          = "crawler.arct"
	TEST_TEMPLATE     = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME    = "detik"
	CRAWLER_NAME      = "Detik Forum Crawler"
	LINK_TO_CRAWL     = [
							"http://forum.detik.com/mobil-f80.html",
							"http://forum.detik.com/politik-f49.html",
							"http://forum.detik.com/tokoh-f137.html",
							"http://forum.detik.com/partai-politik-f138.html",
							"http://forum.detik.com/sosial-budaya-f52.html",
							"http://forum.detik.com/internasional-f134.html",
							"http://forum.detik.com/militer-f151.html",
							"http://forum.detik.com/berita-daerah-f210.html",
							"http://forum.detik.com/selebriti-f15.html",
							"http://forum.detik.com/intl-celebrity-f190.html",
							"http://forum.detik.com/musik-f12.html",
							"http://forum.detik.com/pageant-f261.html",
							"http://forum.detik.com/film-f13.html",
							"http://forum.detik.com/seni-budaya-f205.html",
							"http://forum.detik.com/k-corner-f213.html",
							"http://forum.detik.com/k-pop-f214.html",
							"http://forum.detik.com/k-drama-f215.html",
							"http://forum.detik.com/j-corner-f36.html",
							"http://forum.detik.com/manga-f37.html",
							"http://forum.detik.com/anime-tokusatsu-f38.html",
							"http://forum.detik.com/bunka-f44.html",
							"http://forum.detik.com/sepakbola-f17.html",
							"http://forum.detik.com/liga-italia-f100.html",
							"http://forum.detik.com/liga-inggris-f99.html",
							"http://forum.detik.com/liga-spanyol-f101.html",
							"http://forum.detik.com/liga-indonesia-f102.html",
							"http://forum.detik.com/liga-dunia-f103.html",
							"http://forum.detik.com/liga-champions-f104.html",
							"http://forum.detik.com/fans-club-f105.html",
							"http://forum.detik.com/pssi-dan-timnas-indonesia-f106.html",
							"http://forum.detik.com/detikers-league-f209.html",
							"http://forum.detik.com/formula-1-f18.html",
							"http://forum.detik.com/moto-gp-f19.html",
							"http://forum.detik.com/olahraga-lain-f20.html",
							"http://forum.detik.com/futsal-f181.html",
							"http://forum.detik.com/diskusi-it-f69.html",
							"http://forum.detik.com/curhat-pelanggan-it-f77.html",
							"http://forum.detik.com/berita-ekonomi-f91.html",
							"http://forum.detik.com/perbankan-f160.html",
							"http://forum.detik.com/asuransi-f161.html",
							"http://forum.detik.com/entrepreneur-f96.html",
							"http://forum.detik.com/peluang-usaha-f92.html",
							"http://forum.detik.com/bursa-saham-f90.html",
							"http://forum.detik.com/belajar-saham-f141.html",
							"http://forum.detik.com/friends-relationship-f88.html",
							"http://forum.detik.com/fashion-f28.html",
							"http://forum.detik.com/family-f173.html",
							"http://forum.detik.com/psikologi-f182.html",
							"http://forum.detik.com/hidup-sehat-f30.html",
							"http://forum.detik.com/cerita-kita-f259.html",
							"http://forum.detik.com/food-f33.html",
							"http://forum.detik.com/traveling-f149.html",
							"http://forum.detik.com/hobi-lainnya-f154.html",
							"http://forum.detik.com/games-f58.html",
							"http://forum.detik.com/tanaman-hias-f94.html",
							"http://forum.detik.com/sepeda-f121.html"
						]
	COUNTRY           = "IDN"
	THREAD_XPATH      = "//tbody[re:test(@id,'threadbits_forum_*')]/tr"
	THREAD_LINK_XPATH = ".//a[re:test(@id,'thread_title_*')]/@href"
	LAST_PAGE_XPATH   = "//a[re:test(@title,'Last Page*')]/@href"
	PREV_XPATH        = "//a[@rel='prev']/@href"
	POST_XPATH        = "//table[re:test(@id,'post*')]"
	FIELDS            = [
		{"published_date": {
			"single": True, 
			"data_type": "date", 
			"concat": True, 
			"xpath": "./tbody/tr[1]/td[1]/text()"
		}},
		{"permalink": {
			"single": True, 
			"data_type": "url", 
			"concat": False, 
			"xpath": ".//a[re:test(@id,'postcount*')]/@href"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":".//a[@class='bigusername']/text()"
		}},
		# {"author_id":{
		# 	"single":True,
		# 	"data_type": "string",
		# 	"concat":False,
		# 	"xpath":".//div[@class='user-name']/@data-userid"
		# }},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[re:test(@id,'post_message_*')]//text()"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//td[@class='navbar']/strong/text()"
		}}
	]
	CONDITIONS = {
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