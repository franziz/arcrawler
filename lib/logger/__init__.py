from raven.conf 		    import setup_logging
from raven.handlers.logging import SentryHandler
import raven
import logging

class Logger(raven.Client):
	def __init__(self, **kwargs):
		self.public_key = "3ad4e70e205c4eb793061be7527d9d7d"
		self.secret_key = "472435681da448a583d219164febf92c"
		self.project_id = 2

		self.dsn = "http://%s:%s@sentry:9000/%s" % (
			self.public_key,
			self.secret_key,
			self.project_id
		)
		raven.Client.__init__(self, self.dsn, auto_log_stacks=True, **kwargs)

		self.handler = SentryHandler(self)
		setup_logging(self.handler)