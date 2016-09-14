from ..config.factory import ConfigFactory
from ..monitor 		  import Monitor
from ..database       import Database
from .object 		  import MentionDB, AuthorInfoDB
from .template        import MentionTemplate
from curtsies 		  import fmtstr
import pymongo
import arrow
import tomorrow

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
		return [document for document in db.data.find(
			{"$where": "(this.converted == null || this.converted==false)"},
		)]

	@tomorrow.threads(10)
	def save(self, source_db=None, mention=None):
		mention_db     = MentionDB()
		author_info_db = AuthorInfoDB()
		try:
			mention_db.mention = mention
			mention_db.save()

			author_info_db.generate_info(mention)
			author_info_db.save()
			print("[converter_engine][debug] Converted one document!")
		except pymongo.errors.DuplicateKeyError:
			print(fmtstr("[converter_engine][error] Ops! Duplicate mention"))
		finally:
			mention_db.set_as_converted(source_db=source_db)
		return True

	def convert(self):
		crawlers = self.get_crawlers()
		for crawler_name, config in crawlers.items():
			assert "db_address" in config, "db_address is not defined."
			assert "db_name"    in config, "db_name is not defined."

			print("[converter_engine][debug] Converting %s" % crawler_name)
			db         = self.get_db(db_address=config["db_address"], db_name=config["db_name"])
			template   = MentionTemplate()
			documents  = self.get_documents(db=db)
			monitor_id = Monitor.start_converter(crawler_name=crawler_name.title(), number_of_document=len(documents))
			documents  = [template.patch(document).to_dict() for document in documents]
			print("[converter_engine][debug] Found %s document(s)" % len(documents))
			
			documents = [self.save(db, document) for document in documents]
			Monitor.stop_converter(document_id=monitor_id)