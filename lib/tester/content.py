from ..forum_engine.engine 			    import Engine
from ..forum_engine.tools.field_factory import FieldFactory
from . 				   	   			    import Tester
from curtsies		    			    import fmtstr
import random
import math

class Content(Tester):
	def __init__(self):
		pass

	def test(self, source=None, props=None, field=None):
		try:
			assert props is not None, "props is not defined."
			assert field is not None, "field is not defined."
			Tester.test(self, source)

			fields_parser = FieldFactory.get_parser(FieldFactory.FIELDS)
			url_parser    = FieldFactory.get_parser(FieldFactory.URL)

			success = False
			link    = random.sample(self.links,1)[0]
			print("[content_tester][debug] Link %s" % link)

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
			print("[content_tester][debug] Thread: %s" % thread_link)

			# Check if thread_link can be reached or not
			page = source.NETWORK_TOOLS.parse(thread_link, parse=False)
			if str(page) == "<html></html>":
				success = False
				print(fmtstr("[content_tester][error] Invalid link.", "red"))
			else:
				engine.current_engine = engine._make_engine(thread_link)
				posts                 = engine.current_engine.get_posts(source.POST_XPATH)			
				post                  = random.sample(posts,1)[0]
				result                = fields_parser.parse(
									 	     post = post,
									 	    xpath = props["xpath"],
									 	    props = props,
									 	    field = field
										)
				if not type(result) is list:
					result = [result]
				sample      = result[0]
				success = True if sample else False
				if not success:
					print(fmtstr("[content_tester][error] Content is empty.","red"))
		except ValueError:
			print(fmtstr("[content_tester][error] ValueError", "red"))
			success = False
		return success