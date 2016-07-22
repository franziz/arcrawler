from ..network_tools import NetworkTools

class Template(object):
	TYPE                 = "news"
	TEMPLATE             = ""
	TEST_TEMPLATE		 = ""
	NAME                 = ""
	DB_SERVER_ADDRESS    = ""
	DB_SERVER_NAME       = ""
	CRAWLER_NAME         = ""
	LINK_TO_CRAWL        = ""
	COUNTRY              = ""
	TITLE_XPATH          = ""
	CONTENT_XPATH        = ""
	PUBLISHED_DATE_XPATH = ""
	AUTHOR_NAME_XPATH    = ""
	NETWORK_TOOLS        = NetworkTools()
#end class