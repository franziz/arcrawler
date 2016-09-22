from ..parser.fields   import FieldsParser
from ..parser.xpath    import XPATHParser
from ..parser.date     import DateParser
from ..parser.template import TemplateParser

class ParserFactory:
	FIELDS   = 0
	XPATH    = 1
	DATE     = 2
	TEMPLATE = 3

	def __init__(self):
		pass

	@classmethod
	def get_parser(self, parser_name=None):
		assert parser_name is not None, "parser_name is not defined."

		if parser_name == ParserFactory.FIELDS:
			return FieldsParser()
		elif parser_name == ParserFactory.XPATH:
			return XPATHParser()
		elif parser_name == ParserFactory.DATE:
			return DateParser()
		elif parser_name == ParserFactory.TEMPLATE:
			return TemplateParser()