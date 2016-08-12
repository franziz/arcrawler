from ..forum_engine.engine 			    import Engine
from ..forum_engine.tools.field_factory import FieldFactory
from ..network_tools 					import NetworkTools
from . 				   	   			    import Tester
from curtsies		    			    import fmtstr
import random
import math

class URL(Tester):
	def __init__(self):
		pass

	def test(self, source=None, props=None, field=None):
		try:
			assert props is not None, "props is not defined."
			assert field is not None, "field is not defined."
			Tester.test(self, source)

			fields_parser = FieldFactory.get_parser(FieldFactory.FIELDS)
			url_parser    = FieldFactory.get_parser(FieldFactory.URL)

			link    = random.sample(self.links,1)[0]
			success = False
			engine  = Engine()
			engine.set_name(source.CRAWLER_NAME)
			engine.set_method(engine.BACKWARD)
			engine.set_link_to_crawl(link)
			engine.set_thread_xpath(source.THREAD_XPATH)
			engine.set_thread_link_xpath(source.THREAD_LINK_XPATH)
			engine.set_last_page_xpath(source.LAST_PAGE_XPATH)
			engine.set_prev_xpath(source.PREV_XPATH)
			engine.set_post_xpath(source.POST_XPATH)
			engine.set_network_tools(source.NETWORK_TOOLS)

			threads               = engine.get_threads()
			thread                = random.sample(threads, 1)[0]		
			thread_link           = engine.get_thread_link(thread)
			engine.current_engine = engine._make_engine(thread_link)
			posts                 = engine.current_engine.get_posts(source.POST_XPATH)		
			post                  = random.sample(posts,1)[0] # assuming has post
			result                = fields_parser.parse(
								 	     post = post,
								 	    xpath = props["xpath"],
								 	    props = props,
								 	    field = field
									)
			if not type(result) is list:
				result = [result]
			sample      = result[0]
			print("[url_tester][debug] Sample: %s" % sample)
			sample_page = source.NETWORK_TOOLS.parse(sample, parse=False)
			sample_page = str(sample_page)
			if "<html></html>" in sample_page:
				success = False
			else:
				success = True
		except ValueError:
			print(fmtstr("[url_tester][error] ValueError","red"))
			success = False
		return success