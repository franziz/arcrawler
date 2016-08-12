from ..forum_engine.engine   import Engine
from ..network_tools   		 import NetworkTools
from . 						 import Tester
from curtsies 				 import fmtstr
import random
import math

class Post(Tester):
	def __init__(self):
		pass

	def test(self, source):
		Tester.test(self, source)

		success = False
		link    = random.sample(self.links,1)[0]
		print("[post_tester][debug] Link: %s" % link)

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

		threads     = engine.get_threads()
		thread      = random.sample(threads, 1)[0]		
		thread_link = engine.get_thread_link(thread)
		print("[post_tester][debug] Thread: %s" % thread_link)

		page = source.NETWORK_TOOLS.parse(thread_link, parse=False)
		if str(page) == "<html></html>":
			success = False
			print(fmtstr("[post_tester][error] Invalid link.","red"))
		else:
			engine.current_engine = engine._make_engine(thread_link)
			posts                 = engine.current_engine.get_posts(source.POST_XPATH)		
			success               = True if len(posts) > 0 else False		
			if not success:
				print(fmtstr("[post_tester][error] No posts!","red"))
		return success