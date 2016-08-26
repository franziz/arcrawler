from .route     import RouteConfig
from .run       import RunConfig
from .converter import ConverterConfig

class ConfigFactory:
	ROUTE     = 0
	RUN       = 1
	CONVERTER = 2

	def __init__(self):
		pass

	@classmethod
	def get(self, config_name=None):
		assert config_name is not None, "config_name is not defined."
		if config_name == ConfigFactory.ROUTE:
			return RouteConfig()
		elif config_name == ConfigFactory.RUN:
			return RunConfig()
		elif config_name == ConfigFactory.CONVERTER:
			return ConverterConfig()

