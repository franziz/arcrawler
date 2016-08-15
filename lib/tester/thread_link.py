# -*- coding: utf-8 -*-

from ..validator.factory       import ValidatorFactory
from ..forum_engine.exceptions import NoThreadLink
from ..exceptions  			   import CannotOpenURL
from . 						   import Tester
from curtsies 				   import fmtstr
import random
import math

class ThreadLink(Tester):
	def __init__(self):
		pass

	def test(self, source=None, **kwargs):
		try:
			Tester.test(self, source)
			
			url_validator = ValidatorFactory.get_validator(ValidatorFactory.URL)
			
			success = False
			link    = random.sample(self.links,1)[0]
			engine  = self.prepare_engine()
			engine.set_link_to_crawl(link)
			print("[thread_link_tester][debug] Link: %s" % link.encode("utf-8"))

			threads     = engine.get_threads()
			thread      = random.sample(threads, 1)[0]
			thread_link = engine.get_thread_link(thread)
			print("[thread_link_tester][debug] Thread: %s" % thread_link.encode("utf-8"))

			url_validator.validate(thread_link)
			success = True
		except NoThreadLink as no_thread_link:
			print(fmtstr("[thread_link_tester][error] %s" % no_thread_link,"red"))			
			success = False
		except ValueError as value_error:
			print(fmtstr("[thread_link_tester][error] %s" % value_error, "red"))
			success = False
		except CannotOpenURL as cannot_open_url:
			print(fmtstr("[thread_link_tester][error] %s" % cannot_open_url,"red"))
			success = False
		return success
