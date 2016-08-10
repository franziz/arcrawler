from pymongo import MongoClient
import arrow

class Monitor(object):
	def __init__(self):
		pass

	def _connect_to_database(self):
		db = MongoClient("mongodb://mongo:27017/test")
		db = db.monitor
		return db

	def current_queue(self):
		db     = self._connect_to_database()
		queue  = db.queue.find()
		result = []
		for document in queue:
			new_document = Document()
			new_document.from_dict(document)
			result.append(new_document)
		return result

	def renew_queue(self, new_documents=[]):
		""" This function will renew monitor.queue database by removing the documents
			that are not inside new_documents parameter. 

			Example:
			old_documents = [{1:"abc"}, {2:"def"}, {3:"ghi"}]
			new_documents = [{1:"aaa"}, {4:"axz"}]
			result        = [{1:"aaa"}, {4:"axz"}]
		"""
		for new_document in new_documents:
			

	def _set_status(self, crawler=None, status=None):
		assert status        is not None, "status is not defined."
		assert crawler       is not None, "crawler is not defined."
		assert type(crawler) is Document, "incorrect crawler data type."

		db = self._connect_to_database()
		current_time = arrow.utcnow().datetime
		db.queue.update_one({"hash":crawler.HASH}, {"$set":{
			"last_update" : current_time,
				 "status" : status
		}})
		crawler.LAST_UPDATE = current_time
		crawler.STATUS      = status
		return crawler

	def set_as_idle(self, crawler=None):
		assert crawler       is not None, "crawler is not defined."
		assert type(crawler) is Document, "incorrect crawler data type."
		self._set_status(crawler, status.IDLE)

	def set_as_processing(self, crawler=None):
		assert crawler       is not None, "crawler is not defined."
		assert type(crawler) is Document, "incorrect crawler data type."
		self._set_status(crawler, status.PROCESSING)

	def set_as_processed(self, crawler=None):
		assert crawler 		 is not None, "crawler is not defined."
		assert type(crawler) is Document, "incorrect crawler data type."
		self._set_status(crawler, status.PROCESSED)

class Status(object):
	IDLE       = "idle"
	PROCESSING = "processing"
	PROCESSED  = "processed"

class Document(object):
	def __init__(self):
		self.HASH              = None
		self.LINK              = None
		self.NAME              = None
		self.DB_TO_INSERT      = None
		self.DB_NAME_TO_INSERT = None
		self.COUNTRY           = None
		self.LAST_UPDATE       = None
		self.STATUS            = None

	def from_dict(self, source=None):
		self.HASH              = source["hash"]
		self.LINK              = source["link"]
		self.DB_TO_INSERT      = source["db_to_insert"]
		self.DB_NAME_TO_INSERT = source["db_name_to_insert"]
		self.COUNTRY           = source["country"]
		self.LAST_UPDATE       = source["last_update"]
		self.STATUS            = source["status"]