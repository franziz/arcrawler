# -*- coding: utf-8 -*-

from ..forum_engine.tools.field_factory import FieldFactory
from ..forum_engine.exceptions		    import NoThreadLink, NoThreadFound, NoPostFound
from ..validator  						import Validator
from ..validator.factory 			    import ValidatorFactory
from ..exceptions  					    import CannotOpenURL, FutureDateError, InvalidDateFormat
from . 				   	   			    import Tester
from curtsies 						    import fmtstr
import random
import math
import arrow

class Date(Tester):
	def __init__(self):
		pass

	def test(self, source=None, props=None, field=None):
		try:
			assert props is not None, "props is not defined."
			assert field is not None, "field is not defined."

			Tester.test(self, source)

			url_validator         = ValidatorFactory.get_validator(ValidatorFactory.URL)
			future_date_validator = ValidatorFactory.get_validator(ValidatorFactory.FUTURE_DATE)
			fields_parser         = FieldFactory.get_parser(FieldFactory.FIELDS)
			date_parser           = FieldFactory.get_parser(FieldFactory.DATE)

			success = False
			stop    = False
			for link in self.links:
				print("[date_tester][debug] Link: %s" % link.encode("utf-8"))
				engine = self.prepare_engine()
				engine.set_link_to_crawl(link)

				threads = engine.get_threads()
				threads = random.sample(threads, math.ceil(len(threads)*0.1))
				if len(threads) == 0: raise NoThreadFound("No thread(s) were found.")				
				for thread in threads:
					thread_link = engine.get_thread_link(thread)
					print("[date_tester][debug] Thread: %s" % thread_link.encode("utf-8"))
					url_validator.validate(thread_link)
					
					engine.current_engine = engine._make_engine(thread_link)
					print("[date_tester][debug] Current Page: %s" % engine.current_engine.current_page_link.encode("utf-8"))

					url_validator.validate(engine.current_engine.current_page_link) # Will throw CannotOpenURL Exception
					posts = engine.current_engine.get_posts(source.POST_XPATH)
					if len(posts) == 0: raise NoPostFound("No post(s) were found.")
					for post in posts:
						result = fields_parser.parse(
							          post = post,
							         xpath = props["xpath"],
							         props = props,
							         field = field
								 )
						result = date_parser.parse(result)

						if not type(result) is list   : result = [result]						
						if None             in result : raise InvalidDateFormat("Invalid data format")

						for maybe_future in result:
							future_date_validator.validate(maybe_future)
						for r in result:
							print("[date_tester][debug] Data: %s" % r)
			success = True # If everything never been raisen, means the test is success
		except NoPostFound as no_post_found:
			print(fmtstr("[date_tester][error] %s" % no_post_found,"red"))
			success = False
		except FutureDateError as future_date:
			print(fmtstr("[date_tester][error] %s" % future_date,"red"))
			success = False
		except InvalidDateFormat as invalid_date_format:
			print(fmtstr("[date_tester][error] %s" % invalid_date_format,"red"))
			success = False
		except NoThreadFound as no_thread_found:
			print(fmtstr("[date_tester][error] %s" % no_thread_found,"red"))
			success = False
		except NoThreadLink as no_thread_link:
			print(fmtstr("[date_tester][error] %s" % no_thread_link,"red"))
			success = False
		except ValueError as value_error:
			print(fmtstr("[date_tester][error] %s" % value_error, "red"))
			success = False
		except CannotOpenURL as cannot_open_url:
			print(fmtstr("[date_tester][error] %s" % cannot_open_url, "red"))
			success = False
		return success
		