from lib.factory.config import ConfigFactory
from lib.monitor        import Monitor
from lib.exceptions     import CannotFindThread, IncorrectXPATHSyntax, CannotFindArticleLink, ValidationError, CannotFindField
from curtsies 			import fmtstr
from multiprocessing    import Pool
from lib.logger         import Logger
import time
import glob
import os
import importlib
import random
import logging

def execute_worker(crawler_name=None):
	logger = logging.getLogger(__name__)
	try:
		assert crawler_name is not None, "crawler_name is not defined."
		module  = importlib.import_module("crawlers.%s" % crawler_name)
		crawler = module.Crawler()
		crawler.crawl()
	except CannotFindThread as ex:
		logger.error(str(ex), exc_info=True)
	except IncorrectXPATHSyntax as ex:
		logger.error(str(ex), exc_info=True)
	except CannotFindArticleLink as ex:
		logger.error(str(ex), exc_info=True)
	except AssertionError as ex:
		logger.error(str(ex), exc_info=True)
	except CannotFindField as ex:
		logger.error(str(ex), exc_info=True)
	except ValidationError as ex:
		logger.error(str(ex), exc_info=True)


if __name__ == "__main__":
	""" Exceptions:
		- AssertionError (Monitor)
		- CannotFindField (Monitor)
		- ValidationError (Monitor)
	"""
	Logger()
	monitor = Monitor()

	while True:
		run_config    = ConfigFactory.get_config(ConfigFactory.RUN)
		crawler_names = run_config.get("run")
		section_name  = run_config.get("section")

		# monitor.capture_section_start(name=section_name.title())
		for crawler_name in crawler_names:
			# monitor.capture_crawler_start(name=crawler_name.title())
			name 	   = crawler_name.replace(" ","_")
			name       = name.lower()
			crawlers   = []
			print("[run][debug] Preparing %s" % name)
			for file_name in glob.iglob(os.path.join(os.getcwd(),"crawlers","%s_*.py" % name)):
				file_name = file_name.replace(os.getcwd(),"")
				file_name = file_name.replace("crawlers","")
				file_name = file_name.replace(".py","")
				file_name = file_name.replace("/","")
				crawlers.append(file_name)
			print("[run][debug] Crawling...")
			run_config = ConfigFactory.get_config(ConfigFactory.RUN)
			workers    = run_config.get("workers")
			with Pool(workers) as pool:
				pool.map(execute_worker, crawlers)
			# monitor.capture_crawler_stop(name=crawler_name.title())
		# monitor.capture_section_stop(name=section_name.title())

		rnd = random.randint(60,360)
		print(fmtstr("[run][debug] Sleeping %s seconds" % rnd, "yellow"))
		time.sleep(rnd)