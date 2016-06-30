from pymongo   import MongoClient
from .template import MentionTemplate
from tqdm      import tqdm
import glob
import importlib
import hashlib
import arrow
import pycountry

class Engine(object):

	def __init__(self):
		self.source_files = "/root/app/src"		
		self.files        = dict()

	def _find_sources(self):
		files   = dict()
		sources = glob.glob("{}/*.py".format(self.source_files))
		sources = tqdm(sources)
		sources.set_description("[converter_engine] Finding sources...")
		for file in sources:			
			file_name = file.split("/")[-1].replace(".py","")
			files.update({file_name : {"location":file}})
		return files
	#end def

	def convert(self, callback=None):
		assert callback is not None, "callback is not defined."

		self.files = self._find_sources()
		for key, value in self.files.items():
			source = importlib.import_module("src.{}".format(key))
			source = source.Crawler()
			self.files[key].update(dict(
				db = dict(
						address = source.DB_SERVER_ADDRESS,
						   name = source.DB_SERVER_NAME
				   )
			))

		# iterate through all files
		# assume that all files already have db_address and db_name
		# then connecto to db_address and db_name in order to get the data
		for key,value in self.files.items():
			db        = MongoClient("mongodb://{}".format(value["db"]["address"]))
			db        = db[value["db"]["name"]]
			documents = [document for document in db.data.find({"$or":[{"converted":None},{"converted":False}]})]
			documents = tqdm(documents)
			documents.set_description("[converter_engine] Converting {}".format(key))
			for document in documents:
				new_document                              = MentionTemplate()
				new_document.MentionId                    = hashlib.sha256(document["permalink"].encode("utf-8")).hexdigest()
				new_document.MentionText                  = document["content"]
				new_document.MentionType                  = "forum_post"
				new_document.MentionDirectLink            = document["permalink"]
				new_document.MentionCreatedDate           = document["published_date"]
				new_document.MentionCreatedDateISO        = document["published_date"]
				new_document.AuthorId                     = document["author_id"] if "author_id" in document else document["author_name"]
				new_document.AuthorName                   = new_document.AuthorId
				new_document.AuthorDisplayName            = document["author_name"]
				new_document.SourceType                   = "Forums"
				new_document.SourceName                   = document["_crawled_by"]
				new_document.SentFromHost                 = "220.100.163.132"
				new_document.DateInsertedIntoCrawlerDB    = document["_insert_time"]
				new_document.DateInsertedIntoCrawlerDBISO = document["_insert_time"]
				new_document.DateInsertedIntoCentralDB    = arrow.utcnow().datetime
				new_document.DateInsertedIntoCentralDBISO = arrow.utcnow().datetime
				new_document.Country                      = document["_country"]
				
				callback(source_db=db, mention=new_document.to_dict())
			#end for

		#end for
	#end def
#end class