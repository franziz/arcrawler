from ..forum_engine.engine   import Engine
from ..network_tools   		 import NetworkTools
from . 						 import Tester
from curtsies	 			 import fmtstr
import random
import math

class LastPageLink(Tester):
	def __init__(self):
		pass

	def test(self, source=None):
		Tester.test(self, source)

		success = False
		results = []
		stop    = False
		for link in self.links:
			if stop: break
			print("[last_page_link_tester][debug] Link: %s" % link)
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
				if stop: break
				thread_link           = engine.get_thread_link(thread) # Assuming thread_link has no error				
				engine.current_engine = engine._make_engine(thread_link)
				if engine.current_engine.has_last_page:
					print("[last_page_link_tester][debug] Thread: %s" % engine.current_engine.current_page_link)
					# I think I need to check if the last_page link can be opened or not
					page    = source.NETWORK_TOOLS.parse(engine.current_engine.current_page_link, parse=False)					
					success = False if str(page) == "<html></html>" else True
					stop    = True
					if not success:
						print(fmtstr("[last_page_link_tester][error] Invalid url.","red"))
		return success