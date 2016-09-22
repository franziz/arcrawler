import os
import copy
import bson.json_util

class ConverterConfigWriter:
	def __init__(self):
		pass

	def write(self, **kwargs):
		copy_from = kwargs.get("copy_from", None)
		crawlers  = kwargs.get("crawlers", {})
		location  = kwargs.get("location", os.path.join(os.getcwd()))
		location  = os.path.join(location,"config")

		if not os.path.isdir(location): os.makedirs(location)

		old_config = {}
		if copy_from is not None:
			file       = open(copy_from,"r")
			old_config = bson.json_util.loads(file.read())
			file.flush()
			file.close()
		new_config = copy.deepcopy(old_config)
		new_config.update({"crawlers":crawlers})

		with open(os.path.join(location,"converter.json"),"w") as file:
			file.write(bson.json_util.dumps(new_config, indent=4))
			file.flush()
			file.close()
		return True