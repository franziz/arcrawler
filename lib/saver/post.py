from ..exceptions import DuplicateKeyError, SaveError
from curtsies     import fmtstr
import pymongo
import bson.errors

class PostSaver:
	def __init__(self, **kwargs):
		self.db_address = kwargs.get("db_address",None)
		self.db_name    = kwargs.get("db_name",None)

	def save(self,document=None):
		assert "permalink"              in document, "permalink is not defined."
		assert "content"                in document, "content is not defined."
		assert len(document["content"]) > 0        , "content cannot be empty."

		connection = pymongo.MongoClient("mongodb://%s" % self.db_address)
		db         = connection[self.db_name]

		# Ensuring Index
		db.data.create_index([("permalink", pymongo.ASCENDING)], unique=True)
		db.data.create_index([("converted", pymongo.ASCENDING)])
		db.data.create_index("TTL",expireAfterSeconds=2592000)

		try:
			db.data.insert_one(document)
		except pymongo.errors.DuplicateKeyError:
			raise DuplicateKeyError("Ops! Duplciate Data!")
		except bson.errors.InvalidBSON:
			raise SaveError("Invalid BSON. Cannot save data!")
		finally:
			connection.close()

	def batch_save(self, documents=None):
		""" Return:
			success<bool> : Indicate if all the documents is success or not
		"""
		assert documents is not None, "documents is not defined."
		
		success = True
		try:
			for document in documents:
				self.save(document)
				print(fmtstr("[PostSaver][success] Inserted One Document!","green"))
			success = True
		except DuplicateKeyError as ex:
			# Just do not try to push any more document if you find any DuplicateKeyError
			print(fmtstr("[PostSaver][debug] %s" % ex,"red"))
			success =  False
		except AssertionError as ex:
			print(fmtstr("[PostSaver][error] Assertion is not passed!","red"))
			success =  False
		except SaveError as ex:
			print(fmtstr("[PostSaver][error] %s" % ex, "red"))
			success = False
		return success