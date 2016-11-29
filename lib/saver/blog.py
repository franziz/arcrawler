from curtsies import fmtstr
import pymongo
import bson.json_util
import re
import arrow

class BlogSaver:
	def __init__(self, **kwargs):
		self.db_address = kwargs.get("db_address", "mongo:27017")
		self.db_name    = kwargs.get("db_name", "news_crawler")

	def save(self, article=None):
		""" Exceptions:
			-  AssertionError
		"""
		assert article is not None, "article is not defined."
		
		monitor_conn = pymongo.MongoClient("mongodb://mongo:27017/monitor")
		monitor_db   = monitor_conn["monitor"]

		conn = pymongo.MongoClient("mongodb://mongo:27017/blog_crawler")
		db   = conn["blog_crawler"]

		# Ensuring index		
		db.data.create_index([("permalink", pymongo.ASCENDING)], unique=True, background=True)
		db.data.create_index([("converted", pymongo.ASCENDING)], background=True)
		db.data.create_index("TTL",expireAfterSeconds=2592000, background=True)

		try:
			db.data.insert_one(article)
			monitor_db.status.update(
				{"crawler_name": re.compile(article["_crawled_by"], re.IGNORECASE)},
				{"$set":{
					"crawler_name": article["_crawled_by"].title(),
					"last_insert_time": arrow.utcnow().datetime
				}},
				upsert=True
			)
			print(fmtstr("[BlogSaver][success] Inserted One Document!"))
		except pymongo.errors.DuplicateKeyError:
			print(fmtstr("[BlogSaver][error] Duplicate Document!","red"))
		finally:
			conn.close()
			monitor_conn.close()