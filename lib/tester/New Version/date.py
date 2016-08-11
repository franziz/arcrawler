from ..forum_engine.engine 			    import Engine
from ..forum_engine.tools.field_factory import FieldFactory
from . 				   	   			    import Tester
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
		results = []
		for link in self.links:
			print("[date_parser][debug] Link: %s" % link)
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
				thread_link           = engine.get_thread_link(thread) # Assuming thread_link has no error				
				engine.current_engine = engine._make_engine(thread_link)
				posts                 = engine.current_engine.get_posts(source.POST_XPATH)

				print("[date_parser][debug] Thread: %s" % thread_link)
				for post in posts:
					result = fields_parser.parse(
						          post = post,
						         xpath = props["xpath"],
						         props = props,
						         field = field
							 )
					result = date_parser.parse(result)
					if type(result) is list:
						if None in result: break
					else:
						if result is None: break
					print("[date_tester][debug] Data: %s" % result)

		success = False if False in results else True			
		return success
		