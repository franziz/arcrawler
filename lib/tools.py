from lxml             import html
from .proxy_switcher  import ProxySwitcher
from .forum_engine    import exceptions
import bson.json_util
import pymongo
import pytz
import tzlocal
import lxml
import requests
import arrow
import socket
import datetime
import dateparser
import ftfy


def _expand_link(domain=None, link=None):
	assert domain    is not None                      , "Domain is not defined."
	assert "http://" in domain or "https://" in domain, "domain should have http"
	assert link      is not None                      , "Link is not defined." 

	generated_link = link
	if "http://" not in link and "https://" not in link:
		generated_link = "{domain}{link}".format(domain=domain, link=link)
	if "s=" in generated_link:
		session_string = "s="
	elif "sid=" in generated_link:
		session_string = "sid="
	elif "PHPSESSID=" in generated_link:
		session_string = "PHPSESSID="
	else:
		session_string = "s="
	if session_string in generated_link:
		session_index = generated_link.index(session_string)
		begining_link = generated_link[:session_index]
		tmp           = generated_link[session_index:]
		amp_index     = tmp.index("&") if "&" in tmp else None
		pagar_index   = tmp.index("#") if "#" in tmp else None
		if amp_index is not None and pagar_index is not None:
			ending_index = amp_index if amp_index < pagar_index else pagar_index
			ending_index = ending_index + session_index
			ending_link  = generated_link[ending_index:]
		elif amp_index is not None and pagar_index is None:
			ending_index = amp_index + session_index
			ending_link  = generated_link[ending_index:]
		elif amp_index is None and pagar_index is not None:
			ending_index = pagar_index + session_index
			ending_link  = generated_link[ending_index:]
		else:
			ending_index = -1
			ending_link  = ""
		generated_link = "".join([begining_link, ending_link])
	return generated_link
#end def

def _xpath(parent=None, syntax=None):
	assert parent is not None, "Parent is not defined."
	assert syntax is not None, "Syantax is not defined."
	
	if "re:test" in syntax:
		try:
			regexpNS = "http://exslt.org/regular-expressions"
			result   = parent.xpath(syntax,namespaces={'re':regexpNS})
		except lxml.etree.XPathEvalError as invalid_expression:
			print(syntax)
			raise
		except UnicodeDecodeError:
			result = None
		#end try
	else:
		try:
			result = parent.xpath(syntax)
		except UnicodeDecodeError:
			result = None
	#end if
	return result
#end def

def _date_parser(str_date=None):
	assert str_date       is not None, "str_date is not defined."
	assert type(str_date) is str     , "str_date should in str."	

	# manual date conversion
	str_date = str_date.lower().replace("jum'at","jumat")
	
	try:
		result = dateparser.parse(str_date)
		if result.tzinfo is None: result = tzlocal.get_localzone().localize(result, is_dst=None)
		result = result.astimezone(pytz.utc)
	except AttributeError as attr_err:
		str_date = bson.json_util.dumps({"date":str_date})
		print("[arcrawler][error] {}".format(str_date))
		print("[arcrawler][error] DATE ERROR!")
		result = None
		# result = arrow.utcnow().datetime
		# raise
	except ValueError as value_error:
		str_date = bson.json_util.dumps({"date":str_date})
		print("[arcrawler][error] {}".format(str_date))
		print("[arcrawler][error] DATE ERROR!")
		result = None
		# result = arrow.utcnow().datetime
		# raise
	except:
		raise
	#end try

	if result is not None:
		assert type(result) is datetime.datetime, "result is not datetime."
	return result
#end def

def _clean_string(string=None):
	assert string is not None, "string is not defined."
	string = ftfy.fix_encoding(string)
	string = string.encode("utf-8").replace(b"\xc2\xa0",b"").decode("utf-8")
	string = string.replace(u"\r"," ")
	string = string.replace(u"\n"," ")
	string = string.replace(u"\t"," ")
	string = string.replace(u"&#13;"," ")
	string = string.lstrip()
	string = string.rstrip()
	return string
#end def

def _assert(condition=None,  exception=None, message=None):
	assert condition is not None, "Condition is not defined."

	if exception is None and message is not None:
		assert condition, message
	elif exception is not None and message is None:
		try:
			assert condition
		except AssertionError as e:
			raise exception
		#end try
	else:
		raise exceptions.InvalidAssertionArguments("You need to specify only one paramters.")
	#end if
#end def

def _force_create_index(db=None, collection=None, field=None):
	assert db               is not None                 , "db is not defined."
	assert type(db)         is pymongo.database.Database, "db is not pymongo.database.Database."
	assert collection       is not None                 , "collection is not defined."
	assert type(collection) is str                      , "collection is not str."
	assert field            is not None                 , "field is not defined."
	assert type(field)      is str                      , "field is not str."

	has_database = False
	while not has_database:
		try:
			# check indexes inside database
			has_permalink_index = False
			max_try             = 10
			tried               = 0
			while not has_permalink_index and tried < max_try:
				tried = tried + 1
				for index in db[collection].list_indexes():
					if field in index["key"]:
						has_permalink_index = True
						break
					#end if
				#end for
				if not has_permalink_index:
					db[collection].create_index(
						[(field, pymongo.ASCENDING)],
						unique=True
					)
				#end if
			#end while
			if tried >= max_try:
				raise exceptions.MaxTryExceeded("MaxTry!")
			else:
				has_database = True
			#end for
		except pymongo.errors.OperationFailure as no_db:
			db[collection].insert({"dummy":-1})
			db[collection].remove({"dummy":-1})
		#end try
	#end while
#end def