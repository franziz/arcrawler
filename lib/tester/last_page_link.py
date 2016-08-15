# -*- coding: utf-8 -*-

from ..forum_engine.exceptions import NoThreadLink, NoThreadFound
from ..validator.factory       import ValidatorFactory
from ..network_tools   	       import NetworkTools
from ..exceptions              import CannotOpenURL
from . 					       import Tester
from curtsies	 		       import fmtstr
import random
import math

class LastPageLink(Tester):
	def __init__(self):
		pass

	def test(self, source=None):
		try:
			Tester.test(self, source)

			url_validator = ValidatorFactory.get_validator(ValidatorFactory.URL)

			success = False
			results = []			
			for link in self.links:			
				if success: break
				print("[last_page_link_tester][debug] Link: %s" % link.encode("utf-8"))
				url_validator.validate(link)

				engine = self.prepare_engine()
				engine.set_link_to_crawl(link)

				threads = engine.get_threads()
				threads = random.sample(threads, math.ceil(len(threads) * 0.1))
				if len(threads) == 0: raise NoThreadFound("No thread(s) were found.")				
				for thread in threads:					
					if success: break
					thread_link = engine.get_thread_link(thread) # Assuming thread_link has no error
					print(u"[last_page_link_tester][debug] Thread: %s" % thread_link.encode("utf-8"))
					url_validator.validate(thread_link)

					engine.current_engine = engine._make_engine(thread_link)
					if engine.current_engine.has_last_page:
						print("[last_page_link_tester][debug] Current Page: %s" % engine.current_engine.current_page_link.encode("utf-8"))
						url_validator.validate(engine.current_engine.current_page_link) # Will throw a CannotOpenURL Exception
						success = True # If the code hits this line, means it is a success
			if not success:
				print(fmtstr("[last_page_link_tester][warning] Cannot find last page link. Please check again the xpath","yellow"))
		except NoThreadFound as no_thread_found:
			print(fmtstr("[last_page_link_tester][error] %s" % no_thread_found,"red"))
			success = False
		except NoThreadLink as no_thread_link:
			print(fmtstr("[last_page_link_tester][error] %s" % no_thread_link,"red"))
			success = False
		except ValueError as value_error:
			print(fmtstr("[last_page_link_tester][error] %s" % value_error, "red"))
			success = False
		except CannotOpenURL as cannot_open_url:
			print(fmtstr("[last_page_link_tester][error] %s" % cannot_open_url,"red"))
			success = False
		return success