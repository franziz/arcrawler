from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "idws"
	CRAWLER_NAME = "idws crawler"
	LINK_TO_CRAWL = [
		"http://forum.idws.id/forums/informasi-utama.12/",
		"http://forum.idws.id/forums/dev-update.433/",
		"http://forum.idws.id/forums/kotak-suara-idws.17/",
		"http://forum.idws.id/forums/laporan-error-abuse-or-illegal.27/",
		"http://forum.idws.id/forums/butuh-bantuan.534/",
		"http://forum.idws.id/categories/spesial-dari-kami.661/",
		"http://forum.idws.id/forums/konsultasi-it.662/",
		"http://forum.idws.id/forums/event.154/",
		"http://forum.idws.id/forums/store-idws.665/",
		"http://forum.idws.id/forums/komunitas.306/",
		"http://forum.idws.id/forums/tengah-komunitas.13/",
		"http://forum.idws.id/forums/gossip.195/",
		"http://forum.idws.id/forums/pojok-komunitas.305/",
		"http://forum.idws.id/forums/groups-node.652/",
		"http://forum.idws.id/forums/pictures-gallery.52/",
		"http://forum.idws.id/forums/celebrity-snapshot.160/",
		"http://forum.idws.id/forums/photography-graphic-design-showcase.452/",
		"http://forum.idws.id/forums/random-images.496/",
		"http://forum.idws.id/forums/lifestyle.48/",
		"http://forum.idws.id/forums/official-and-free-talk.533/",
		"http://forum.idws.id/forums/beauty-and-body-care.530/",
		"http://forum.idws.id/forums/fashion.531/",
		"http://forum.idws.id/forums/wedding.535/",
		"http://forum.idws.id/forums/parenting-and-pregnancy.532/",
		"http://forum.idws.id/forums/writing-zone.453/",
		"http://forum.idws.id/forums/dear-diary.155/",
		"http://forum.idws.id/forums/fiction.242/",
		"http://forum.idws.id/forums/colors-of-life.454/",
		"http://forum.idws.id/forums/curhat.153/",
		"http://forum.idws.id/forums/humor.423/",
		"http://forum.idws.id/forums/motivasi-inspirasi.419/",
		"http://forum.idws.id/forums/dunia-lain.325/",
		"http://forum.idws.id/forums/education.89/",
		"http://forum.idws.id/forums/history-and-culture.43/",
		"http://forum.idws.id/forums/indonesian-history.499/",
		"http://forum.idws.id/forums/world-history.500/",
		"http://forum.idws.id/forums/science-and-technology.377/",
		"http://forum.idws.id/forums/education-free-talk-and-trivia.395/",
		"http://forum.idws.id/forums/school-and-campus-zone.397/",
		"http://forum.idws.id/forums/military-interest.537/",
		"http://forum.idws.id/forums/books.538/",
		"http://forum.idws.id/forums/book-review.421/",
		"http://forum.idws.id/forums/keep-up-your-health.53/",
		"http://forum.idws.id/forums/intensive-health-unit.413/",
		"http://forum.idws.id/forums/pengetahuan-penting-penunjang-kesehatan.415/",
		"http://forum.idws.id/forums/dokumenter.29/",
		"http://forum.idws.id/forums/profile.369/",
		"http://forum.idws.id/forums/creative-community.524/",
		"http://forum.idws.id/forums/fansubs-encoders.525/",
		"http://forum.idws.id/forums/movie-maker.527/",
		"http://forum.idws.id/forums/indie.329/",
		"http://forum.idws.id/forums/radio.497/",
		"http://forum.idws.id/forums/business-center-entrepreneurship-center.467/",
		"http://forum.idws.id/forums/entrepreneur-talks.470/",
		"http://forum.idws.id/forums/cooperate-corner.469/",
		"http://forum.idws.id/forums/micro-business-talks.468/",
		"http://forum.idws.id/forums/make-money-online.78/",
		"http://forum.idws.id/forums/adsense.202/",
		"http://forum.idws.id/forums/affiliate-program.204/",
		"http://forum.idws.id/forums/forex-trading.379/",
		"http://forum.idws.id/forums/career-talks.465/",
		"http://forum.idws.id/forums/job-vacancy.229/",
		"http://forum.idws.id/forums/money-talks.464/",		
		"http://forum.idws.id/forums/pc-games-online.73/",
		"http://forum.idws.id/forums/games-free-talk.80/",
		"http://forum.idws.id/forums/gadget-zone.55/",
		"http://forum.idws.id/forums/hardware-zone.539/",
		"http://forum.idws.id/forums/software-zone.540/",
		"http://forum.idws.id/forums/free-talk-zone.541/",
		"http://forum.idws.id/forums/travelling-and-culinary.50/",
		"http://forum.idws.id/forums/sports-center.57/",
		"http://forum.idws.id/forums/soccer.205/",
		"http://forum.idws.id/forums/meramu-meracik.65/",
		"http://forum.idws.id/forums/request-resep.66/",
		"http://forum.idws.id/forums/otomotif.196/",
		"http://forum.idws.id/forums/flora-dan-fauna.207/",
		"http://forum.idws.id/forums/nusantara.209/",
		"http://forum.idws.id/forums/jabodetabek.210/",
		"http://forum.idws.id/forums/jakarta.297/",
		"http://forum.idws.id/forums/bogor.298/",
		"http://forum.idws.id/forums/depok.299/",
		"http://forum.idws.id/forums/tangerang.300/",
		"http://forum.idws.id/forums/bekasi.301/",
		"http://forum.idws.id/forums/jawa-bali-dan-sekitarnya.218/",
		"http://forum.idws.id/forums/bandung.211/",
		"http://forum.idws.id/forums/jogja.212/",
		"http://forum.idws.id/forums/semarang.214/",
		"http://forum.idws.id/forums/surabaya-malang.213/",
		"http://forum.idws.id/forums/surakarta.285/",
		"http://forum.idws.id/forums/bali.215/",
		"http://forum.idws.id/forums/sumatera.219/",
		"http://forum.idws.id/forums/medan.216/",
		"http://forum.idws.id/forums/aceh.217/",
		"http://forum.idws.id/forums/jambi.220/",
		"http://forum.idws.id/forums/palembang.221/",
		"http://forum.idws.id/forums/lampung.222/",
		"http://forum.idws.id/forums/batam.227/",
		"http://forum.idws.id/forums/riau.231/",
		"http://forum.idws.id/forums/padang.232/",
		"http://forum.idws.id/forums/kalimantan.223/",
		"http://forum.idws.id/forums/pontianak.224/",
		"http://forum.idws.id/forums/sulawesi.225/",
		"http://forum.idws.id/forums/papua.226/",
		"http://forum.idws.id/forums/luar-negeri.228/",
		"http://forum.idws.id/forums/official-feedback-testimonial.345/",
		"http://forum.idws.id/forums/computer-stuff.90/",
		"http://forum.idws.id/forums/processor-motherboard.108/",
		"http://forum.idws.id/forums/software.111/",
		"http://forum.idws.id/forums/keyboards-mouse-input.103/",
		"http://forum.idws.id/forums/desktop-pc.102/",
		"http://forum.idws.id/forums/casing-power-supply-cooling.101/",
		"http://forum.idws.id/forums/monitor-display.104/",
		"http://forum.idws.id/forums/memory.105/",
		"http://forum.idws.id/forums/networking-communications.106/",
		"http://forum.idws.id/forums/sound-graphics-video-card.110/",
		"http://forum.idws.id/forums/notebook.107/",
		"http://forum.idws.id/forums/printer-scanner-ink.109/",
		"http://forum.idws.id/forums/drives-storage.112/",
		"http://forum.idws.id/forums/aksesoris-perangkat-lainnya.100/",
		"http://forum.idws.id/forums/toys-and-hobbies.98/",
		"http://forum.idws.id/forums/action-figures.113/",
		"http://forum.idws.id/forums/model-kit.116/",
		"http://forum.idws.id/forums/die-cast-mini-4wd-r-c.457/",
		"http://forum.idws.id/forums/airsoft.115/",
		"http://forum.idws.id/forums/cards.119/",
		"http://forum.idws.id/forums/others-toys-and-hobbies.114/",
		"http://forum.idws.id/forums/flora-dan-fauna.143/",
		"http://forum.idws.id/forums/flora-tumbuhan.144/",
		"http://forum.idws.id/forums/fauna-hewan.145/",
		"http://forum.idws.id/forums/collectibles.146/",
		"http://forum.idws.id/forums/art-handicraft.459/",
		"http://forum.idws.id/forums/antique.460/",
		"http://forum.idws.id/forums/book-shop.458/",
		"http://forum.idws.id/forums/handphone-pda.92/",
		"http://forum.idws.id/forums/kartu-perdana.99/",
		"http://forum.idws.id/forums/pulsa.462/",
		"http://forum.idws.id/forums/aksesoris-sparepart-service-handphone.461/",
		"http://forum.idws.id/forums/video-games.486/",
		"http://forum.idws.id/forums/console-handheld.487/",
		"http://forum.idws.id/forums/games.131/",
		"http://forum.idws.id/forums/online-gaming.488/",
		"http://forum.idws.id/forums/aksesoris-sparepart-service-video-games.489/",
		"http://forum.idws.id/forums/elektronik.490/",
		"http://forum.idws.id/forums/gadgets-aksesoris.491/",
		"http://forum.idws.id/forums/kamera-aksesoris.492/",
		"http://forum.idws.id/forums/elektronik-lainnya.493/",
		"http://forum.idws.id/forums/dvd-cd.93/",
		"http://forum.idws.id/forums/audio.132/",
		"http://forum.idws.id/forums/movies.133/",
		"http://forum.idws.id/forums/others-dvd-cd.134/",
		"http://forum.idws.id/forums/gadget-console-games.91/",
		"http://forum.idws.id/forums/fashion-mode.96/",
		"http://forum.idws.id/forums/baju.135/",
		"http://forum.idws.id/forums/sepatu.136/",
		"http://forum.idws.id/forums/tas-dompet.137/",
		"http://forum.idws.id/forums/aksesoris.138/",
		"http://forum.idws.id/forums/distro-clothing.139/",
		"http://forum.idws.id/forums/branded.141/",
		"http://forum.idws.id/forums/second-hand.142/",
		"http://forum.idws.id/forums/others-fashion-mode.140/",
		"http://forum.idws.id/forums/makanan-minuman.95/",
		"http://forum.idws.id/forums/makanan-minuman.117/",
		"http://forum.idws.id/forums/otomotif.94/",
		"http://forum.idws.id/forums/kendaraan-roda-empat.126/",
		"http://forum.idws.id/forums/perlengkapan-aksesoris-kendaraan-roda-4.127/",
		"http://forum.idws.id/forums/kendaraan-roda-dua.124/",
		"http://forum.idws.id/forums/perlengkapan-aksesoris-kendaraan-roda-2.125/",
		"http://forum.idws.id/forums/interior-exterior-dan-aksesoris.123/",
		"http://forum.idws.id/forums/jasa.77/",
		"http://forum.idws.id/forums/jasa-download.129/",
		"http://forum.idws.id/forums/kartu-kredit.128/",
		"http://forum.idws.id/forums/jasa-lainnya.130/",
		"http://forum.idws.id/forums/properties.97/",
		"http://forum.idws.id/forums/others-shopping-corner.76/"
    ]
	COUNTRY = "IDN"
	THREAD_XPATH = "//ol[@class='discussionListItems']/li[re:test(@id,'thread-*')]"
	THREAD_LINK_XPATH = ".//a[@class='PreviewTooltip']/@href"
	LAST_PAGE_XPATH = "(//div[@class='PageNav']//a)[last()-1]/@href"
	PREV_XPATH = "//div[@class='PageNav']//a[@class='currentPage ']/preceding-sibling::a[1]/@href"
	POST_XPATH = "//ol[@class='messageList']/li[re:test(@id,'post-*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath": "concat(.//a[@class='datePermalink']/abbr/text(),.//a[@class='datePermalink']/span/@title)"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//a[@class='username']//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='messageContent']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//a[@title='Permalink']/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@class='titleBar']/h1/text()"
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
