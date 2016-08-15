from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "t-shirtforums"
	CRAWLER_NAME = "T-shirtforums Crawler"
	LINK_TO_CRAWL = [
		"http://www.t-shirtforums.com/announcements-site-updates/",
		"http://www.t-shirtforums.com/forum-information/",
		"http://www.t-shirtforums.com/t-shirt-forum-site-issues-help-desk/",
		"http://www.t-shirtforums.com/t-shirt-printing-issues/",
		"http://www.t-shirtforums.com/general-t-shirt-selling-discussion/",
		"http://www.t-shirtforums.com/graphics-design-help/",
		"http://www.t-shirtforums.com/business-finance/",
		"http://www.t-shirtforums.com/ecommerce-site-design/",
		"http://www.t-shirtforums.com/t-shirt-marketing/",
		"http://www.t-shirtforums.com/offline-retail-tradeshows/",
		"http://www.t-shirtforums.com/t-shirt-tag-relabeling-finishing/",
		"http://www.t-shirtforums.com/t-shirt-fulfillment-services/",
		"http://www.t-shirtforums.com/cafepress/",
		"http://www.t-shirtforums.com/zazzle/",
		"http://www.t-shirtforums.com/printmojo/",
		"http://www.t-shirtforums.com/spreadshirt/",
		"http://www.t-shirtforums.com/printfection/",
		"http://www.t-shirtforums.com/region-specific-t-shirt-information/",
		"http://www.t-shirtforums.com/asia/",
		"http://www.t-shirtforums.com/australia-new-zealand/",
		"http://www.t-shirtforums.com/canada/",
		"http://www.t-shirtforums.com/europe/",
		"http://www.t-shirtforums.com/united-kingdom/",
		"http://www.t-shirtforums.com/screen-printing/",
		"http://www.t-shirtforums.com/screen-printing-equipment/",
		"http://www.t-shirtforums.com/plastisol-ink-screen-printing/",
		"http://www.t-shirtforums.com/water-based-ink-screen-printing/",
		"http://www.t-shirtforums.com/heat-press-heat-transfers/",
		"http://www.t-shirtforums.com/inkjet-heat-transfer-paper/",
		"http://www.t-shirtforums.com/laser-heat-transfer-paper/",
		"http://www.t-shirtforums.com/heat-presses-equipment/",
		"http://www.t-shirtforums.com/printers-inks-inkjet-laser-transfers/",
		"http://www.t-shirtforums.com/t-shirt-crossover-diary-heat-press-newbie/",
		"http://www.t-shirtforums.com/plastisol-transfers/",
		"http://www.t-shirtforums.com/vinyl-cutters-plotters-transfers/",
		"http://www.t-shirtforums.com/gcc-brand-vinyl-cutters/",
		"http://www.t-shirtforums.com/vinyl-signs-decals/",
		"http://www.t-shirtforums.com/graphtec-brand-vinyl-cutters/",
		"http://www.t-shirtforums.com/knk-vinyl-cutters/",
		"http://www.t-shirtforums.com/roland-vinyl-cutters/",
		"http://www.t-shirtforums.com/summa-vinyl-cutters/",
		"http://www.t-shirtforums.com/rhinestone-decoration/",
		"http://www.t-shirtforums.com/direct-garment-dtg-inkjet-printing/",
		"http://www.t-shirtforums.com/aeoon-dtg/",
		"http://www.t-shirtforums.com/anajet/",
		"http://www.t-shirtforums.com/belquette/",
		"http://www.t-shirtforums.com/brother/",
		"http://www.t-shirtforums.com/dtg-brand/",
		"http://www.t-shirtforums.com/epson-surecolor-dtg-printers/",
		"http://www.t-shirtforums.com/fast-t-jet/",
		"http://www.t-shirtforums.com/firebird-inks/",
		"http://www.t-shirtforums.com/freejet/",
		"http://www.t-shirtforums.com/kornit/",
		"http://www.t-shirtforums.com/m-r-digital/",
		"http://www.t-shirtforums.com/mimaki/",
		"http://www.t-shirtforums.com/ms-brand/",
		"http://www.t-shirtforums.com/neoflex/",
		"http://www.t-shirtforums.com/resolute-dtg/",
		"http://www.t-shirtforums.com/sawgrass/",
		"http://www.t-shirtforums.com/spectra/",
		"http://www.t-shirtforums.com/texjet/",
		"http://www.t-shirtforums.com/veloci-jet/",
		"http://www.t-shirtforums.com/diy-dtg/",
		"http://www.t-shirtforums.com/dtg-inks/",
		"http://www.t-shirtforums.com/dtg-pretreatment/",
		"http://www.t-shirtforums.com/dtg-battle-royale/",
		"http://www.t-shirtforums.com/dye-sublimation/",
		"http://www.t-shirtforums.com/pad-printing/",
		"http://www.t-shirtforums.com/find-wholesale-blank-t-shirts-other-imprintable-products/",
		"http://www.t-shirtforums.com/embroidery/",
		"http://www.t-shirtforums.com/pro-world-help-forums/",
		"http://www.t-shirtforums.com/heat-presses-sold-pro-world/",
		"http://www.t-shirtforums.com/using-pro-world-transfer-paper/",
		"http://www.t-shirtforums.com/pro-world-heat-transfer-application/",
		"http://www.t-shirtforums.com/custom-transfers-pro-world/",
		"http://www.t-shirtforums.com/suggestions-ideas-pro-world/",
		"http://www.t-shirtforums.com/cad-cut-direct-help-forums/",
		"http://www.t-shirtforums.com/cad-cut-materials-sold-cad-cut-direct/",
		"http://www.t-shirtforums.com/stahls-applique-innovation/",
		"http://www.t-shirtforums.com/cad-color-materials-sold-cad-cut-direct/",
		"http://www.t-shirtforums.com/vinyl-cutters-printer-cutters-heat-presses-being-used-cad-cut-direct-materials/",
		"http://www.t-shirtforums.com/cad-cut-h2o-beta-innovation/",
		"http://www.t-shirtforums.com/fruit-loom-help-forums/",
		"http://www.t-shirtforums.com/jerzees-help-forums/",
		"http://www.t-shirtforums.com/need-help-finding-t-shirt-design/",
		"http://www.t-shirtforums.com/general-t-shirt-buying-discussion/",
		"http://www.t-shirtforums.com/t-shirt-industry-news/",
		"http://www.t-shirtforums.com/t-shirt-articles/",
		"http://www.t-shirtforums.com/t-shirtforums-newsletter-articles/",
    ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//a[re:test(@id,'thread_title_*')]"
	THREAD_LINK_XPATH = "./@href"
	LAST_PAGE_XPATH = "(//div[@class='pagenav']//td[@class='vbmenu_control'])[last()]//preceding::a[re:test(@title,'Last Page*') or re:test(@title,'Show results*')][1]/@href"
	PREV_XPATH = "//div[@class='pagenav']//a[@rel='prev']/@href"
	POST_XPATH = "//div[@id='posts']//table[re:test(@id,'post*') and @class='tborder vbseo_like_postbit']"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": True,
			"xpath":".//a[re:test(@id,'postcount*')]/preceding::text()[1]"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//a[@class='bigusername']//text()"
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
			"xpath": ".//a[@title='Link to this Post']/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"(//span[@class='navbar'])[last()]/a/text()"
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
