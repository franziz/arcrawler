from ..writer.crawler import CrawlerWriter
from ..writer.run     import RunConfigWriter
from ..writer.sentry  import SentryConfigWriter
from ..writer.route   import RouteConfigWriter
from ..writer.monitor import MonitorConfigWriter

class WriterFactory:
	CRAWLER    	   = 0
	RUN_CONFIG 	   = 1
	SENTRY_CONFIG  = 2
	ROUTE_CONFIG   = 3
	MONITOR_CONFIG = 4

	def __init__(self):
		pass

	@classmethod
	def get_writer(self, writer_name=None):
		""" Exceptions: 
			- AssertionError
		""" 
		assert writer_name is not None, "writer_name is not defined."

		if writer_name == WriterFactory.CRAWLER:
			return CrawlerWriter()
		elif writer_name == WriterFactory.RUN_CONFIG:
			return RunConfigWriter()
		elif writer_name == WriterFactory.SENTRY_CONFIG:
			return SentryConfigWriter()
		elif writer_name == WriterFactory.ROUTE_CONFIG:
			return RouteConfigWriter()
		elif writer_name == WriterFactory.MONITOR_CONFIG:
			return MonitorConfigWriter()