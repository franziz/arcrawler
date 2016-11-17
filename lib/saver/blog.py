from curtsies import fmtstr
import pymongo
import bson.json_util

class BlogSaver:
	def __init__(self, **kwargs):
		self.db_address = kwargs.get("db_address", "mongo:27017")
		self.db_name    = kwargs.get("db_name", "news_crawler")

	def save(self, article=None):
		""" Exceptions:
			-  AssertionError
		"""
		assert article is not None, "article is not defined."

		conn = pymongo.MongoClient("mongodb://%s/%s" % (self.db_address, self.db_name))
		db   = conn[self.db_name]

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