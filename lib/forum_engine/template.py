from ..network_tools import NetworkTools

class Template(object):
	TEMPLATE          = ""
	TEST_TEMPLATE     = ""
	NAME              = ""
	DB_SERVER_ADDRESS = ""
	DB_SERVER_NAME    = ""
	CRAWLER_NAME      = ""
	LINK_TO_CRAWL     = ""
	COUNTRY           = ""
	THREAD_XPATH      = ""
	THREAD_LINK_XPATH = ""
	LAST_PAGE_XPATH   = ""
	PREV_XPATH        = ""
	POST_XPATH        = ""
	FIELDS            = dict()
	CONDITIONS        = dict()
	NETWORK_TOOLS     = NetworkTools()
#end class