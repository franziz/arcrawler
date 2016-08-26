from pymongo          import MongoClient
from .template        import MentionTemplate
from tqdm             import tqdm
from urllib.parse     import urlparse
from ..config.factory import ConfigFactory
import glob
import importlib
import hashlib
import arrow
import pycountry

class Engine(object):

	def __init__(self):
		self.config_file = ConfigFactory.get(ConfigFactory.CONVERTER)

	def convert(self, callback=None):
		assert callback         is not None, "callback is not defined."
		assert self.config_file is not None, "config_file is not defined."

		# iterate through all files
		# assume that all files already have db_address and db_name
		# then connecto to db_address and db_name in order to get the data
		# for key,value in self.files.items():
		crawlers = self.config_file.get("crawlers")
		for key,value in crawlers.items():
			db        = MongoClient("mongodb://{}".format(value["db_address"]))
			db        = db[value["db_name"]]
			documents = [document for document in db.data.find(
							{"$where": "(this.converted == null || this.converted==false) && this.published_date <= this._insert_time"},
						)]
			documents = tqdm(documents)
			for document in documents:
				_id = document["permalink"] if "permalink" in document else document["url"] if "url" in document else None
				documents.set_description("[converter_engine] Converting {}".format(key))
				
				source_name                               = document["permalink"]
				source_name                               = urlparse(source_name)
				source_name                               = source_name.netloc
				source_name                               = source_name.lower().replace("www.","")
				source_name                               = "{}{}".format(source_name[0].upper(), source_name[1:])

				new_document                              = MentionTemplate()
				new_document.MentionId                    = hashlib.sha256(_id.encode("utf-8")).hexdigest() 
				new_document.MentionText                  = document["content"]
				new_document.MentionMiscInfo			  = document["_thread_link"] if "_thread_link" in document else ""
				new_document.MentionType                  = "forum_post"
				new_document.MentionDirectLink            = document["permalink"]
				new_document.MentionCreatedDate           = document["published_date"]
				new_document.MentionCreatedDateISO        = document["published_date"]
				new_document.AuthorId                     = document["author_id"] if "author_id" in document else document["author_name"]
				new_document.AuthorName                   = document["author_name"]
				new_document.AuthorDisplayName            = document["author_name"]
				new_document.SourceType                   = "Forums"
				new_document.SourceName                   = source_name
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