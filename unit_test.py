from lib.news_engine.engine import Engine
import bson.json_util

news             = Engine()
news.country     = "IDN"
news.source_type = "news"
news.url         = "http://www.otosia.com/"
news.parse()
for article in news.articles:
	article.title_xpath          = "//h1[@class='OtoDetailT']/text()"
	article.author_xpath         = "concat('otosia','')"
	article.content_xpath        = "//div[@class='OtoDetailNews']//p/text()"
	article.published_date_xpath = "//h1[@class='OtoDetailT']/following-sibling::span[1]/text()"
	article.extract()	
print(bson.json_util.dumps(news.articles[0].to_dict(), indent=4, separators=(",",":")))


# import dateparser
# from lib.network_tools import NetworkTools
# from lib import tools

# net = NetworkTools(use_proxy=False)
# page = net.parse("https://www.otosaigon.com/threads/trai-nghiem-dau-phat-cao-cap-pioneer-avh-x8750bt-tai-viet-nam.8682827/page-2")
# posts = tools._xpath(page,"//ol[@id='messageList']//li[re:test(@id,'post-*')]")
# print(len(posts))
# for post in posts:
# 	hasil = "".join(tools._xpath(post,".//span[@class='DateTime']/@title"))
# 	hasil = tools._clean_string(hasil)
# 	print(hasil.encode("utf-8"))
# 	print(dateparser.parse(hasil))

# import dateparser
# import ftfy

# hasil = ftfy.fix_encoding("sunday, 10 july 2016 12:15")
# print(dateparser.parse(hasil))

# from lib import tools
# permalink = "https://www.tsikot.com/forums/racing-off-roading-fun-run-talk-16/drag-racing-greenhills-100896-post2732035/?s=56ebd1ce7f2b93afc88ddeed9e6d73fe#post2732035"
# # permalink = "http://gearheads.in/showthread.php?22007-Clutch-Slipping&s=ccbb7628f2b5c1068f70d44453890fd4&p=445873&viewfull=1#post445873"
# print(tools._expand_link("http://gearheads.in", permalink))