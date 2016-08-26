from lib.runners        import Runner
from lib.config.factory import ConfigFactory
import multiprocessing
import time

def execute_worker(name=None, pid=None):
	assert name is not None, "name is not defined."
	assert pid  is not None, "pid is not defined."
	
	runner = Runner(name)
	runner.run()

if __name__ == "__main__":
	run_config = ConfigFactory.get(ConfigFactory.RUN)

	while True:
		workers = list()
		for key, value in run_config.get("run").items():			
			worker = multiprocessing.Process(target=execute_worker, args=(value,key), daemon=False)
			workers.append(worker)
		for worker in workers:
			worker.start()
		for worker in workers:
		 	worker.join()
