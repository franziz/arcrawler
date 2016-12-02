# from ..database import Database
from ..factory.config    import ConfigFactory
from ..factory.validator import ValidatorFactory
import re
import pymongo
import arrow

class Monitor:
	def __init__(self):
		""" Exceptions:
			- AssertionError (ConfigFactory, ValidatorFactory, MonitorConfig.get, MonitorConfigValidator.validate)
			- CannotFindField (MonitorConfig.get, MonitorConfigValidator.validate)
			- ValidationError (MonitorConfigValidator.validate)
		"""
		self.config = ConfigFactory.get_config(ConfigFactory.MONITOR)

		validator = ValidatorFactory.get_validator(ValidatorFactory.MONITOR_CONFIG)
		validator.validate(self.config)
		self.config = self.config.get("monitor")
	
	def capture_insert_document(self, crawler_name=None):
		""" Exceptions:
			- AssertionError
		"""
		assert crawler_name is not None, "crawler_name is not defined."
		assert self.config  is not None, "config is not defined."

		conn = pymongo.MongoClient("mongodb://%s:%s/%s" % (
			self.config["ip"],
			self.config["port"],
			self.config["database"]
		))
		db = conn[self.config["database"]]
		db.status.update(
			{"crawler_name": re.compile(crawler_name, re.IGNORECASE)},
			{"$set":{
				"crawler_name": crawler_name.title(),
				"last_insert_time": arrow.utcnow().datetime
			}},
			upsert=True
		)
		conn.close()

	def capture_section_start(self, section_name=None):
		""" Exceptions:
			- AssertionError
		"""
		assert section_name is not None, "section_name is not defined."
		assert self.config  is not None, "config is not defined."

		conn = pymongo.MongoClient("mongodb://%s:%s/%s" % (
			self.config["ip"],
			self.config["port"],
			self.config["database"]
		))
		db = conn[self.config["database"]]
		db.section.update(
			{"section_name": re.compile(section_name, re.IGNORECASE)},
			{"$set":{
				"section_name": section_name.title(),
				"start_time": arrow.utcnow().datetime
			}}
		)
		conn.close()

	def capture_section_stop(self, section_name=None):
		""" Exceptions:
			- AssertionError
		"""
		assert section_name is not None, "section_name is not defined."
		assert self.config  is not None, "config is not defined."

		conn = pymongo.MongoClient("mongodb://%s:%s/%s" % (
			self.config["ip"],
			self.config["port"],
			self.config["database"]
		))
		db = conn[self.config["database"]]
		db.section.update(
			{"section_name": re.compile(section_name, re.IGNORECASE)},
			{"$set":{
				"section_name": section_name.title(),
				"end_time": arrow.utcnow().datetime
			}}
		)
		conn.close()

	def capture_crawler_start(self, crawler_name=None):
		""" Exceptions:
			- AssertionError
		"""
		pass
		


	# @classmethod
	# def section_start(self, name=None):
	# 	assert name is not None, "name is not defined."
	# 	db = Database.get_db(Database.MONITOR)
	# 	db.section.delete_many({"$and":[{"section_name":name},{"end_time":None}]})

	# 	document = {
	# 		"_insert_time" : arrow.utcnow().datetime,
	# 		"section_name" : name,
	# 		  "start_time" : arrow.utcnow().datetime,
	# 		    "end_time" : None
	# 	}
	# 	result = db.section.insert_one(document)
	# 	return result.inserted_id

	# @classmethod
	# def section_stop(self, id=None):
	# 	assert id is not None, "id is not defined."
	# 	db = Database.get_db(Database.MONITOR)
	# 	db.section.update({"_id":id},{"$set":{"end_time":arrow.utcnow().datetime}})

	# @classmethod
	# def start_converter(self, crawler_name=None, number_of_document=None):
	# 	assert crawler_name 			is not None, "crawler_name is not defined."
	# 	assert number_of_document       is not None, "number_of_document is not defined."
	# 	assert type(number_of_document) is int 	   , "incorrect number_of_document data type."

	# 	document = {
	# 			  "_insert_time" : arrow.utcnow().datetime,
	# 		 	  "crawler_name" : crawler_name,
	# 		 	 	"start_time" : arrow.utcnow().datetime,
	# 		          "end_time" : None,
	# 		"number_of_document" : number_of_document
	# 	}
	# 	db     = Database.get_db(Database.MONITOR)
	# 	result = db.converter.insert_one(document)
	# 	return result.inserted_id
		
	# @classmethod
	# def stop_converter(self, document_id=None):
	# 	assert document_id is not None, "document_id is not defined."
	# 	db = Database.get_db(Database.MONITOR)
	# 	db.converter.update({"_id":document_id},{"$set":{"end_time":arrow.utcnow().datetime}})

	# @classmethod
	# def inserted_document(self, crawler_name=None, document_id=None, permalink=None):
	# 	assert crawler_name is not None, "crawler_name is not defined."
	# 	assert document_id  is not None, "document_id is  not defined."
	# 	assert permalink    is not None, "permalink is not defined."

	# 	document = {
	# 		"_insert_time" : arrow.utcnow().datetime,
	# 		"crawler_name" : crawler_name.title(),
	# 		 "document_id" : document_id,
	# 		   "permalink" : permalink
	# 	}
	# 	db = Database.get_db(Database.MONITOR)
	# 	db.inserted_document.insert_one(document)

	# @classmethod
	# def crawler_start(self, crawler_name=None):
	# 	assert crawler_name is not None, "crawler_name is not defined."

	# 	db = Database.get_db(Database.MONITOR)
	# 	db.data.delete_many({"$and":[{"crawler_name":crawler_name.title()},{"end_time":None}]})

	# 	document = {
	# 		"_insert_time" : arrow.utcnow().datetime,
	# 		"crawler_name" : crawler_name.title(),
	# 		"start_time" : arrow.utcnow().datetime,
	# 		"end_time" : None
	# 	}
	# 	result = db.data.insert_one(document)
	# 	return result.inserted_id

	# @classmethod
	# def crawler_stop(self, process_id=None):
	# 	assert process_id is not None, "process_id is not defined."
	# 	db = Database.get_db(Database.MONITOR)
	# 	db.data.update({"_id":process_id},{"$set":{"end_time":arrow.utcnow().datetime}})
