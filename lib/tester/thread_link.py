from ..forum_engine.engine     import Engine
from ..forum_engine.exceptions import NoThreadLink
from . 						   import Tester
from curtsies 				   import fmtstr
import random
import math

class ThreadLink(Tester):
	def __init__(self):
		pass

	def test(self, source=None, **kwargs):
		Tester.test(self, source)
		
		success = False
		link    = random.sample(self.links,1)[0]
		print("[thread_link_tester][debug] Link: %s" % link)
		
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
		thread  = random.sample(threads, 1)[0]
		try:
			thread_link = engine.get_thread_link(thread)
			print("[thread_link_tester][debug] Thread: %s" % thread_link)
			page    = source.NETWORK_TOOLS.parse(thread_link, parse=False)
			success = False if str(page) == "<html></html>" else True
			if not success:
				print(fmtstr("[thread_link_tester][error] Invalid Link.","red"))
		except NoThreadLink:
			success = False
			print(fmtstr("[thread_link_tester][error] No Thread Link.","red"))
		return success
