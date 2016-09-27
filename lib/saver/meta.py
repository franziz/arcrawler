import pymongo

class MetaSaver:
	def __init__(self):
		pass

	def save(self, document=None):
		assert document is not None, "document is not defined."

		conn = pymongo.MongoClient("mongodb://220.100.163.132/monitor")
		db   = conn["monitor"]

		db.crawlers_meta.create_index([("name",pymongo.ASCENDING)], unique=True)
		db.crawlers_meta.update({"name":document["name"]},{"$set":document},upsert=True)
		conn.close()