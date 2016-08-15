# -*- coding: utf-8 -*-

from ..validator.factory import ValidatorFactory
from ..exceptions  		 import CannotOpenURL
from . 		             import Tester
from curtsies            import fmtstr
import random

class Thread(Tester):
	def __init__(self):
		pass

	def test(self, source=None, **kwargs):
		try:
			Tester.test(self, source)
			
			url_validator = ValidatorFactory.get_validator(ValidatorFactory.URL)

			success  = False
			link     = random.sample(self.links,1)[0]			
			print("[thread_tester][debug] Link: %s" % link.encode("utf-8"))
			url_validator.validate(link)

			engine  = self.prepare_engine()
			engine.set_link_to_crawl(link)
			
			threads = engine.get_threads()
			success = False if len(threads) == 0 else True
			if not success:
				print(fmtstr("[thread_tester][error] Cannot find threads.","red"))
		except CannotOpenURL as cannot_open_url:
			print(fmtstr("[thread_tester][error] %s" % cannot_open_url,"red"))
			success = False
		except ValueError as value_error:
			print(fmtstr("[thread_tester][error] %s" % value_error,"red"))
			success = False
		return success
			