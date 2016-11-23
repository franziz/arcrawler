import os
import bson.json_util

class RunConfigWriter:
	def __init__(self):
		pass

	def write(self, **kwargs):
		""" Exceptions:
			- AssertionError
		"""
		workers  = kwargs.get("workers",10)
		section  = kwargs.get("section",None)
		run      = kwargs.get("run",None)
		location = kwargs.get("location", os.path.join(os.getcwd()))
		location = os.path.join(location,"config")

		assert section is not None, "section is not defined."
		assert run     is not None, "run is not defined."

		if not os.path.isdir(location):
			os.makedirs(location)

		document = {
			"workers" : workers,
			"section" : section,
			    "run" : run
		}

		with open(os.path.join(location, "run.json"),"w") as file:
			file.write(bson.json_util.dumps(document, indent=4))
			file.flush()
			file.close()

