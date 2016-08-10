from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "digitalpoint"
	CRAWLER_NAME = "Digitalpoint Crawler"
	LINK_TO_CRAWL = [
		"https://forums.digitalpoint.com/forums/google.5/",
		"https://forums.digitalpoint.com/forums/adsense.27/",
		"https://forums.digitalpoint.com/forums/guidelines-compliance.69/",
		"https://forums.digitalpoint.com/forums/placement-reviews-examples.72/",
		"https://forums.digitalpoint.com/forums/reporting-stats.71/",
		"https://forums.digitalpoint.com/forums/payments.68/",
		"https://forums.digitalpoint.com/forums/35/",
		"https://forums.digitalpoint.com/forums/112/",
		"https://forums.digitalpoint.com/forums/142/",
		"https://forums.digitalpoint.com/forums/62/",
		"https://forums.digitalpoint.com/forums/google-api.7/",
		"https://forums.digitalpoint.com/forums/shopping.8/",
		"https://forums.digitalpoint.com/forums/yahoo.6/",
		"https://forums.digitalpoint.com/forums/publisher-network.47/",
		"https://forums.digitalpoint.com/forums/84/",
		"https://forums.digitalpoint.com/forums/yahoo-api.46/",
		"https://forums.digitalpoint.com/forums/bing.43/",
		"https://forums.digitalpoint.com/forums/bing-ads.82/",
		"https://forums.digitalpoint.com/forums/all-other-search-engines.26/",
		"https://forums.digitalpoint.com/forums/directories.25/",
		"https://forums.digitalpoint.com/forums/solicitations-announcements.65/",
		"https://forums.digitalpoint.com/forums/odp-dmoz.66/",
		"https://forums.digitalpoint.com/forums/general-business.33/",
		"https://forums.digitalpoint.com/forums/general-marketing.21/",
		"https://forums.digitalpoint.com/forums/search-engine-optimization.12/",
		"https://forums.digitalpoint.com/forums/keywords.77/",
		"https://forums.digitalpoint.com/forums/microdata.67/",
		"https://forums.digitalpoint.com/forums/payment-processing.101/",
		"https://forums.digitalpoint.com/forums/paypal.134/",
		"https://forums.digitalpoint.com/forums/social-networks.118/",
		"https://forums.digitalpoint.com/forums/facebook.135/",
		"https://forums.digitalpoint.com/forums/twitter.140/",
		"https://forums.digitalpoint.com/forums/google.142/",
		"https://forums.digitalpoint.com/forums/link-development.13/",
		"https://forums.digitalpoint.com/forums/legal-issues.44/",
		"https://forums.digitalpoint.com/forums/domain-names.45/",
		"https://forums.digitalpoint.com/forums/appraisals.61/",
		"https://forums.digitalpoint.com/forums/copywriting.86/",
		"https://forums.digitalpoint.com/forums/copywriting.86/",
		"https://forums.digitalpoint.com/forums/ecommerce.115/",
		"https://forums.digitalpoint.com/forums/pay-per-click-advertising.20/",
		"https://forums.digitalpoint.com/forums/digital-point-ads.138/",
		"https://forums.digitalpoint.com/forums/google-adwords.35/",
		"https://forums.digitalpoint.com/forums/yahoo-search-marketing.84/",
		"https://forums.digitalpoint.com/forums/bing-ads.82/",
		"https://forums.digitalpoint.com/forums/affiliate-programs.22/",
		"https://forums.digitalpoint.com/forums/affiliate-program-management.79/",
		"https://forums.digitalpoint.com/forums/commission-junction.73/",
		"https://forums.digitalpoint.com/forums/google.131/",
		"https://forums.digitalpoint.com/forums/ebay.133/",
		"https://forums.digitalpoint.com/forums/amazon.75/",
		"https://forums.digitalpoint.com/forums/clickbank.87/",
		"https://forums.digitalpoint.com/forums/chitika.74/",
		"https://forums.digitalpoint.com/forums/html-website-design.16/",
		"https://forums.digitalpoint.com/forums/css.39/",
		"https://forums.digitalpoint.com/forums/graphics-multimedia.55/",
		"https://forums.digitalpoint.com/forums/photoshop.121/",
		"https://forums.digitalpoint.com/forums/design.144/",
		"https://forums.digitalpoint.com/forums/content-management.51/",
		"https://forums.digitalpoint.com/forums/blogging.40/",
		"https://forums.digitalpoint.com/forums/drupal.120/",
		"https://forums.digitalpoint.com/forums/joomla.111/",
		"https://forums.digitalpoint.com/forums/xml-rss.78/",
		"https://forums.digitalpoint.com/forums/scripts.9/",
		"https://forums.digitalpoint.com/forums/programming.17/",
		"https://forums.digitalpoint.com/forums/php.37/",
		"https://forums.digitalpoint.com/forums/javascript.38/",
		"https://forums.digitalpoint.com/forums/c.48/",
		"https://forums.digitalpoint.com/forums/ruby.56/",
		"https://forums.digitalpoint.com/forums/databases.57/",
		"https://forums.digitalpoint.com/forums/mysql.108/",
		"https://forums.digitalpoint.com/forums/sites.52/",
		"https://forums.digitalpoint.com/forums/domains.59/",
		"https://forums.digitalpoint.com/forums/design-contests.94/",
		"https://forums.digitalpoint.com/forums/advertising.90/",
		"https://forums.digitalpoint.com/forums/secondhand-licenses.148/",
		"https://forums.digitalpoint.com/forums/services.60/",
		"https://forums.digitalpoint.com/forums/content-creation.102/",
		"https://forums.digitalpoint.com/forums/design.104/",
		"https://forums.digitalpoint.com/forums/programming.103/",
		"https://forums.digitalpoint.com/forums/traffic.99/",
		"https://forums.digitalpoint.com/forums/web-hosting.98/",
		"https://forums.digitalpoint.com/forums/introductions.2/",
		"https://forums.digitalpoint.com/forums/general-chat.19/",
		"https://forums.digitalpoint.com/forums/movies-music-tv.97/",
		"https://forums.digitalpoint.com/forums/games.126/",
		"https://forums.digitalpoint.com/forums/sports.125/",
		"https://forums.digitalpoint.com/forums/hardware.107/",
		"https://forums.digitalpoint.com/forums/politics-religion.80/",
		"https://forums.digitalpoint.com/forums/products-tools.14/",
		"https://forums.digitalpoint.com/forums/keyword-tracker.10/",
		"https://forums.digitalpoint.com/forums/cookie-search.30/",
		"https://forums.digitalpoint.com/forums/better-analytics.31/",
		"https://forums.digitalpoint.com/forums/legacy.41/",
		"https://forums.digitalpoint.com/forums/reviews.91/",
		"https://forums.digitalpoint.com/forums/websites.23/",
		"https://forums.digitalpoint.com/forums/design.144/",
		"https://forums.digitalpoint.com/forums/seo.92/",
		"https://forums.digitalpoint.com/forums/support-feedback.3/",
		"https://forums.digitalpoint.com/forums/138/",
		"https://forums.digitalpoint.com/forums/10/"
        ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//ol[@class='discussionListItems']/li[re:test(@id,'thread-*')]"
	THREAD_LINK_XPATH = ".//h3[@class='title']/a[@class='PreviewTooltip']/@href"
	LAST_PAGE_XPATH = "(//div[@class='PageNav']//a)[last()-1]/@href"
	PREV_XPATH = "//div[@class='PageNav']//a[contains(text(),'< Prev')]/@href"
	POST_XPATH = "//ol[@class='messageList']/li"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":"concat(.//span[@class='DateTime']/@title,.//abbr[@class='DateTime']/text())"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":".//a[@class='username']//text()"
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
			"xpath": "concat(//*[@id='login']/input[2]/@value,'#',./@id)"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"(//span[@class='crumbs']//a[@class='crumb'])[last()]/span/text()"
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
