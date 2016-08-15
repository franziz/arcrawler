# -*- coding: utf-8 -*-

from ..forum_engine.exceptions import NoThreadLink
from ..validator.factory       import ValidatorFactory
from ..network_tools   	       import NetworkTools
from ..exceptions              import CannotOpenURL
from . 					       import Tester
from curtsies 			       import fmtstr
import random
import math

class Post(Tester):
	def __init__(self):
		pass

	def test(self, source):
		try:
			Tester.test(self, source)

			url_validator = ValidatorFactory.get_validator(ValidatorFactory.URL)

			success = False
			link    = random.sample(self.links,1)[0]
			engine  = self.prepare_engine()
			engine.set_link_to_crawl(link)
			print("[post_tester][debug] Link: %s" % link.encode("utf-8"))


			threads     = engine.get_threads()
			thread      = random.sample(threads, 1)[0]		
			thread_link = engine.get_thread_link(thread)
			print("[post_tester][debug] Thread: %s" % thread_link.encode("utf-8"))
			url_validator.validate(thread_link)			

			engine.current_engine = engine._make_engine(thread_link)
			print("[post_tester][debug] Current Page: %s" % engine.current_engine.current_page_link.encode("utf-8"))
			url_validator.validate(engine.current_engine.current_page_link)

			posts   = engine.current_engine.get_posts(source.POST_XPATH)		
			success = True if len(posts) > 0 else False		
			if not success:
				print(fmtstr("[post_tester][error] No posts!","red"))
		except NoThreadLink as no_thread_link:
			print(fmtstr("[post_tester][error] %s" % no_thread_link,"red"))
			success = False
		except CannotOpenURL as cannot_open_url:
			print(fmtstr("[post_tester][error] %s" % cannot_open_url,"red"))
			success = False
		except ValueError as value_error:
			print(fmtstr("[post_tester][error] %s" % value_error,"red"))
			success = False
		return success