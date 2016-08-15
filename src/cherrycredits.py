from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "cherrycredits"
	CRAWLER_NAME = "Cherrycredits Crawler"
	LINK_TO_CRAWL = [
		"http://forum.cherrycredits.com/forum/13-sg/",
		"http://forum.cherrycredits.com/forum/14-my/",
		"http://forum.cherrycredits.com/forum/15-ph/",
		"http://forum.cherrycredits.com/forum/16-au/",
		"http://forum.cherrycredits.com/forum/17-th/",
		"http://forum.cherrycredits.com/forum/18-en/",
		"http://forum.cherrycredits.com/forum/88-forum-news/",
		"http://forum.cherrycredits.com/forum/10-the-cherry-cafeteria/",
		"http://forum.cherrycredits.com/forum/177-news-and-updates/",
		"http://forum.cherrycredits.com/forum/178-general-discussion/",
		"http://forum.cherrycredits.com/forum/179-guides-strategies/",
		"http://forum.cherrycredits.com/forum/180-guilds/",
		"http://forum.cherrycredits.com/forum/181-fan-media/",
		"http://forum.cherrycredits.com/forum/182-technical-issues/",
		"http://forum.cherrycredits.com/forum/183-account-issues/",
		"http://forum.cherrycredits.com/forum/184-in-game-bug-report/",
		"http://forum.cherrycredits.com/forum/185-in-game-translations/",
		"http://forum.cherrycredits.com/forum/186-feedback-and-suggestions/",
		"http://forum.cherrycredits.com/forum/156-news-and-updates/",
		"http://forum.cherrycredits.com/forum/157-general-discussion/",
		"http://forum.cherrycredits.com/forum/158-guides-strategies/",
		"http://forum.cherrycredits.com/forum/171-bay-of-fury/",
		"http://forum.cherrycredits.com/forum/172-dark-edge/",
		"http://forum.cherrycredits.com/forum/173-oath-of-dawn/",
		"http://forum.cherrycredits.com/forum/174-azure-lake/",
		"http://forum.cherrycredits.com/forum/159-fan-media/",
		"http://forum.cherrycredits.com/forum/160-technical-issues/",
		"http://forum.cherrycredits.com/forum/161-account-issues/",
		"http://forum.cherrycredits.com/forum/162-in-game-bug-report/",
		"http://forum.cherrycredits.com/forum/163-in-game-translations/",
		"http://forum.cherrycredits.com/forum/165-feedback-and-suggestions/",
		"http://forum.cherrycredits.com/forum/31-news-and-updates/",
		"http://forum.cherrycredits.com/forum/55-official-pvp-tournaments/",
		"http://forum.cherrycredits.com/forum/37-general-discussion/",
		"http://forum.cherrycredits.com/forum/89-guides-strategies/",
		"http://forum.cherrycredits.com/forum/38-archer/",
		"http://forum.cherrycredits.com/forum/39-cleric/",
		"http://forum.cherrycredits.com/forum/40-sorceress/",
		"http://forum.cherrycredits.com/forum/41-warrior/",
		"http://forum.cherrycredits.com/forum/65-academic/",
		"http://forum.cherrycredits.com/forum/101-kali/",
		"http://forum.cherrycredits.com/forum/121-assassin/",
		"http://forum.cherrycredits.com/forum/152-lancea/",
		"http://forum.cherrycredits.com/forum/175-machina/",
		"http://forum.cherrycredits.com/forum/56-colosseum/",
		"http://forum.cherrycredits.com/forum/42-fan-media/",
		"http://forum.cherrycredits.com/forum/109-westwood/",
		"http://forum.cherrycredits.com/forum/110-springwood/",
		"http://forum.cherrycredits.com/forum/111-greenwood/",
		"http://forum.cherrycredits.com/forum/112-holywood/",
		"http://forum.cherrycredits.com/forum/168-blitzwood/",
		"http://forum.cherrycredits.com/forum/169-blitzwood-guilds/",
		"http://forum.cherrycredits.com/forum/50-westwood-central-market/",
		"http://forum.cherrycredits.com/forum/51-springwood-central-market/",
		"http://forum.cherrycredits.com/forum/52-greenwood-central-market/",
		"http://forum.cherrycredits.com/forum/54-holywood-central-market/",
		"http://forum.cherrycredits.com/forum/166-blitzwood-central-market/",
		"http://forum.cherrycredits.com/forum/49-cash-shop/",
		"http://forum.cherrycredits.com/forum/36-technical-issues/",
		"http://forum.cherrycredits.com/forum/44-account-issues/",
		"http://forum.cherrycredits.com/forum/45-in-game-bug-report/",
		"http://forum.cherrycredits.com/forum/46-in-game-translations/",
		"http://forum.cherrycredits.com/forum/47-abuse-report/",
		"http://forum.cherrycredits.com/forum/35-website-issues/",
		"http://forum.cherrycredits.com/forum/48-feedback-and-suggestions/",
		"http://forum.cherrycredits.com/forum/82-archives/",
		"http://forum.cherrycredits.com/forum/32-close-beta-discussion/",
		"http://forum.cherrycredits.com/forum/21-pre-close-beta-discussion/",
		"http://forum.cherrycredits.com/forum/231-tin-t%e1%bb%a9c-s%e1%bb%b1-ki%e1%bb%87n/",
		"http://forum.cherrycredits.com/forum/238-h%c6%b0%e1%bb%9bng-d%e1%ba%abn-chia-s%e1%ba%bb-kinh-nghi%e1%bb%87m/",
		"http://forum.cherrycredits.com/forum/232-h%e1%bb%97-tr%e1%bb%a3-k%e1%bb%b9-thu%e1%ba%adt/",
		"http://forum.cherrycredits.com/forum/233-h%e1%bb%97-tr%e1%bb%a3-v%e1%bb%81-tai-kho%e1%ba%a3n/",
		"http://forum.cherrycredits.com/forum/234-bao-l%e1%bb%97i-trong-game/",
		"http://forum.cherrycredits.com/forum/235-l%e1%bb%97i-d%e1%bb%8bch-thu%e1%ba%adt/",
		"http://forum.cherrycredits.com/forum/236-dong-gop-%e2%80%93-ph%e1%ba%a3n-h%e1%bb%93i/",
		"http://forum.cherrycredits.com/forum/188-news-and-updates/",
		"http://forum.cherrycredits.com/forum/189-general-discussion/",
		"http://forum.cherrycredits.com/forum/195-guides-strategies/",
		"http://forum.cherrycredits.com/forum/197-archer/",
		"http://forum.cherrycredits.com/forum/198-cleric/",
		"http://forum.cherrycredits.com/forum/199-sorceress/",
		"http://forum.cherrycredits.com/forum/200-warrior/",
		"http://forum.cherrycredits.com/forum/201-academic/",
		"http://forum.cherrycredits.com/forum/202-kali/",
		"http://forum.cherrycredits.com/forum/203-assassin/",
		"http://forum.cherrycredits.com/forum/204-lancer/",
		"http://forum.cherrycredits.com/forum/205-machina/",
		"http://forum.cherrycredits.com/forum/206-colosseum/",
		"http://forum.cherrycredits.com/forum/207-fan-media/",
		"http://forum.cherrycredits.com/forum/208-party-recruitment/",
		"http://forum.cherrycredits.com/forum/209-guilds/",
		"http://forum.cherrycredits.com/forum/227-buying/",
		"http://forum.cherrycredits.com/forum/228-selling/",
		"http://forum.cherrycredits.com/forum/229-shop/",
		"http://forum.cherrycredits.com/forum/211-cash-shop/",
		"http://forum.cherrycredits.com/forum/212-technical-issues/",
		"http://forum.cherrycredits.com/forum/213-account-issues/",
		"http://forum.cherrycredits.com/forum/214-in-game-bug-report/",
		"http://forum.cherrycredits.com/forum/215-in-game-translations/",
		"http://forum.cherrycredits.com/forum/216-abuse-report/",
		"http://forum.cherrycredits.com/forum/217-website-issues/",
		"http://forum.cherrycredits.com/forum/218-feedback-and-suggestions/",
		"http://forum.cherrycredits.com/forum/191-neuigkeitenevents/",
		"http://forum.cherrycredits.com/forum/219-allgemeine-spieldiskussionen/",
		"http://forum.cherrycredits.com/forum/220-hilfe/",
		"http://forum.cherrycredits.com/forum/221-technische-probleme/",
		"http://forum.cherrycredits.com/forum/222-sonstiges/",
		"http://forum.cherrycredits.com/forum/194-newsevents/",
		"http://forum.cherrycredits.com/forum/223-discussions-generales/",
		"http://forum.cherrycredits.com/forum/224-aide/",
		"http://forum.cherrycredits.com/forum/226-off-topics/",
		"http://forum.cherrycredits.com/forum/93-news-and-updates/",
		"http://forum.cherrycredits.com/forum/94-general-discussion/",
		"http://forum.cherrycredits.com/forum/95-tactics-anthem-fan-submissions/",
		"http://forum.cherrycredits.com/forum/96-bug-report/",
		"http://forum.cherrycredits.com/forum/97-feedback-and-suggestions/",
		"http://forum.cherrycredits.com/forum/225-problemes-techniques/",
        ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//div[@class='ipsBox_container']//a[@itemprop='url']"
	THREAD_LINK_XPATH = "./@href"
	LAST_PAGE_XPATH = "(//div[@class='pagination clearfix left ']//a[not(contains(text(),'Next'))])[last()]/@href"
	PREV_XPATH = "//div[@class='pagination clearfix left ']//li[@class='page active']/preceding-sibling::li[1]/a/@href"
	POST_XPATH = "//div[re:test(@id,'post_id_*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": True,
			"xpath":".//abbr[@itemprop='commentTime']/text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath": ".//span[@class='author vcard']/text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='post entry-content ']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//a[@itemprop='replyToUrl']/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"(//div[@id='secondary_navigation']//li)[last()]/a//text()"
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
