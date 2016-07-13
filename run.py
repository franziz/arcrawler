from lib.runners import Runner
from lib         import builder
from pymongo     import MongoClient
import multiprocessing
import time

def execute_worker(name=None, pid=None):
	assert name is not None, "name is not defined."
	assert pid  is not None, "pid is not defined."
	
	runner = Runner(name)
	runner.run()

if __name__ == "__main__":
	config = builder.read_config_file()
	assert "run" in config, "run is not defined."	

	db = MongoClient("mongodb://mongo:27017/test")
	db = db.monitor


	workers = list()
	for key, value in config["run"].items():		
		print(value)
		# TODO: check if name is in database
		worker = multiprocessing.Process(target=execute_worker, args=(value,key), daemon=False)
		workers.append(worker)
	for worker in workers:
		worker.start()
