import pymongo

class Database:
	MONITOR = 0

	def __init__(self):
		pass

	@classmethod
	def get_db(self, database_name=None):
		assert database_name is not None, "database_name is not defined."

		db = pymongo.MongoClient("mongodb://mongo:27017")
		if database_name == Database.MONITOR:
			db = db["monitor"]
		return db