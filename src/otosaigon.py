from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "otosaigon"
	CRAWLER_NAME = "Otosaigon Crawler"
	LINK_TO_CRAWL = [
		'https://www.otosaigon.com/forums/am-thanh-xe-hoi.68/',
		'https://www.otosaigon.com/forums/audi.134/',
		'https://www.otosaigon.com/forums/ben-xe-du-liu-tiu.72/',
		'https://www.otosaigon.com/forums/bmw.46/',
		'https://www.otosaigon.com/forums/ca-phe-xuyen-viet.71/',		
		'https://www.otosaigon.com/forums/chuyen-muc-nhiep-anh-os.135/',
		'https://www.otosaigon.com/forums/clb-the-duc-the-thao.198/',
		'https://www.otosaigon.com/forums/cong-nghe-o-to-cartech.309/',
		'https://www.otosaigon.com/forums/cong-nghe-thong-tin.280/',
		'https://www.otosaigon.com/forums/du-lich-kham-pha.181/',
		'https://www.otosaigon.com/forums/e-gara-ky-thuat-benh-vien-o-to.82/',
		'https://www.otosaigon.com/forums/emma-vietnam.205/',
		'https://www.otosaigon.com/forums/fiat.48/',
		'https://www.otosaigon.com/forums/ford.49/',
		'https://www.otosaigon.com/forums/formula-1.93/',
		'https://www.otosaigon.com/forums/gm-chevrolet.50/',
		'https://www.otosaigon.com/forums/gop-y-huong-dan-su-dung-lien-he-qc.81/',
		'https://www.otosaigon.com/forums/honda.99/',
		'https://www.otosaigon.com/forums/hop-mat-giao-luu-chia-se.69/',
		'https://www.otosaigon.com/forums/hyundai.52/',
		'https://www.otosaigon.com/forums/infiniti.305/',
		'https://www.otosaigon.com/forums/isuzu.51/',
		'https://www.otosaigon.com/forums/kia.186/',
		'https://www.otosaigon.com/forums/kinh-nghiem-cho-nguoi-moi-lai-xe.304/',
		'https://www.otosaigon.com/forums/len-noi-that-do-dan-ngoai.67/',
		'https://www.otosaigon.com/forums/lexus.310/',
		'https://www.otosaigon.com/forums/mazda.53/',
		'https://www.otosaigon.com/forums/mercedes-benz.54/',
		'https://www.otosaigon.com/forums/mitsubishi.55/',
		'https://www.otosaigon.com/forums/ngua-sat-dau-yeu.79/',
		'https://www.otosaigon.com/forums/nissan.100/',
		'https://www.otosaigon.com/forums/os-finance-investment.227/',
		'https://www.otosaigon.com/forums/os-voi-cong-dong.185/',
		'https://www.otosaigon.com/forums/pickup-offroad-club-poc.184/',
		'https://www.otosaigon.com/forums/renault.254/',
		'https://www.otosaigon.com/forums/s-o-s-ho-tro-giao-thong.258/',
		'https://www.otosaigon.com/forums/sieu-xe-supercar.202/',
		'https://www.otosaigon.com/forums/sinh-nhat-os-cac-su-kien-offline-os.101/',
		'https://www.otosaigon.com/forums/subaru.233/',
		'https://www.otosaigon.com/forums/suzuki.57/',
		'https://www.otosaigon.com/forums/thong-bao-tu-ban-quan-tri.162/',
		'https://www.otosaigon.com/forums/tin-tuc-tu-van-cong-nghe-o-to.127/',
		'https://www.otosaigon.com/forums/toyota.58/',
		'https://www.otosaigon.com/forums/tren-duong-thien-ly-va-cac-thac-mac-biet-hoi-ai.78/',
		'https://www.otosaigon.com/forums/tu-van-mam-lop-xe.282/',
		'https://www.otosaigon.com/forums/tu-van-mua-ban-o-to.187/'
	]
	COUNTRY = "VNM"
	THREAD_XPATH = "//ol[@class='discussionListItems']//li[re:test(@id,'thread*')]"
	THREAD_LINK_XPATH = "//div[@class='titleText']//h3[@class='title']//a[@class='PreviewTooltip']/@href"
	LAST_PAGE_XPATH = "(//div[@class='PageNav']/nav//a[not(contains(@class,'text'))])[last()]/@href"
	PREV_XPATH = "(//div[@class='PageNav']/nav//a[contains(@class,'text')])[1]/@href"
	POST_XPATH = "//ol[@id='messageList']//li[re:test(@id,'post-*')]"
	FIELDS = [
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath": "concat(substring(concat(concat('20',substring-before(substring-after(substring-after(.//span[@class='item muted']//a[@class='datePermalink']/span/@title,'/'),'/'),' ')),'/',substring-before(substring-after(.//span[@class='item muted']//a[@class='datePermalink']/span/@title,'/'),'/'),'/',substring-before(.//span[@class='item muted']//a[@class='datePermalink']/span/@title,'/'),' ',substring-after(substring-after(substring-after(.//span[@class='item muted']//a[@class='datePermalink']/span/@title,'/'),'/'),'lúc ')),	1 div contains(.//span[@class='item muted']//a[@class='datePermalink']/span/@title,'/')),substring(	.//span[@class='item muted']//a[@class='datePermalink']/abbr/@data-time,1 div not(contains(.//span[@class='item muted']//a[@class='datePermalink']/span/@title,'/'))))"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":".//div[@class='messageUserBlock']//h3[@class='userText']//a[@class='username']//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='messageContent']/article/blockquote//text()[1]"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath":".//div[@class='publicControls']//a/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"normalize-space(//div[@class='mainContent']//div[@class='titleBar']//h1//text())"
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