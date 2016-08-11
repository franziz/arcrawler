from ..forum_engine.engine   import Engine
from ..network_tools   		 import NetworkTools
from . 						 import Tester
import random
import math

class Post(Tester):
	def __init__(self):
		pass

	def test(self, source):
		Tester.test(self, source)

		success = False
		results = []
		for link in self.links:
			engine = Engine()
			engine.set_name(source.CRAWLER_NAME)
			engine.set_method(engine.BACKWARD)
			engine.set_link_to_crawl(link)
			engine.set_thread_xpath(source.THREAD_XPATH)
			engine.set_thread_link_xpath(source.THREAD_LINK_XPATH)
			engine.set_last_page_xpath(source.LAST_PAGE_XPATH)
			engine.set_prev_xpath(source.PREV_XPATH)
			engine.set_post_xpath(source.POST_XPATH)
			engine.set_network_tools(source.NETWORK_TOOLS)

			threads = engine.get_threads()
			threads = random.sample(threads, math.ceil(len(threads) * 0.1))
			for thread in threads:				
				thread_link           = engine.get_thread_link(thread) # Assuming thread_link has no error				
				engine.current_engine = engine._make_engine(thread_link)
				posts                 = engine.current_engine.get_posts(source.POST_XPATH)
				# Force exit if found any posts in the link
				# This test will only test wheteher you can find a post or not
				if len(posts) > 0:
					results.append(True)
					break
				else:
					results.append(False)
			# Stop the iteration if found a last_page_link.
			# Assuming that other last_page_link should be the same
			if True in results: break
		success = True if True in results else False			
		return success