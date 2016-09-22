from ..factory.template   import TemplateFactory
from ..factory.config     import ConfigFactory, ConverterConfig
from multiprocessing.pool import Pool
from curtsies             import fmtstr
import pymongo
import arrow

class ConverterEngine:
	def __init__(self):
		pass

	def save(self, args):
		source_address, source_name, mention = args
		
		template       = TemplateFactory.get_template(TemplateFactory.MENTION)
		mention_db     = MentionDB()
		author_info_db = AuthorInfoDB()
		try:
			mention            = template.patch(mention).to_dict()
			mention_db.mention = mention
			mention_db.save()

			author_info = author_info_db.generate_info(mention)
			author_info_db.save(author_info)
			print(fmtstr("[converter_engine][success] Converted one document!","green"))
		except pymongo.errors.DuplicateKeyError:
			print(fmtstr("[converter_engine][error] Ops! Duplicate mention","red"))
		except pymongo.errors.NetworkTimeout:
			print(fmtstr("[converter_engine][error] Network Timeout","red"))
		finally:
			connection = pymongo.MongoClient("mongodb://%s" % source_address)
			db         = connection[source_name]
			mention_db.set_as_converted(mention["MentionDirectLink"], source_db=db)
			connection.close()
		return True

	def convert(self, **kwargs):
		crawlers = kwargs.get("crawlers", None)

		if crawlers is None:
			converter_config = ConfigFactory.get_config(ConfigFactory.CONVERTER)
			crawlers         = converter_config.get("crawlers")

		for key, values in crawlers.items():
			connection = pymongo.MongoClient("mongodb://%s" % values["db_address"])
			db         = connection[values["db_name"]]
			try:
				
				documents = db.data.find({"converted":False})
				documents = [(values["db_address"], values["db_name"], document,) for document in documents]

				with Pool(5) as pool:
					pool.map(self.save, documents)
			except:
				raise
			finally:
				connection.close()
		return True

class MentionDB(object):
	def __init__(self):
		pass

	def save(self):
		assert self.mention is not None, "mention is not defined."

		config     = ConverterConfig()
		connection = pymongo.MongoClient(config.target_connection_string)
		db         = connection["isid"]

		try:
			result = db.mention.insert_one(self.mention)
			connection.close()
			return result.inserted_id
		except:
			connection.close()
			raise

	def set_as_converted(self, permalink=None, source_db=None):
		assert permalink is not None, "key is not defined."
		assert source_db is not None, "source_db is not defined."

		source_db.data.update(
			{"permalink":permalink},
			{"$set":{"converted":True}}
		)

class AuthorInfoDB(object):
	def __init__(self):
		pass

	def generate_info(self, mention=None):
		assert "SourceName"        in mention, "SourceName is not defined."
		assert "AuthorId"          in mention, "AuthorId is not defined."
		assert "AuthorName"        in mention, "AuthorName is not defined."
		assert "AuthorDisplayName" in mention, "AuthorDisplayName is not defined."
		assert "AuthorLocation"    in mention, "AuthorLocation is not defined."

		update_time      = arrow.now().format("YYYY-MM-DD HH:mm:ss")
		update_time_iso  = "%sZ" % arrow.now().format("YYYY-MM-DDTHH:mm:ss")
		author_info = {
			                "AuthorType" : mention["SourceName"],
			                  "AuthorId" : mention["AuthorId"],
			          "AuthorScreenName" : mention["AuthorName"],
			         "AuthorDisplayName" : mention["AuthorDisplayName"],
			            "AuthorLocation" : mention["AuthorLocation"],
			       "AuthorFollowerCount" : -1,
			         "AuthorFriendCount" : -1,
			         "AuthorStatusCount" : -1,
			            "AuthorLanguage" : "",
			"AuthorTotalMentionsCrawled" : 1,
			           "LastUpdatedDate" : update_time,
			        "LastUpdatedDateISO" : update_time_iso.replace(" ","T") + "Z"
		}
		return author_info

	def save(self, author_info=None):
		assert author_info is not None, "author_info is not defined."

		config     = ConverterConfig()
		connection = pymongo.MongoClient(config.target_connection_string)
		db         = connection["isid"]
		documents  = db.author_info.find({
			"AuthorScreenName" : author_info["AuthorScreenName"],
			      "AuthorType" : author_info["AuthorType"]
	   })
		is_duplicate = True if documents.count() > 0 else False

		if is_duplicate:
			db.author_info.update_one(
				{
				  	"AuthorScreenName":author_info["AuthorScreenName"],
					      "AuthorType":author_info["AuthorType"]
				},
				{
					"$inc":{"AuthorTotalMentionsCrawled":1},
					"$set":{
						   "LastUpdatedDate":author_info["LastUpdatedDate"], 
						"LastUpdatedDateISO":author_info["LastUpdatedDateISO"]
					}
				}
			)
		else:
			db.author_info.insert_one(author_info)
		connection.close()