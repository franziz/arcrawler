from curtsies import fmtstr
import pymongo
import bson.json_util
import re
import arrow

class ArticleSaver:
	def __init__(self):
		pass

	def save(self, article=None):
		assert article is not None, "article is not defined."

		monitor_conn = pymongo.MongoClient("mongodb://mongo:27017/monitor")
		monitor_db   = monitor_conn["monitor"]

		conn = pymongo.MongoClient("mongodb://mongo:27017/news_crawler")
		db   = conn["news_crawler"]

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
			print(fmtstr("[ArticleSaver][success] Inserted One Document!"))
		except pymongo.errors.DuplicateKeyError:
			print(fmtstr("[ArticleSaver][error] Duplicate Document!","red"))
		finally:
			conn.close()
			monitor_conn.close()