from raven.conf 		    import setup_logging
from raven.handlers.logging import SentryHandler
import raven
import logging

class Logger(raven.Client):
	def __init__(self, **kwargs):
		self.public_key = "5570134675474d8682b476c6da319812"
		self.secret_key = "000f2481edcb4eda870c7d05f0126f3a"
		self.project_id = 2

		self.dsn = "http://%s:%s@sentry:9000/%s" % (
			self.public_key,
			self.secret_key,
			self.project_id
		)
		raven.Client.__init__(self, self.dsn, auto_log_stacks=True, **kwargs)

		self.handler = SentryHandler(self)
		setup_logging(self.handler)