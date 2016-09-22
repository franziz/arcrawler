from ..exceptions import DuplicateKeyError
import pymongo

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
		finally:
			connection.close()