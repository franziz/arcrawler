from ..network_tools import NetworkTools
import jinja2
import inspect
import os
import copy

class Template:
	TEMPLATE          = "crawler.arct"
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

	@classmethod
	def patch(self, crawler=None, link=None):
		assert crawler  is not None                     , "crawler is not defined."
		assert Template in inspect.getmro(type(crawler)), "incorrect crawler data type."
		assert link     is not None                     , "link is not defined."

		crawler 			  = copy.deepcopy(crawler)
		crawler.LINK_TO_CRAWL = link
		template_folder 	  = os.path.join(os.getcwd(), "templates")
		loader 				  = jinja2.FileSystemLoader(searchpath=template_folder)
		env 				  = jinja2.Environment(loader=loader)
		template  			  = env.get_template(crawler.TEMPLATE)
		template 		      = template.render(template=crawler)
		return template

	def get_variables(self):
		return [
			"TEMPLATE",
			"TEST_TEMPLATE",
			"NAME",
			"DB_SERVER_ADDRESS",
			"DB_SERVER_NAME",
			"CRAWLER_NAME",
			"LINK_TO_CRAWL",
			"COUNTRY",
			"THREAD_XPATH",
			"THREAD_LINK_XPATH",
			"LAST_PAGE_XPATH",
			"PREV_XPATH",
			"POST_XPATH",
			"FIELDS",
			"CONDITIONS",
			"NETWORK_TOOLS"
		]
#end class