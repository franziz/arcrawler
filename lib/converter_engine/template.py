from urllib.parse import urlparse
import pycountry
import arrow
import hashlib

class MentionTemplate(object):

	def __init__(self):
		self.mention_id                        = ""
		self.mention_title                     = ""
		self.mention_description               = ""
		self.mention_text                      = ""
		self.mention_type                      = ""
		self.mention_language                  = ""
		self.mention_direct_link               = ""
		self.mention_location                  = ""
		self.mention_created_date              = ""
		self.mention_created_date_iso          = ""
		self.mention_in_reply_to               = ""
		self.mention_misc_info                 = ""
		self.author_id                         = ""
		self.author_name                       = ""
		self.author_dipslay_name               = ""
		self.author_location                   = ""
		self.author_language                   = ""
		self.author_misc_info                  = ""
		self.tenant_id                         = ""
		self.tenant_track_tags                 = ""
		self.source_type                       = ""
		self.source_name                       = ""
		self.sent_from_host                    = ""
		self.date_inserted_into_crawler_db     = ""
		self.date_inserted_into_crawler_db_iso = ""
		self.date_inserted_into_central_db     = ""
		self.date_inserted_into_central_db_iso = ""
		self.tenant_dbs_forwarded              = ""
		self.country                           = ""
		self.ttl                               = arrow.utcnow().datetime


	def patch(self, document=None):
		assert document is not None, "document is not defined."
		_id = document["permalink"] if "permalink" in document else document["url"] if "url" in document else None
		
		source_name = document["permalink"]
		source_name = urlparse(source_name)
		source_name = source_name.netloc
		source_name = source_name.lower().replace("www.","")
		source_name = "{}{}".format(source_name[0].upper(), source_name[1:])

		self.MentionId                    = hashlib.sha256(_id.encode("utf-8")).hexdigest() 
		self.MentionText                  = document["content"]
		self.MentionMiscInfo			  = document["_thread_link"] if "_thread_link" in document else ""
		self.MentionType                  = "forum_post"
		self.MentionDirectLink            = document["permalink"]
		self.MentionCreatedDate           = document["published_date"]
		self.MentionCreatedDateISO        = document["published_date"]
		self.AuthorId                     = document["author_id"] if "author_id" in document else document["author_name"]
		self.AuthorName                   = document["author_name"]
		self.AuthorDisplayName            = document["author_name"]
		self.SourceType                   = "Forums"
		self.SourceName                   = source_name
		self.SentFromHost                 = "220.100.163.132"
		self.DateInsertedIntoCrawlerDB    = document["_insert_time"]
		self.DateInsertedIntoCrawlerDBISO = document["_insert_time"]
		self.DateInsertedIntoCentralDB    = arrow.utcnow().datetime
		self.DateInsertedIntoCentralDBISO = arrow.utcnow().datetime
		self.Country                      = document["_country"]
		return self

	def to_dict(self):
		""" 
			This will conver all properties become a dict. 
		    This function hold an assumption that the property always starts with upper case
		"""

		properties = [prop for prop in dir(self) if prop[0].isupper()]
		result     = dict()
		for prop in properties:
			result.update({prop:getattr(self,prop)})

		return result

	@property
	def MentionId(self):
		return self.mention_id

	@MentionId.setter
	def MentionId(self, value):
		self.mention_id = value

	@property
	def MentionTitle(self):
		return self.mention_title

	@MentionTitle.setter
	def MentionTitle(self, value):
		self.mention_title = value

	@property
	def MentionDescription(self):
		return self.mention_description

	@MentionDescription.setter
	def MentionDescription(self,value):
		self.mention_description = value

	@property
	def MentionText(self):
		return self.mention_text

	@MentionText.setter
	def MentionText(self,value):
		self.mention_text = value

	@property
	def MentionType(self):
		return self.mention_type

	@MentionType.setter
	def MentionType(self,value):
		self.mention_type = value

	@property
	def MentionLanguage(self):
		return self.mention_language

	@MentionLanguage.setter
	def MentionLanguage(self,value):
		self.mention_language = value

	@property
	def MentionDirectLink(self):
		return self.mention_direct_link

	@MentionDirectLink.setter
	def MentionDirectLink(self,value):
		self.mention_direct_link = value

	@property
	def MentionLocation(self):
		return self.mention_location

	@MentionLocation.setter
	def MentionLocation(self,value):
		self.mention_location = value

	@property
	def MentionCreatedDate(self):
		return self.mention_created_date

	@MentionCreatedDate.setter
	def MentionCreatedDate(self,value):
		date                      = arrow.get(value)
		date                      = date.format("YYYY-MM-DD HH:mm:ss")
		self.mention_created_date = date

	@property
	def MentionCreatedDateISO(self):		
		return self.mention_created_date_iso

	@MentionCreatedDateISO.setter
	def MentionCreatedDateISO(self, value):
		date                          = arrow.get(value)
		date                          = date.format("YYYY-MM-DDTHH:mm:ss")
		date                          = date  + "Z"
		self.mention_created_date_iso = date

	@property
	def MentionInReplyTo(self):
		return self.mention_in_reply_to

	@MentionInReplyTo.setter
	def MentionInReplyTo(self, value):
		self.mention_in_reply_to = value

	@property
	def MentionMiscInfo(self):
		return self.mention_misc_info

	@MentionMiscInfo.setter
	def MentionMiscInfo(self, value):
		self.mention_misc_info = value

	@property
	def AuthorId(self):
		return self.author_id

	@AuthorId.setter
	def AuthorId(self, value):
		self.author_id = value

	@property
	def AuthorName(self):
		return self.author_name

	@AuthorName.setter
	def AuthorName(self, value):
		self.author_name = value

	@property
	def AuthorDisplayName(self):
		return self.author_dipslay_name

	@AuthorDisplayName.setter
	def AuthorDisplayName(self, value):
		self.author_dipslay_name = value

	@property
	def AuthorLocation(self):
		return self.author_location

	@AuthorLocation.setter
	def AuthorLocation(self, value):
		self.author_location = value

	@property
	def AuthorLanguage(self):
		return self.author_language

	@AuthorLanguage.setter
	def AuthorLanguage(self, value):
		self.author_language = value

	@property
	def AuthorMiscInfo(self):
		return self.author_misc_info

	@AuthorMiscInfo.setter
	def AuthorMiscInfo(self, value):
		selc.author_misc_info = value

	@property
	def TenantId(self):
		return self.tenant_id

	@TenantId.setter
	def TenantId(self, value):
		self.tenant_id = value

	@property
	def TenantTrackTags(self):
		return self.tenant_track_tags

	@TenantTrackTags.setter
	def TenantTrackTags(self, value):
		self.tenant_track_tags = value

	@property
	def SourceType(self):
		return self.source_type

	@SourceType.setter
	def SourceType(self, value):
		self.source_type = value

	@property
	def SourceName(self):
		return self.source_name

	@SourceName.setter
	def SourceName(self, value):
		self.source_name = value

	@property
	def SentFromHost(self):
		return self.sent_from_host

	@SentFromHost.setter
	def SentFromHost(self, value):
		self.sent_from_host = value

	@property
	def DateInsertedIntoCrawlerDB(self):
		return self.date_inserted_into_crawler_db

	@DateInsertedIntoCrawlerDB.setter
	def DateInsertedIntoCrawlerDB(self, value):
		date                               = arrow.get(value)
		date                               = date.to("Asia/Singapore")
		date                               = date.format("YYYY-MM-DD HH:mm:ss")
		self.date_inserted_into_crawler_db = date

	@property
	def DateInsertedIntoCrawlerDBISO(self):
		return self.date_inserted_into_crawler_db_iso

	@DateInsertedIntoCrawlerDBISO.setter
	def DateInsertedIntoCrawlerDBISO(self, value):
		date                                   = arrow.get(value)
		date 								   = date.to("Asia/Singapore")
		date                                   = date.format("YYYY-MM-DDTHH:mm:ss")
		date                                   = date  + "Z"
		self.date_inserted_into_crawler_db_iso = date

	@property
	def DateInsertedIntoCentralDB(self):
		return self.date_inserted_into_central_db

	@DateInsertedIntoCentralDB.setter
	def DateInsertedIntoCentralDB(self, value):
		date                               = arrow.get(value)
		date                               = date.to("Asia/Singapore")
		date                               = date.format("YYYY-MM-DD HH:mm:ss")
		self.date_inserted_into_central_db = date

	@property
	def DateInsertedIntoCentralDBISO(self):
		return self.date_inserted_into_central_db_iso

	@DateInsertedIntoCentralDBISO.setter
	def DateInsertedIntoCentralDBISO(self, value):
		date                                   = arrow.get(value)
		date 								   = date.to("Asia/Singapore")
		date                                   = date.format("YYYY-MM-DDTHH:mm:ss")
		date                                   = date  + "Z"
		self.date_inserted_into_central_db_iso = date	

	@property
	def TenantDBsForwarded(self):
		return self.tenant_dbs_forwarded

	@TenantDBsForwarded.setter
	def TenantDBsForwarded(self, value):
		self.tenant_dbs_forwarded = value

	@property
	def Country(self):
		return self.country

	@Country.setter
	def Country(self, value):		
		country      = pycountry.countries.get(alpha3=value)
		country      = country.name.upper()
		country 	 = country.replace(" ","_")

		if country == "VIET_NAM":
			country = "VIETNAM"

		self.country = country
	