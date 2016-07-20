# from lib          import tools
# from pymongo      import MongoClient
# from tqdm         import tqdm
# from urllib.parse import urlparse
# import pymongo

# db   = MongoClient("mongodb://220.100.163.132:27017/test")
# db   = db.tsikot
# pbar = db.data.find()
# for document in pbar:
# 	before = document["permalink"]
# 	domain = urlparse(before)
# 	domain = "{}://{}".format(domain.scheme, domain.netloc)
# 	after  = tools._expand_link(domain, before)
# 	_id    = document["_id"]
# 	try:
# 		if after != before:
# 			db.data.update_one({"_id":_id},{"$set":{"permalink":after}})
# 			print("[{}] Updated!".format(_id))
# 		else:
# 			print("[{}] Nothing wrong!".format(_id))
# 	except pymongo.errors.DuplicateKeyError:
# 		db.data.delete_one({"_id":_id})
# 		print("[{}] Deleted!".format(_id))



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

import dateparser
from lib.network_tools import NetworkTools
from lib import tools

# https://www.serayamotor.com/diskusi/./viewtopic.php?f=13&t=23033&
# https://www.serayamotor.com/diskusi/./viewtopic.php?f=13&t=21495&
# https://www.serayamotor.com/diskusi/./viewtopic.php?f=13&t=16492&
# https://www.serayamotor.com/diskusi/./viewtopic.php?f=13&t=23223&
# https://www.serayamotor.com/diskusi/./viewtopic.php?f=13&t=6694&
# https://www.serayamotor.com/diskusi/./viewtopic.php?f=13&t=13243&
# https://www.serayamotor.com/diskusi/./viewtopic.php?f=13&t=4156&
# https://www.serayamotor.com/diskusi/./viewtopic.php?f=13&t=4030&
# https://www.serayamotor.com/diskusi/./viewtopic.php?f=13&t=23710&
# https://www.serayamotor.com/diskusi/./viewtopic.php?f=13&t=23630&
# https://www.serayamotor.com/diskusi/./viewtopic.php?f=13&t=23074&
# https://www.serayamotor.com/diskusi/./viewtopic.php?f=13&t=23091&
# https://www.serayamotor.com/diskusi/./viewtopic.php?f=13&t=22915&
# https://www.serayamotor.com/diskusi/./viewtopic.php?f=13&t=22181&
# https://www.serayamotor.com/diskusi/./viewtopic.php?f=13&t=22057&
# https://www.serayamotor.com/diskusi/./viewtopic.php?f=13&t=21848&
# https://www.serayamotor.com/diskusi/./viewtopic.php?f=13&t=21761&
# https://www.serayamotor.com/diskusi/./viewtopic.php?f=13&t=21639&
# https://www.serayamotor.com/diskusi/./viewtopic.php?f=13&t=21505&
# https://www.serayamotor.com/diskusi/./viewtopic.php?f=13&t=21517&
# https://www.serayamotor.com/diskusi/./viewtopic.php?f=13&t=15644&
# https://www.serayamotor.com/diskusi/./viewtopic.php?f=13&t=21462&
# https://www.serayamotor.com/diskusi/./viewtopic.php?f=13&t=21291&
# https://www.serayamotor.com/diskusi/./viewtopic.php?f=64&t=21096&
# https://www.serayamotor.com/diskusi/./viewtopic.php?f=13&t=20478&
# https://www.serayamotor.com/diskusi/./viewtopic.php?f=13&t=20077&
# https://www.serayamotor.com/diskusi/./viewtopic.php?f=13&t=20047&
# https://www.serayamotor.com/diskusi/./viewtopic.php?f=13&t=19864&

net = NetworkTools(use_proxy=False)
page = net.parse("https://www.serayamotor.com/diskusi/viewtopic.php?f=13&t=21495&")
posts = tools._xpath(page,"concat('diskusi/',(//div[@class='pagination']//ul//li[not(contains(@class,'next'))]//a)[last()]//@href)")
print(posts)
# for post in posts:
# 	hasil = "".join(tools._xpath(post,".//strong/a[re:test(@class,'username*')]//text()"))
# 	hasil = tools._clean_string(hasil)
# 	# print(tools._expand_link("https://www.serayamotor.com/",hasil))
# 	# print(tools._date_parser(hasil))
# 	print(hasil.encode("utf-8"))
# 	# print(dateparser.parse(hasil))

# import dateparser
# import ftfy

# hasil = ftfy.fix_encoding("sunday, 10 july 2016 12:15")
# print(dateparser.parse(hasil))

# from lib import tools
# permalink = "https://www.tsikot.com/forums/racing-off-roading-fun-run-talk-16/drag-racing-greenhills-100896-post2732035/?s=56ebd1ce7f2b93afc88ddeed9e6d73fe#post2732035"
# # permalink = "http://gearheads.in/showthread.php?22007-Clutch-Slipping&s=ccbb7628f2b5c1068f70d44453890fd4&p=445873&viewfull=1#post445873"
# print(tools._expand_link("http://gearheads.in", permalink))