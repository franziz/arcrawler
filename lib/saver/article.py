from curtsies import fmtstr
import pymongo
import bson.json_util

class ArticleSaver:
	def __init__(self):
		pass

	def save(self, article=None):
		assert article is not None, "article is not defined."

		conn = pymongo.MongoClient("mongodb://220.100.163.132/news_crawler")
		db   = conn["news_crawler"]

		# Ensuring index		
		db.data.create_index([("permalink", pymongo.ASCENDING)], unique=True, background=True)
		db.data.create_index([("converted", pymongo.ASCENDING)], background=True)
		db.data.create_index("TTL",expireAfterSeconds=2592000, background=True)

		try:
			db.data.insert_one(article)
			print(fmtstr("[ArticleSaver][success] Inserted One Document!"))
		except pymongo.errors.DuplicateKeyError:
			print(fmtstr("[ArticleSaver][error] Duplicate Document!","red"))
		finally:
			conn.close()