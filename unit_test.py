# import pymongo
# import bson.json_util
# import arrow

# if __name__ == "__main__":
# 	db = pymongo.MongoClient("mongodb://220.100.163.132")
# 	db = db["kaskus"]
# 	documents = db.data.find({}).sort([("$natural",-1)]).limit(1)

# 	for document in documents:
# 		print(bson.json_util.dumps(document, indent=4))
# from lib.engine.converter import ConverterEngine

# if __name__ == "__main__":
# 	engine = ConverterEngine()
# 	engine.convert(crawlers={
# 		"Kaskus Crawler": {
#             "db_name": "kaskus",
#             "db_address": "mongo:27017"
#      	}
#      })
# from lib.builder         import Builder
# from lib.builder.section import Section

# def callback(message=None):
# 	print(message)

# if __name__ == "__main__":
# 	section = Section(
# 		name = "high_priority_section_1",
# 		items = ["Kaskus Crawler"],
# 		workers = 13
# 	)
# 	Builder.build(section,callback)

# from lib.network_tools import NetworkTools
# from lib.engine.forum  import ForumEngine
# from lib.factory.saver import SaverFactory

# class Crawler:
# 	def __init__(self):
# 		pass

# 	def crawl(self):
# 		saver            = SaverFactory.get_saver(SaverFactory.POST)
# 		saver.db_address = "mongo:27017"
# 		saver.db_name    = "kaskus"
		
# 		engine = ForumEngine(
# 			             name = "Kaskus Crawler",
# 			    network_tools = NetworkTools(use_proxy=True),
# 			    link_to_crawl = "http://www.kaskus.co.id/forum/136/feedback-amp-testimonial",
# 			          country = "IDN",
# 			     thread_xpath = "//tr[re:test(@id,'thread*')]",
# 			thread_link_xpath = ".//a[re:test(@class,'link_thread_title*')]/@href",
# 			  last_page_xpath = "//a[@class='tooltips last-page']/@href",
# 			       prev_xpath = "//a[@class='tooltips previous-page']/@href",
# 			       post_xpath = "//div[@class='row nor-post']",
# 			           fields = [{'published_date': {'xpath': ".//time[@class='entry-date']/@datetime", 'concat': False, 'data_type': 'date', 'single': True}}, {'permalink': {'xpath': ".//div[@class='permalink']/a/@href", 'concat': False, 'data_type': 'url', 'single': True}}, {'author_name': {'xpath': ".//span[@itemprop='name']//text()", 'concat': False, 'data_type': 'string', 'single': True}}, {'author_id': {'xpath': ".//div[@class='user-name']/@data-userid", 'concat': False, 'data_type': 'string', 'single': True}}, {'content': {'xpath': ".//div[@class='entry']//text()", 'concat': True, 'data_type': 'string', 'single': True}}, {'title': {'xpath': "//div[@class='current']/text()", 'concat': False, 'data_type': 'string', 'single': True}}]
# 		)
# 		engine.crawl(saver=saver)

# if __name__ == "__main__":
# 	crawler = Crawler()
# 	crawler.crawl()

# from lib.factory.parser import ParserFactory

# if __name__ == "__main__":
# 	parser  = ParserFactory.get_parser(ParserFactory.THREAD_XPATH)
# 	threads = parser.parse(
# 		 link = "http://www.kaskus.co.id/forum/21/?ref=postlist-21&med=header_link",
# 		xpath = "//tr[re:test(@id,'thread*')]"
# 	)
# 	print(len(threads))


# from lib.factory.parser import ParserFactory

# if __name__ == "__main__":
# 	parser = ParserFactory.get_parser(ParserFactory.DATE)
# 	date   = parser.parse("2016-09-10 12:12:00")
# 	print("%s" % date)

# import pymongo
# import arrow
# import tomorrow
# from tqdm import tqdm

