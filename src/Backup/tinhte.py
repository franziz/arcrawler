from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "tinhte"
	CRAWLER_NAME = "Tinhte Crawler"
	LINK_TO_CRAWL = [
		"https://tinhte.vn/forums/thong-tin-cong-nghe.10/",
		"https://tinhte.vn/forums/thuong-mai-dien-tu.636/",
		"https://tinhte.vn/forums/dam-may-dich-vu-truc-tuyen.460/",
		"https://tinhte.vn/forums/tham-do-cong-nghe.232/",
		"https://tinhte.vn/forums/ca-phe-tinh-te.36/",
		"https://tinhte.vn/forums/quang-cao-khuyen-mai.230/",
		"https://tinhte.vn/forums/chu-viet-nhanh.639/",
		# "https://tinhte.vn/forums/contests/", No need to crawl this one
		"https://tinhte.vn/categories/may-tinh-windows.6/",
		"https://tinhte.vn/categories/may-tinh-apple-mac-os-x.195/",
		"https://tinhte.vn/forums/may-tinh-linux.79/",
		"https://tinhte.vn/forums/may-tinh-chrome-os.402/",
		"https://tinhte.vn/forums/tu-van-chon-mua-may-tinh.199/",
		"https://tinhte.vn/forums/anh-nen-wallpaper.64/",
		"https://tinhte.vn/categories/ios.82/",
		"https://tinhte.vn/categories/android.150/",
		"https://tinhte.vn/categories/windows-phone.3/",
		"https://tinhte.vn/categories/blackberry.98/",
		"https://tinhte.vn/forums/dien-thoai-nhat-ban.459/",
		"https://tinhte.vn/forums/dien-thoai-pho-thong.362/",
		"https://tinhte.vn/forums/tu-van-chon-mua-dtdd.368/",
		"https://tinhte.vn/forums/lap-trinh-cho-di-dong.270/",
		"https://tinhte.vn/forums/mang-di-dong.510/",
		"https://tinhte.vn/categories/windows-mobile.247/",
		"https://tinhte.vn/categories/symbian.83/",
		"https://tinhte.vn/categories/palm-os-webos.4/",
		"https://tinhte.vn/forums/meego.405/",
		"https://tinhte.vn/forums/samsung-bada.429/",
		"https://tinhte.vn/forums/tin-tuc.71/",
		"https://tinhte.vn/forums/danh-gia.660/",
		"https://tinhte.vn/forums/su-kien-nhiep-anh.559/",
		"https://tinhte.vn/forums/kien-thuc-cam-nang.560/",
		"https://tinhte.vn/forums/nghe-thuat-chup-anh.566/",
		"https://tinhte.vn/forums/xu-ly-anh-so.571/",
		"https://tinhte.vn/forums/hoi-dap-thao-luan.561/",
		"https://tinhte.vn/forums/anh-binh-anh.547/",
		"https://tinhte.vn/forums/xe-may.544/",
		"https://tinhte.vn/forums/xe-o-to.545/",
		"https://tinhte.vn/forums/xe-dap.628/",
		"https://tinhte.vn/forums/giao-thong-ptvc-khac.546/",
		"https://tinhte.vn/forums/khoa-hoc.76/",
		"https://tinhte.vn/forums/thiet-bi-ngoai-vi.29/",
		"https://tinhte.vn/forums/dien-tu-tieu-dung.293/",
		"https://tinhte.vn/forums/tv-va-dau-thu-phat-noi-dung.621/",
		"https://tinhte.vn/forums/may-doc-sach-ebook.426/",
		"https://tinhte.vn/forums/may-choi-game.77/",
		"https://tinhte.vn/forums/gps.347/",
		"https://tinhte.vn/forums/dong-ho-thong-minh.633/",
		# "https://tinhte.vn/hotro/", No need to crawl this one
		"https://tinhte.vn/forums/thong-bao-tu-tinhte-vn.2/",
		"https://tinhte.vn/forums/gop-y-xay-dung-dien-dan.81/"
    ]
	COUNTRY = "VNM"
	THREAD_XPATH = "//ol/li[re:test(@id,'thread-*')]"
	THREAD_LINK_XPATH = ".//h3[@class='title']/a/@href"
	LAST_PAGE_XPATH = "(//div[@class='PageNav']/nav/a)[last()-1]/@href"
	PREV_XPATH = "//div[@class='PageNav']/nav//a[@class='currentPage ']/preceding-sibling::a[1]/@href"
	POST_XPATH = "//form[@class='InlineModForm section']/ol/li[re:test(@id,'post-*')]"
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
			"xpath": ".//h3[@class='userText']//a/text()"
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
			"xpath": ".//div[@class='messageDetails']/a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@class='titleBar']/h1//text()"
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
