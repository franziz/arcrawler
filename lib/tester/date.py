from ..forum_engine.engine 			    import Engine
from ..forum_engine.tools.field_factory import FieldFactory
from ..forum_engine.exceptions		    import NoThreadLink
from . 				   	   			    import Tester
from curtsies 						    import fmtstr
import random
import math

class Date(Tester):
	def __init__(self):
		pass

	def test(self, source=None, props=None, field=None):
		assert props is not None, "props is not defined."
		assert field is not None, "field is not defined."

		Tester.test(self, source)

		fields_parser = FieldFactory.get_parser(FieldFactory.FIELDS)
		date_parser   = FieldFactory.get_parser(FieldFactory.DATE)

		success = False
		stop    = False
		for link in self.links:
			if stop: break
			print("[date_tester][debug] Link: %s" % link)
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
			threads = random.sample(threads, math.ceil(len(threads)*0.1))
			for thread in threads:
				if stop: break
				try:
					thread_link           = engine.get_thread_link(thread) 				
					engine.current_engine = engine._make_engine(thread_link)

					page = source.NETWORK_TOOLS.parse(engine.current_engine.current_page_link, parse=False)
					if str(page) == "<html></html>":
						success = False
						stop    = True
						print(fmtstr("[date_tester][error] Invalid link.", "red"))
					else:
						print("[date_tester][debug] Thread: %s" % thread_link)
						posts = engine.current_engine.get_posts(source.POST_XPATH)
						for post in posts:
							result = fields_parser.parse(
								          post = post,
								         xpath = props["xpath"],
								         props = props,
								         field = field
									 )
							result = date_parser.parse(result)
							if not type(result) is list:
								result = [result]
							if None in result:
								success = False
								stop    = True
							else:
								success = True
							for r in result:
								print("[date_tester][debug] Data: %s" % r)
				except NoThreadLink:
					print("[date_tester][debug] Passing the thread_link.")
		return success
		