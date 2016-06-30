from lib.runners import Runner
from lib         import builder
from pymongo     import MongoClient
import multiprocessing

def execute_worker(name=None):
	assert name is not None, "name is not defined."
	runner = Runner(name)
	runner.run()

if __name__ == "__main__":
	config = builder.read_config_file()
	assert "run" in config, "run is not defined."	

	db = MongoClient("mongodb://mongo:27017/test")
	db = db.monitor

	for key, value in config["run"].items():		
		# TODO: check if name is in database
		worker = multiprocessing.Process(target=execute_worker, args=(value,), daemon=False)
		worker.start()