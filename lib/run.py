from lib.factory.config import ConfigFactory
from lib.monitor        import Monitor
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
	try:
		assert crawler_name is not None, "crawler_name is not defined."
		module  = importlib.import_module("crawlers.%s" % crawler_name)
		crawler = module.Crawler()
		crawler.crawl()
	except:
		logger = logging.getLogger(__name__)
		logger.error("Something is wrong!", exc_info=True)

if __name__ == "__main__":
	Logger()
	while True:
		run_config    = ConfigFactory.get_config(ConfigFactory.RUN)
		crawler_names = run_config.get("run")
		section_name  = run_config.get("section")
		section_id    = Monitor.section_start(name=section_name)
		for crawler_name in crawler_names:
			process_id = Monitor.crawler_start(crawler_name.title())
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
			Monitor.crawler_stop(process_id)
		Monitor.section_stop(id=section_id)

		rnd = random.randint(60,360)
		print(fmtstr("[run][debug] Sleeping %s seconds" % rnd, "yellow"))
		time.sleep(rnd)