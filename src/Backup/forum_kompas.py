from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "kompas"
	CRAWLER_NAME = "Kompas Crawler"
	LINK_TO_CRAWL = [
		"http://forum.kompas.com/forums/2-Informasi-amp-Pengumuman-haha",
		"http://forum.kompas.com/forums/231-Keep-Posting-Point-(KEPO)-KompasForum",
		"http://forum.kompas.com/forums/177-Kuis-Kontes-Polling",
		"http://forum.kompas.com/forums/208-Merah-Putih-Membanggakan",
		"http://forum.kompas.com/forums/225-Surat-Cinta",
		"http://forum.kompas.com/forums/218-Adu-Gombal",
		"http://forum.kompas.com/forums/221-Cerita-Unik-Ramadhan",
		"http://forum.kompas.com/forums/220-Euforia-Euro-2012",
		"http://forum.kompas.com/forums/224-Pantun-Semangat-AFF-2012",
		"http://forum.kompas.com/forums/188-Events-amp-Aktifitas",
		"http://forum.kompas.com/forums/222-KOMPASIANA",
		"http://forum.kompas.com/forums/109-Pertanyaan-amp-Bantuan",
		"http://forum.kompas.com/forums/178-Teras",
		"http://forum.kompas.com/forums/207-Happy-Birthday",
		"http://forum.kompas.com/forums/209-Arcade-World",
		"http://forum.kompas.com/forums/213-KompasTV",
		"http://forum.kompas.com/forums/226-Kompas-Karier",
		"http://forum.kompas.com/forums/214-Ekspedisi-Cincin-Api",
		"http://forum.kompas.com/forums/175-Bentara-Budaya",
		"http://forum.kompas.com/forums/217-HelloFest",
		"http://forum.kompas.com/forums/5-International",
		"http://forum.kompas.com/forums/6-Nasional",
		"http://forum.kompas.com/forums/228-SERBA-SERBI-PEMILU-2014",
		"http://forum.kompas.com/forums/9-Megapolitan",
		"http://forum.kompas.com/forums/223-100-Hari-Jokowi",
		"http://forum.kompas.com/forums/194-Ekonomi-Umum",
		"http://forum.kompas.com/forums/80-Saham-amp-Valas",
		"http://forum.kompas.com/forums/24-Sepakbola",
		"http://forum.kompas.com/forums/227-PIALA-DUNIA-BRAZIL-2014",
		"http://forum.kompas.com/forums/216-EURO-2012",
		"http://forum.kompas.com/forums/92-Bola-Indonesia",
		"http://forum.kompas.com/forums/93-Liga-Inggris",
		"http://forum.kompas.com/forums/94-Liga-Italia",
		"http://forum.kompas.com/forums/95-Liga-Spanyol",
		"http://forum.kompas.com/forums/165-Futsal",
		"http://forum.kompas.com/forums/30-Racing",
		"http://forum.kompas.com/forums/36-Bulu-Tangkis",
		"http://forum.kompas.com/forums/32-Basket",
		"http://forum.kompas.com/forums/38-Lainnya",
		"http://forum.kompas.com/forums/120-Sekolah-amp-Pendidikan",
		"http://forum.kompas.com/forums/234-SNMPTN",
		"http://forum.kompas.com/forums/16-Sains",
		"http://forum.kompas.com/forums/13-Green-amp-Global-Warming",
		"http://forum.kompas.com/forums/10-Kesehatan",
		"http://forum.kompas.com/forums/84-Medis",
		"http://forum.kompas.com/forums/85-Alternatif",
		"http://forum.kompas.com/forums/12-Perempuan",
		"http://forum.kompas.com/forums/89-Tentang-Pria",
		"http://forum.kompas.com/forums/90-Curhat",
		"http://forum.kompas.com/forums/91-Keluarga",
		"http://forum.kompas.com/forums/125-Fashion-amp-Beauty",
		"http://forum.kompas.com/forums/105-Love-Talk",
		"http://forum.kompas.com/forums/124-Food",
		"http://forum.kompas.com/forums/122-Resep",
		"http://forum.kompas.com/forums/17-Travel",
		"http://forum.kompas.com/forums/14-Properti",
		"http://forum.kompas.com/forums/108-Urban-Life",
		"http://forum.kompas.com/forums/117-Gosip",
		"http://forum.kompas.com/forums/22-Musik",
		"http://forum.kompas.com/forums/116-Movies",
		"http://forum.kompas.com/forums/123-Gadget",
		"http://forum.kompas.com/forums/232-iOS-amp-Apps",
		"http://forum.kompas.com/forums/233-Android-amp-Apps",
		"http://forum.kompas.com/forums/54-Computer-Corner",
		"http://forum.kompas.com/forums/57-Jaringan-Telekomunikasi-dan-Internet",
		"http://forum.kompas.com/forums/25-Gaming-World",
		"http://forum.kompas.com/forums/18-Otomotif-Umum",
		"http://forum.kompas.com/forums/171-Car-Corner",
		"http://forum.kompas.com/forums/172-Motor-Corner",
		"http://forum.kompas.com/forums/173-ShowOff",
		"http://forum.kompas.com/forums/121-Bincang-Buku",
		"http://forum.kompas.com/forums/153-Favorit-Writers",
		"http://forum.kompas.com/forums/185-Photo-Story-amp-Behind-the-Scene",
		"http://forum.kompas.com/forums/184-Peralatan",
		"http://forum.kompas.com/forums/182-Agenda-Fotografi",
		"http://forum.kompas.com/forums/183-Klinik-Fotografi-Kompas",
		"http://forum.kompas.com/forums/187-Umum-Images",
		"http://forum.kompas.com/forums/206-Lapak-Jual-Beli",
		"http://forum.kompas.com/forums/197-Lapak-Elektronik",
		"http://forum.kompas.com/forums/203-Lapak-Komputer-amp-Gadget",
		"http://forum.kompas.com/forums/198-Lapak-Otomotif",
		"http://forum.kompas.com/forums/199-Lapak-Properti",
		"http://forum.kompas.com/forums/200-Lapak-Busana-amp-Aksesoris",
		"http://forum.kompas.com/forums/202-Lapak-Musik-amp-Olahraga",
	]
	COUNTRY = "IDN"
	THREAD_XPATH = "//a[re:test(@id,'thread_title_*')]"
	THREAD_LINK_XPATH = "./@href"
	LAST_PAGE_XPATH = "//div[@class='pagination_top']//span[@class='first_last']/a/@href"
	PREV_XPATH = "//div[@class='pagination_top']//span[@class='prev_next']/a/@href"
	POST_XPATH = "//ol[@id='posts']/li[re:test(@id,'post_*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath": ".//span[@class='date']/text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//div[@class='username_container']//a[re:test(@class, 'username*')]/strong//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='content']//text()"
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
			"xpath":"//div[@id='breadcrumb']//li[@class='navbit lastnavbit']//text()"
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