# @tomorrow.threads(10)
# def convert(document):
#     mention_created_date = arrow.get(document["MentionCreatedDateISO"])
#     mention_created_date = mention_created_date.replace(hours=8)
#     document.update({"MentionCreatedDate":mention_created_date.format("YYYY-MM-DD HH:mm:ss")})
#     document.update({"MentionCreatedDateISO":"%sZ" % mention_created_date.format("YYYY-MM-DDTHH:mm:ss")})
#     print("Converted %s" % document["_id"])
#     db.mention.update({"_id":document["_id"]},{"$set":{"MentionCreatedDateISO":document["MentionCreatedDateISO"],"MentionCreatedDate":document["MentionCreatedDate"]}})
#     print("Saved %s" % document["_id"])

# if __name__ == "__main__":
# 	global db
# 	db = pymongo.MongoClient("mongodb://alex:07081984@220.100.163.138/isid?authSource=admin")
# 	db = db["isid"]

# 	thr = arrow.now().replace(days=-1)
# 	thr = thr.format("YYYY-MM-DDTHH:mm:ss")
# 	thr = "%sZ" % thr
# 	documents = db.mention.find({"SourceName":"Kaskus.co.id","DateInsertedIntoCrawlerDBISO":{"$gte":thr}})
# 	print(documents.count())
# 	documents = [convert(document) for document in documents]
	


# import time
# import requests

# from tomorrow import threads

# @threads(5)
# def download(url):
# 	return requests.get(url)

# if __name__ == "__main__":
# 	urls = [
# 	    'http://google.com',
# 	    'http://facebook.com',
# 	    'http://youtube.com',
# 	    'http://baidu.com',
# 	    'http://yahoo.com',
# 	]
# 	start = time.time()
# 	responses = [download(url) for url in urls]
# 	html = [response.text for response in responses]
# 	end = time.time()
# 	print("Time: %f seconds" % (end - start))

# from lib.config.factory import ConfigFactory
# import pymongo
# import glob
# import os
# import importlib

# if __name__ == "__main__":
# 	target = "section_8"
# 	source_files = []
# 	crawlers     = {}
# 	for file_name in glob.iglob(os.path.join(os.getcwd(), "src", "*.py")):
# 		file_name = file_name.replace(os.getcwd(),"")
# 		file_name = file_name.replace("src","")
# 		file_name = file_name.replace(".py","")
# 		file_name = file_name.replace("/","")
# 		module    = importlib.import_module("src.%s" % file_name)
# 		crawler   = module.Crawler()
# 		crawlers.update({crawler.CRAWLER_NAME:crawler})

# 	run_config = ConfigFactory.get(ConfigFactory.RUN)
# 	sections   = run_config.get("sections")
# 	for crawler_name in sections[target]:
# 		print("Dropping %s" % crawler_name.title())
# 		db = pymongo.MongoClient("mongodb://220.100.163.132")
# 		db = db[crawlers[crawler_name].DB_SERVER_NAME]
# 		db.data.drop()

# 	db = pymongo.MongoClient("mongodb://220.100.163.132")
# 	db = db["monitor"]
# 	for crawler_name in sections[target]:
# 		result = db.inserted_document.delete_many({"crawler_name":crawler_name.title()})
# 		print("Removed %s document(s) from %s" % (result.deleted_count, crawler_name.title()))

# from lib.builder import Builder

# def callback(message=None):
# 	print(message)

# if __name__ == "__main__":
# 	Builder.build(
# 		 name = "low_priority_section_1",
# 		items = [
# 			"9carthai Crawler",
# 			"Aoindonesia Crawler",
# 			"cartalk crawler",
# 			"hardwarezone crawler",
# 			"Hiluxtigerclub Crawler",
# 			"hiphopindo crawler",
# 			"Hondanonclub Crawler",
# 			"huahinforum crawler",
# 			"Koratnana Crawler",
# 			"Koratsound Crawler",
# 			"Livingincebuforums Crawler",
# 			"Lolgarena Crawler",
# 			"medlly crawler",
# 			"meraforum crawler",
# 			"suzuki-forums crawler",
# 			"world-a-team crawler",
# 			"worldofdth crawler",
# 			"worldofdth crawler",
# 			"Xdtalk Crawler",
# 			"Yamahat135 Crawler",
# 			"Avanzaxenia Crawler"
# 		],
# 		log_callback=callback
# 	)
# from lib 			   import tools
# from lib.network_tools import NetworkTools
# import bson.json_util
# import lxml

