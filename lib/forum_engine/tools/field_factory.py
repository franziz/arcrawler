from .field_parser.last_page_link import LastPageLink as LastPageLinkParser
from .field_parser.thread  		  import Thread       as ThreadParser
from .field_parser.thread_link 	  import ThreadLink   as ThreadLinkParser
from .field_parser.prev_link   	  import PrevLink 	  as PrevLinkParser
from .field_parser.post 		  import Post 		  as PostParser
from .field_parser.fields  	      import Fields       as FieldsParser
from .field_parser.url 			  import URL  		  as URLParser
from .field_parser.date  		  import Date 		  as DateParser

class FieldFactory:
	LAST_PAGE_LINK = 0
	THREAD 		   = 1
	THREAD_LINK    = 2
	PREV_LINK      = 3
	POST  		   = 4
	FIELDS         = 5
	DATE 		   = 6
	URL 		   = 7

	def __init__(self):
		pass

	@classmethod
	def get_parser(self, parser_name=None):
		assert parser_name is not None, "parser_name is not defined."
		if parser_name == self.LAST_PAGE_LINK:
			return LastPageLinkParser()
		if parser_name == self.THREAD:
			return ThreadParser()
		if parser_name == self.THREAD_LINK:
			return ThreadLinkParser()
		if parser_name == self.PREV_LINK:
			return PrevLinkParser()
		if parser_name == self.POST:
			return PostParser()
		if parser_name == self.FIELDS:
			return FieldsParser()
		if parser_name == self.DATE:
			return DateParser()
		if parser_name == self.URL:
			return URLParser()