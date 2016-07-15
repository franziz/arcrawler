from lib          import tools
from pymongo      import MongoClient
from tqdm         import tqdm
from urllib.parse import urlparse
import pymongo

db   = MongoClient("mongodb://220.100.163.132:27017/test")
db   = db.tsikot
pbar = db.data.find()
for document in pbar:
	before = document["permalink"]
	domain = urlparse(before)
	domain = "{}://{}".format(domain.scheme, domain.netloc)
	after  = tools._expand_link(domain, before)
	_id    = document["_id"]
	try:
		if after != before:
			db.data.update_one({"_id":_id},{"$set":{"permalink":after}})
			print("[{}] Updated!".format(_id))
		else:
			print("[{}] Nothing wrong!".format(_id))
	except pymongo.errors.DuplicateKeyError:
		db.data.delete_one({"_id":_id})
		print("[{}] Deleted!".format(_id))



# from lib.news_engine.engine import Engine
# from lib.network_tools      import NetworkTools
# import bson.json_util

# news                      = Engine()
# news.network_tools        = NetworkTools(use_proxy=False)
# news.url                  = "http://www.otosia.com/"
# news.title_xpath          = "//h1[@class='OtoDetailT']/text()"
# news.author_name_xpath    = "concat('otosia','')"
# news.content_xpath        = "//div[@class='OtoDetailNews']//p/text()"
# news.published_date_xpath = "//h1[@class='OtoDetailT']/following-sibling::span[1]/text()"
# news.parse()
# news.extract()
# print(bson.json_util.dumps(news.articles[0].to_dict(), indent=4, separators=(",",":")))

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