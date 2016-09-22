from ..config.run       import RunConfig
from ..config.converter import ConverterConfig
from ..config.route     import RouteConfig

class ConfigFactory:
	RUN       = 0
	CONVERTER = 1
	ROUTE     = 2

	def __init__(self):
		pass

	@classmethod
	def get_config(self, config_name=None):
		assert config_name is not None, "config_name is not defined."

		if config_name == ConfigFactory.RUN:
			return RunConfig()
		elif config_name == ConfigFactory.CONVERTER:
			return ConverterConfig()
		elif config_name == ConfigFactory.ROUTE:
			return RouteConfig()