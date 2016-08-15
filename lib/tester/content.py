# -*- coding: utf-8 -*-

from ..forum_engine.tools.field_factory import FieldFactory
from ..forum_engine.exceptions 			import NoThreadLink
from ..validator.factory  				import ValidatorFactory
from ..exceptions 					    import CannotOpenURL
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

			url_validator = ValidatorFactory.get_validator(ValidatorFactory.URL)
			fields_parser = FieldFactory.get_parser(FieldFactory.FIELDS)
			url_parser    = FieldFactory.get_parser(FieldFactory.URL)

			success = False
			link    = random.sample(self.links,1)[0]
			engine  = self.prepare_engine()
			engine.set_link_to_crawl(link)
			print("[content_tester][debug] Link %s" % link.encode("utf-8"))

			threads     = engine.get_threads()
			thread      = random.sample(threads, 1)[0]
			thread_link = engine.get_thread_link(thread)
			print("[content_tester][debug] Thread: %s" % thread_link.encode("utf-8"))
		
			url_validator.validate(thread_link) # Will raise a CannotOpenURL Exception
			engine.current_engine = engine._make_engine(thread_link)
			print("[content_tester][debug] Current Page: %s" % engine.current_engine.current_page_link.encode("utf-8"))

			posts  = engine.current_engine.get_posts(source.POST_XPATH)			
			post   = random.sample(posts,1)[0]
			result = fields_parser.parse(
				 	      post = post,
				 	     xpath = props["xpath"],
				 	     props = props,
				 	     field = field
					 )
			if not type(result) is list:
				result = [result]
			sample  = result[0]
			success = True if sample else False
			if not success:
				print(fmtstr("[content_tester][error] Content is empty.","red"))
		except NoThreadLink as no_thread_link:
			print(fmtstr("[content_tester][error] %s" % no_thread_link,"red"))
			success = False
		except ValueError as value_error:
			print(fmtstr("[content_tester][error] %s" % value_error, "red"))
			success = False
		except CannotOpenURL as cannot_open_url:
			print(fmtstr("[content_tester][error] %s" % cannot_open_url, "red"))
			success = False
		return success