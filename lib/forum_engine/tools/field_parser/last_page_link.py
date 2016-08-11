from .    import Parser
from .... import tools
import copy

class LastPageLink(Parser):
	def __init__(self):
		pass

	def parse(self, network_tools=None, thread_link=None, last_page_xpath=None):
		assert network_tools     is not None, "network_tools is not defined."
		assert thread_link       is not None, "thread_link is not defined."
		assert last_page_xpath   is not None, "last_page_xpath is not defined."

		page   = network_tools.parse(thread_link)
		domain = network_tools.get_domain(thread_link)		
		result = tools._xpath(page, last_page_xpath)
		if len(result) > 0:			
			if not type(result) is list:
				result = [result]
			result = result[0]
		else:
			result = copy.deepcopy(thread_link)
		result = tools._expand_link(domain, result)
		return result
