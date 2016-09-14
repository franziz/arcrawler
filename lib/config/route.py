from . import Config
import os
import json

class RouteConfig(Config):
	def __init__(self):
		Config.__init__(self, os.path.join(".","config","route.json"))

	def change_cd_server_route(self, **kwargs):
		new_route = kwargs.get("to",None)
		new_route = kwargs.get("new_route", new_route)

		assert new_route       is not None, "new_route is not defined."
		assert type(new_route) is str     , "incorrect new_route data type."
		
		self.config["cd_server"]["route"] = new_route
		self.write(self.config)