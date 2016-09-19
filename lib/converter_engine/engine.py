from ..config.factory import ConfigFactory
from ..monitor 		  import Monitor
from ..database       import Database
from .object 		  import MentionDB, AuthorInfoDB
from .template        import MentionTemplate
from curtsies 		  import fmtstr
from multiprocessing  import Pool
import pymongo
import arrow

class Engine(object):
	def __init__(self):
		self.config_file = ConfigFactory.get(ConfigFactory.CONVERTER)

	def get_crawlers(self):
		assert self.config_file is not None, "config_file is not defined."
		crawlers = self.config_file.get("crawlers")
		return crawlers

	def get_db(self, db_address=None, db_name=None):
		assert db_address is not None, "db_address is not defined."
		assert db_name    is not None, "db_name is not defined."
		db = pymongo.MongoClient("mongodb://%s" % db_address)
		return db[db_name]


	def get_documents(self, db=None):
		assert db is not None, "db is not defined."
		return db.data.find(
			{"$where": "(this.converted == null || this.converted==false)"},
		)

	def save(self, args=None):
		source_address, source_name, mention = args
		
		template       = MentionTemplate()
		mention_db     = MentionDB()
		author_info_db = AuthorInfoDB()
		try:
			mention            = template.patch(mention).to_dict()
			mention_db.mention = mention
			mention_db.save()

			author_info_db.generate_info(mention)
			author_info_db.save()
			print("[converter_engine][debug] Converted one document!")
		except pymongo.errors.DuplicateKeyError:
			print(fmtstr("[converter_engine][error] Ops! Duplicate mention","red"))
		except pymongo.errors.NetworkTimeout:
			print(fmtstr("[converter_engine][error] Network Timeout","red"))
		finally:
			db = self.get_db(db_address=source_address, db_name=source_name)
			mention_db.set_as_converted(source_db=db)
		return True

	def convert(self):
		crawlers = self.get_crawlers()
		for crawler_name, config in crawlers.items():
			assert "db_address" in config, "db_address is not defined."
			assert "db_name"    in config, "db_name is not defined."

			print("[converter_engine][debug] Converting %s" % crawler_name)
			db         = self.get_db(db_address=config["db_address"], db_name=config["db_name"])
			documents  = self.get_documents(db=db)
			monitor_id = Monitor.start_converter(crawler_name=crawler_name.title(), number_of_document=documents.count())
			print("[converter_engine][debug] Found %s document(s)" % documents.count())

			documents = [(config["db_address"], config["db_name"], document) for document in documents]
			with Pool(3) as pool:
				pool.map(self.save, documents)
			Monitor.stop_converter(document_id=monitor_id)