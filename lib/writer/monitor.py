import os
import shutil

class MonitorConfigWriter:
	def write(self, **kwargs):
		destination = kwargs.get("location", os.path.join(os.getcwd()))
		destination = os.path.join(destination, "config")

		if not os.path.isdir(destination):
			os.makedirs(destination)

		destination = os.path.join(destination, "monitor.json")
		source 	    = os.path.join(os.getcwd(), "config", "monitor.json")
		shutil.copyfile(source, destination)