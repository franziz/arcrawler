from ..config.factory import ConfigFactory
import multiprocessing
import importlib
import os
import glob
import copy

class Runner(object):
	def __init__(self, crawler_names=[]):
		self.crawler_names = crawler_names if type(crawler_names) is list else [crawler_names]
		self.config        = ConfigFactory.get(ConfigFactory.RUN)				

	def run(self):
		crawlers_folder = os.path.join(".","crawlers")
		crawlers        = []
		for crawler_name in self.crawler_names:
			crawler_name = crawler_name.lower()
			crawler_name = crawler_name.replace(" ","_")				
			for file_name in glob.iglob("%s/%s_*.py" % (crawlers_folder, crawler_name)):
				file_name = file_name.replace(crawlers_folder,"")
				file_name = file_name.replace("/","")
				file_name = file_name.replace(".py","")
				crawlers.append(copy.copy(file_name))
		workers = multiprocessing.Pool(int(self.config.get("workers")))
		workers.map(self._execute_worker, crawlers)

	def _execute_worker(self, crawler_name=None):
		assert crawler_name is not None, "crawler_name is not defined."

		crawler_path = "crawlers.{}".format(crawler_name)
		crawler      = importlib.import_module(crawler_path)
		crawler      = crawler.Crawler()
		crawler.crawl()