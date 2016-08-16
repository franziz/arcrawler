# -*- coding: utf-8 -*-

from ..forum_engine.tools.field_factory import FieldFactory
from ..forum_engine.exceptions 			import NoThreadLink, NoThreadFound, NoPostFound
from ..network_tools 					import NetworkTools
from ..validator.factory   			    import ValidatorFactory
from ..exceptions 					    import CannotOpenURL
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

			url_validator = ValidatorFactory.get_validator(ValidatorFactory.URL)
			fields_parser = FieldFactory.get_parser(FieldFactory.FIELDS)
			url_parser    = FieldFactory.get_parser(FieldFactory.URL)

			link = random.sample(self.links,1)[0]
			print("[url_tester][debug] Link: %s" % link.encode("utf-8"))
			
			success = False
			engine  = self.prepare_engine()
			engine.set_link_to_crawl(link)

			threads = engine.get_threads()
			if len(threads) == 0: raise NoThreadFound("No thread(s) were found.")

			thread      = random.sample(threads, 1)[0]		
			thread_link = engine.get_thread_link(thread)
			print("[url_tester][debug] Thread: %s" % thread_link.encode("utf-8"))

			engine.current_engine = engine._make_engine(thread_link)
			print("[url_tester][debug] Current Page: %s" % engine.current_engine.current_page_link.encode("utf-8"))

			posts = engine.current_engine.get_posts(source.POST_XPATH)
			if len(posts) == 0: raise NoPostFound("No post(s) were found.")

			post   = random.sample(posts,1)[0] # assuming has post
			result = fields_parser.parse(
				 	      post = post,
				 	     xpath = props["xpath"],
				 	     props = props,
				 	     field = field
					 )
			if not type(result) is list:
				result = [result]
			sample = result[0]
			print("[url_tester][debug] XPATH Result: %s" % sample.encode("utf-8"))
			
			sample = url_parser.parse(value=sample, domain=NetworkTools.get_domain(engine.current_engine.current_page_link))
			print("[url_tester][debug] Sample: %s" % sample.encode("utf-8"))

			url_validator.validate(sample) # Will throw CannotOpenURL exception
			success = True # If the code hits this line, it means success
		except NoPostFound as no_post:
			print(fmtstr("[url_tester][error] %s" % no_post, "red"))
			success = False
		except NoThreadFound as no_thread:
			print(fmtstr("[url_tester][error] %s" % no_thread, "red"))
			success = False
		except ValueError as value_error:
			print(fmtstr("[url_tester][error] %s" % value_error,"red"))
			success = False
		except NoThreadLink as no_thread_link:
			print(fmtstr("[url_tester][error] %s" % no_thread_link,"red"))
			success = False
		except CannotOpenURL as cannot_open_url:
			print(fmtstr("[url_tester][error] %s" % cannot_open_url,"red"))
			success = False
		return success