# if __name__ == "__main__":
# 	net = NetworkTools(use_proxy=False)
# 	page = net.parse("http://www.autos.ca/forum/index.php?board=67.0", parse=False)
# 	print(u"%s" % page.encode("utf-8"))
# 	# page  = net.parse("https://www.otofun.net/threads/tiep-tuc-do-1-em-m3.395948/page-10")
# 	# posts = tools._xpath(page, "//li[re:test(@id,'post-*')]")
# 	# print(len(posts))
# 	# # print(posts)
# 	# for post in posts:		
# 	# 	str_date = tools._xpath(post, "concat(concat('20',substring-before(substring-after(substring-after(translate(.//div[@class='messageHead']//text(),'lúc',''),'/'),'/'),' ')),'/',substring-before(substring-after(translate(.//div[@class='messageHead']//text(),'lúc',''),'/'),'/'),'/',substring-before(translate(.//div[@class='messageHead']//text(),'lúc',''),'/'),' ',	substring-after(substring-after(substring-after(translate(.//div[@class='messageHead']//text(),'lúc',''),'/'),'/'),' '))")
# 	# 	if type(str_date) is list:
# 	# 		str_date = "".join(str_date)
# 	# 	if str_date is None: print(b"")
# 	# 	else: print(str_date.encode("utf-8"))
# 	# 	str_date = tools._clean_string(str_date)
# 	# 	str_date = tools._date_parser(str_date)
# 	# 	print(bson.json_util.dumps({"date":str_date}))
# # from lib          import tools
# # from pymongo      import MongoClient
# # from tqdm         import tqdm
# # from urllib.parse import urlparse
# # import pymongo

# # db   = MongoClient("mongodb://220.100.163.132:27017/test")
# # db   = db.tsikot
# # pbar = db.data.find()
# # for document in pbar:
# # 	before = document["permalink"]
# # 	domain = urlparse(before)
# # 	domain = "{}://{}".format(domain.scheme, domain.netloc)
# # 	after  = tools._expand_link(domain, before)
# # 	_id    = document["_id"]
# # 	try:
# # 		if after != before:
# # 			db.data.update_one({"_id":_id},{"$set":{"permalink":after}})
# # 			print("[{}] Updated!".format(_id))
# # 		else:
# # 			print("[{}] Nothing wrong!".format(_id))
# # 	except pymongo.errors.DuplicateKeyError:
# # 		db.data.delete_one({"_id":_id})
# # 		print("[{}] Deleted!".format(_id))



# # from lib.news_engine.engine import Engine
# # from lib.network_tools      import NetworkTools
# # import bson.json_util

# # net = NetworkTools(use_proxy=False)
# # page = net.parse("http://httpbin.org/get")
# # posts = tools._xpath(page,"//ol[@id='messageList']//li[re:test(@id,'post-*')]")
# # print(len(posts))
# # for post in posts:
# # 	hasil = "".join(tools._xpath(post,".//div[re:test(@id,'subject_*')]/following-sibling::div[1]/text()"))
# # 	hasil = tools._clean_string(hasil)
# # 	# print(tools._expand_link("https://www.serayamotor.com/",hasil))
# # 	# print(tools._date_parser(hasil))
# # 	print(hasil.encode("utf-8"))
# # 	print(dateparser.parse(hasil))

# # import dateparser
# # import ftfy

# # hasil = ftfy.fix_encoding("sunday, 10 july 2016 12:15")
# # print(dateparser.parse(hasil))

# # from lib import tools
# # permalink = "https://www.tsikot.com/forums/racing-off-roading-fun-run-talk-16/drag-racing-greenhills-100896-post2732035/?s=56ebd1ce7f2b93afc88ddeed9e6d73fe#post2732035"
# # # permalink = "http://gearheads.in/showthread.php?22007-Clutch-Slipping&s=ccbb7628f2b5c1068f70d44453890fd4&p=445873&viewfull=1#post445873"
# # print(tools._expand_link("http://gearheads.in", permalink))