from ..config.run     import RunConfig
from ..config.route   import RouteConfig
from ..config.sentry  import SentryConfig
from ..config.monitor import MonitorConfig

class ConfigFactory:
	RUN     = 0
	ROUTE   = 1
	SENTRY  = 2
	MONITOR = 3

	def __init__(self):
		pass

	@classmethod
	def get_config(self, config_name=None):
		""" Exceptions:
			- AssertionError
		"""
		assert config_name is not None, "config_name is not defined."

		if config_name == ConfigFactory.RUN:
			return RunConfig()
		elif config_name == ConfigFactory.ROUTE:
			return RouteConfig()
		elif config_name == ConfigFactory.SENTRY:
			return SentryConfig()
		elif config_name == ConfigFactory.MONITOR:
			return MonitorConfig()