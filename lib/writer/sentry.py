import os
import shutil

class SentryConfigWriter:
	def write(self, **kwargs):
		destination = kwargs.get("location", os.path.join(os.getcwd()))
		destination = os.path.join(destination, "config")

		if not os.path.isdir(destination):
			os.makedirs(destination)

		destination = os.path.join(destination, "sentry.json")
		source 	    = os.path.join(os.getcwd(), "config", "sentry.json")
		shutil.copyfile(source, destination)