import os
import bson.json_util
import copy

class RouteConfigWriter:
	def __init__(self):
		pass

	def write(self, route=None, **kwargs):
		assert route is not None, "route is not defined."

		location = kwargs.get("location", os.getcwd())
		location = os.path.join(location,"config")

		if not os.path.isdir(location): os.makedirs(location)

		copy_from = kwargs.get("copy_from", os.path.join(os.getcwd(),"config","route.json"))

		old_route = {}
		with open(copy_from, "r") as file:
			old_route = bson.json_util.loads(file.read())
			file.flush()
			file.close()
		new_route = copy.deepcopy(old_route)
		new_route["cd_server"].update({"route":route})
		with open(os.path.join(location,"route.json"), "w") as file:
			file.write(bson.json_util.dumps(new_route, indent=4))
			file.flush()
			file.close()
		return True