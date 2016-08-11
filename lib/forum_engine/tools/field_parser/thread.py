from .    import Parser
from .... import tools

class Thread(Parser):
	def __init__(self):
		pass

	def parse(self, network_tools=None, link=None, thread_xpath=None):
		assert network_tools is not None, "network_tools is not defined."
		assert link 		 is not None, "link is not defined."
		assert thread_xpath  is not None, "thread_xpath is not defined."

		page    = network_tools.parse(link)
		threads = tools._xpath(page, thread_xpath)

		# If the result of the xpath parsing is not list
		# force it to list. However, the list should be empty
		# because it violate the term and condition
		if type(threads) is not list:
			threads = []		
		return threads