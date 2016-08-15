# -*- coding: utf-8 -*-

from ..forum_engine.exceptions import NoPrevious, NoThreadLink, NoThreadFound
from ..forum_engine.engine     import Engine
from ..network_tools  		   import NetworkTools
from ..validator.factory	   import ValidatorFactory
from ..exceptions   		   import CannotOpenURL
from .                         import Tester
from curtsies		    	   import fmtstr
import random
import math

class PrevLink(Tester):
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
				print("[prev_link_tester][debug] Link: %s" % link.encode("utf-8"))
				engine = self.prepare_engine()
				engine.set_link_to_crawl(link)

				threads = engine.get_threads()
				threads = random.sample(threads, math.ceil(len(threads) * 0.1))
				if len(threads) == 0: raise NoThreadFound("No thread(s) were found.")
				for thread in threads:
					if success: break
					thread_link = engine.get_thread_link(thread) # Assuming thread_link has no error
					print(u"[prev_link_tester][debug] Thread: %s" % thread_link.encode("utf-8"))
					url_validator.validate(thread_link)
					
					engine.current_engine = engine._make_engine(thread_link)

					# The logic behind this is, if the current_page has last page
					# It means that the prev_link should be available.
					# If cannot find prev_link, it will throw an exception Noprevious()
					# which is the mart of the end of the iteration
					if engine.current_engine.has_last_page:
						print("[prev_link_tester][debug] Current Page: %s" % engine.current_engine.current_page_link.encode("utf-8"))
						prev_link = engine.current_engine.get_prev_link() # Will throw NoPrevious
						print("[prev_link_tester][debug] Prev Link: %s" % prev_link.encode("utf-8"))
						url_validator.validate(prev_link) # Will throw CannotOpenURL exception
						success = True # If the code hits this line, means it is success
			if not success:
				print(fmtstr("[prev_link_tester][warning] Beware! Are you sure you dont have prev_link?","yellow"))
		except NoThreadFound as no_thread_found:
			print(fmtstr("[prev_link_tester][error] %s" % no_thread_found,"red"))
			success = False
		except NoThreadLink as no_thread_link:
			print(fmtstr("[prev_link_tester][error] %s" % no_thread_link,"red"))
			success = False
		except NoPrevious as no_prev:
			print(fmtstr("[prev_link_tester][error] %s" % no_prev,"red"))
			success = False
		except ValueError as value_error:
			print(fmtstr("[prev_link_tester][error] %s" % value_error,"red"))
			success = False
		except CannotOpenURL as cannot_open_url:
			print(fmtstr("[prev_link_tester][error] %s" % cannot_open_url,"red"))
			success = False
		return success