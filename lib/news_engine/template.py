from ..network_tools import NetworkTools

class Template(object):
	TEMPLATE                = ""
	TEST_TEMPLATE			= ""
	NAME                    = ""
	DB_SERVER_ADDRESS       = ""
	DB_SERVER_NAME          = ""
	CRAWLER_NAME            = ""
	LINK_TO_CRAWL           = ""
	COUNTRY                 = ""
	TITLE_FALLBACK          = list()
	CONTENT_FALLBACK        = list()
	PUBLISHED_DATE_FALLBACK = list()
	AUTHOR_NAME_FALLBACK    = list()
	NETWORK_TOOLS           = NetworkTools()
#end class