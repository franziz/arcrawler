from ..exceptions import DuplicateKeyError, SaveError
from ..monitor    import Monitor
from curtsies     import fmtstr
import pymongo
import bson.errors
import logging
import arrow
import re

class PostSaver:
	def __init__(self, **kwargs):
		self.logger     = logging.getLogger(__name__)
		self.db_address = kwargs.get("db_address",None)
		self.db_name    = kwargs.get("db_name",None)

	def save(self,document=None):
		""" Exceptions:
			- AssertionError (Monitor)
			- CannotFindField (Monitor)
			- ValidationError (Monitor)
			- DuplicateKeyError
			- SaveError
		"""
		assert self.db_address          is not None, "db_address is not defined."
		assert self.db_name 		    is not None, "db_name is not defined."
		assert "permalink"              in document, "permalink is not defined."
		assert "content"                in document, "content is not defined."
		assert len(document["content"]) > 0        , "content cannot be empty."

		monitor = Monitor()

		conn = pymongo.MongoClient("mongodb://%s" % self.db_address)
		db   = conn[self.db_name]

		# Ensuring Index
		db.data.create_index([("permalink", pymongo.ASCENDING)], unique=True)
		db.data.create_index([("converted", pymongo.ASCENDING)])
		db.data.create_index("TTL",expireAfterSeconds=2592000)

		try:
			db.data.insert_one(document)
			monitor.capture_insert_document(crawler_name=document["_crawled_by"])
		except pymongo.errors.DuplicateKeyError:
			raise DuplicateKeyError("Ops! Duplciate Data!")
		except bson.errors.InvalidBSON:
			raise SaveError("Invalid BSON. Cannot save data!")
		finally:
			conn.close()
			# monitor_conn.close()

	def batch_save(self, documents=None):
		""" Exceptions:
			- AssertionError (save)
			- CannotFindField (save)
			- ValidationError (save)

			Return:
			success<bool> : Indicate if all the documents is success or not
		"""
		assert documents is not None, "documents is not defined."
		
		success = True
		try:
			for document in documents:
				try:
					self.save(document)
					print(fmtstr("[PostSaver][success] Inserted One Document!","green"))
				except SaveError as ex:
					self.logger.error(str(ex), exc_info=True)
					print(fmtstr("[PostSaver][error] %s" % ex, "red"))
			success = True
		except DuplicateKeyError as ex:
			# Just do not try to push any more document if you find any DuplicateKeyError
			print(fmtstr("[PostSaver][debug] %s" % ex,"red"))
			success =  False
		return success