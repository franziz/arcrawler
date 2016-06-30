from pymongo import MongoClient
from tqdm    import tqdm
import multiprocessing
import importlib

class Runner(object):
	def __init__(self, crawler_names=[]):
		self.crawler_names = crawler_names if type(crawler_names) is list else [crawler_names]

	def run(self):
		db = MongoClient("mongodb://mongo:27017/test")
		db = db.monitor

		documents = list()
		for name in self.crawler_names:
			crawlers  = db.queue.find({
							       "name":name,
							     "status":"idle", 
							"is_deployed":True
						})
			crawlers  = tqdm(crawlers)
			crawlers.set_description("[arcrawler] Extracting database...")

			crawlers  = [crawler for crawler in crawlers]
			documents = documents + crawlers
		documents = tqdm(documents)
		crawlers  = list()
		for document in documents:
			documents.set_description("[arcrawler] Fetching queue...")
			crawlers.append(document)
		workers = multiprocessing.Pool(10)
		workers.map(self._execute_worker, crawlers)

	def _execute_worker(self,crawler=None):
		assert crawler is not None
		crawler_path = "build.crawlers.{}".format(crawler["hash"])
		crawler      = importlib.import_module(crawler_path)
		crawler      = crawler.Crawler()
		crawler.crawl()