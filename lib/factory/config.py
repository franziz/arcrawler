from ..config.run       import RunConfig
from ..config.route     import RouteConfig

class ConfigFactory:
	RUN       = 0
	ROUTE     = 1

	def __init__(self):
		pass

	@classmethod
	def get_config(self, config_name=None):
		assert config_name is not None, "config_name is not defined."

		if config_name == ConfigFactory.RUN:
			return RunConfig()
		elif config_name == ConfigFactory.ROUTE:
			return RouteConfig()