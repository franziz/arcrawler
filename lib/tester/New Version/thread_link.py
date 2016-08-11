from ..forum_engine.engine     import Engine
from ..forum_engine.exceptions import NoThreadLink
from . import Tester
import random
import math

class ThreadLink(Tester):
	def __init__(self):
		pass

	def test(self, source=None, **kwargs):
		Tester.test(self, source)
		
		success = False
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
				try:
					thread_link = engine.get_thread_link(thread)
					success     = True
				except NoThreadLink:
					success = False
					break
		return success
