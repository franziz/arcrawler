from raven.conf 		    import setup_logging
from raven.handlers.logging import SentryHandler
import raven
import logging

class Logger(raven.Client):
	def __init__(self, **kwargs):
		self.public_key = "18c90be1b6da4d78a8bf375354f0ea53"
		self.secret_key = "11a8c866ce2340529c8cf20e84f629af"
		self.project_id = 3

		self.dsn = "http://%s:%s@sentry:9000/%s" % (
			self.public_key,
			self.secret_key,
			self.project_id
		)
		raven.Client.__init__(self, self.dsn, auto_log_stacks=True, **kwargs)

		self.handler = SentryHandler(self)
		setup_logging(self.handler)