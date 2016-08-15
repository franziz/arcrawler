from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "otofun"
	CRAWLER_NAME = "Otofun Crawler"
	LINK_TO_CRAWL = [
		 'https://www.otofun.net/forums/am-thanh-die%CC%A3n-no%CC%A3i-tha%CC%81t.68/',
		 'https://www.otofun.net/forums/audi.156/',
		 'https://www.otofun.net/forums/bat-dong-san.284/',
		 'https://www.otofun.net/forums/benh-xa-of.131/',
		 'https://www.otofun.net/forums/bmw.21/',
		 'https://www.otofun.net/forums/cac-hang-xe-khac.43/',
		 'https://www.otofun.net/forums/cac-hoi-khac.114/',
		 'https://www.otofun.net/forums/car-designs-concepts.37/',
		 'https://www.otofun.net/forums/cau-chuyen-cac-chuyen-di.26/',
		 'https://www.otofun.net/forums/chi-hoi-cac-dia-phuong.134/',
		 'https://www.otofun.net/forums/cho-gioi.89/',
		 'https://www.otofun.net/forums/clb-nhiep-anh-of-o-pho.74/',
		 'https://www.otofun.net/forums/clb-offroad.63/',
		 'https://www.otofun.net/forums/clb-thuy-luc-khong-quan.130/',
		 'https://www.otofun.net/forums/cong-nghe-ky-thuat.10/',
		 'https://www.otofun.net/forums/daihatsu-isuzu-suzuki.35/',
		 'https://www.otofun.net/forums/do-cong-suat.69/',
		 'https://www.otofun.net/forums/fiat.82/',
		 'https://www.otofun.net/forums/ford.24/',
		 'https://www.otofun.net/forums/giai-tri-thu-gian.287/',
		 'https://www.otofun.net/forums/gm-chevrolet.30/',
		 'https://www.otofun.net/forums/hai-banh-xe-quay.124/',
		 'https://www.otofun.net/forums/hoi-dap-ve-luat-cac-thu-tuc.13/',
		 'https://www.otofun.net/forums/honda.31/',
		 'https://www.otofun.net/forums/htx-onroad.235/',
		 'https://www.otofun.net/forums/hyundai.39/',
		 'https://www.otofun.net/forums/khoe-xe.11/',
		 'https://www.otofun.net/forums/khu-vuc-cac-gian-hang-khac.220/',
		 'https://www.otofun.net/forums/khu-vuc-cac-gian-hang-lien-quan-den-oto.219/',
		 'https://www.otofun.net/forums/khu-vuc-sinh-hoat-cua-cac-chi-hoi.91/',
		 'https://www.otofun.net/forums/kia.245/',
		 'https://www.otofun.net/forums/mazda.29/',
		 'https://www.otofun.net/forums/mercedes-benz.32/',
		 'https://www.otofun.net/forums/mitsubishi.33/',
		 'https://www.otofun.net/forums/moto-phan-khoi-lon.125/',
		 'https://www.otofun.net/forums/mua-ban-xe-2-3-banh.280/',
		 'https://www.otofun.net/forums/mua-xe-ban-xe.88/',
		 'https://www.otofun.net/forums/nang-cap-ngoai-that.67/',
		 'https://www.otofun.net/forums/nissan.143/',
		 'https://www.otofun.net/forums/of-vi-cong-dong.120/',
		 'https://www.otofun.net/forums/ofer-gop-y-voi-bdh.139/',		 
		 'https://www.otofun.net/forums/quan-cafe-otofun.77/',
		 'https://www.otofun.net/forums/renault.230/',
		 'https://www.otofun.net/forums/showroom-oto.278/',
		 'https://www.otofun.net/forums/sidecar-ba-banh.123/',
		 'https://www.otofun.net/forums/sinh-nhat-of-10.307/',
		 'https://www.otofun.net/forums/ssangyong.86/',
		 'https://www.otofun.net/forums/su-dung-bao-duong-sua-chua.9/',
		 'https://www.otofun.net/forums/subaru.293/',
		 'https://www.otofun.net/forums/tai-chinh-ngan-hang.285/',
		 'https://www.otofun.net/forums/thong-bao-huong-dan.4/',
		 'https://www.otofun.net/forums/thong-tin-ve-of-plaza.240/',
		 'https://www.otofun.net/forums/toa-nha-cong-nghe-thong-tin.76/',
		 'https://www.otofun.net/forums/toyota.36/',
		 'https://www.otofun.net/forums/trien-lam-o-to-quoc-te-2015-vims2015.299/',
		 'https://www.otofun.net/forums/trung-tam-the-duc-the-thao.75/',
		 'https://www.otofun.net/forums/vhgt-atgt-kinh-nghiem-lai-xe.15/',
		 'https://www.otofun.net/forums/vietnam-motorshow-2015.301/',
		 'https://www.otofun.net/forums/volkswagen.261/',
		 'https://www.otofun.net/forums/xe-dop.216/'
	]
	COUNTRY = "VNM"
	THREAD_XPATH = "//ol[@class='discussionListItems']//li"
	THREAD_LINK_XPATH = ".//div[@class='titleText']//h3[@class='title']//a[@class='PreviewTooltip']/@href"
	LAST_PAGE_XPATH = "(//div[@class='PageNav']/nav//a[not(contains(@class,'text'))])[last()]/@href"
	PREV_XPATH = "(//div[@class='PageNav']/nav//a[contains(@class,'text')])[1]/@href"
	POST_XPATH = "//li[re:test(@id,'post-*')]"
	FIELDS = [
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":"concat(concat('20',substring-before(substring-after(substring-after(translate(.//div[@class='messageHead']//text(),'lúc',''),'/'),'/'),' ')),'/',substring-before(substring-after(translate(.//div[@class='messageHead']//text(),'lúc',''),'/'),'/'),'/',substring-before(translate(.//div[@class='messageHead']//text(),'lúc',''),'/'),' ',	substring-after(substring-after(substring-after(translate(.//div[@class='messageHead']//text(),'lúc',''),'/'),'/'),' '))"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":".//div[@class='messageUserInfo']//div[@class='userText']//a[@class='username']//text()"
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
			"xpath":".//div[@class='messageHead']//a[@class='headPermalink']//@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"normalize-space((//div[@class='titleBar']//h1//text())[last()])"
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
