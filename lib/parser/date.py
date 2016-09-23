from ..exceptions import ParseError
import dateparser
import arrow
import datetime
import bson.json_util
import lxml

class DateParser:
	def __init__(self):
		pass

	def parse(self, str_date=None):
		assert str_date is not None, "str_date is not defined."		

		# manual date conversion
		if "jum'at" in str_date:
			str_date = str_date.lower().replace("jum'at","jumat")
		
		try:
			try:
				# Arrow is timezone aware, it is first priority
				result = arrow.get(str_date).datetime
			except arrow.parser.ParserError:
				result = dateparser.parse(str_date)
		except AttributeError as attr_err:
			str_date = bson.json_util.dumps({"date":str_date})
			print("[arcrawler][error] {}".format(str_date))
			print("[arcrawler][error] DATE ERROR!")
			result = None
		except ValueError as value_error:
			str_date = bson.json_util.dumps({"date":str_date})
			print("[arcrawler][error] {}".format(str_date))
			print("[arcrawler][error] DATE ERROR!")
			result = None
		except:
			raise ParseError("Cannot parse date: %s" % str_date)

		if result is not None:
			assert type(result) is datetime.datetime, "result is not datetime."
		return result