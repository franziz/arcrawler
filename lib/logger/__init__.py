from raven.conf 		    import setup_logging
from raven.handlers.logging import SentryHandler
import raven
import logging

class Logger(raven.Client):
	def __init__(self, **kwargs):
		self.dsn = "http://3ad4e70e205c4eb793061be7527d9d7d:472435681da448a583d219164febf92c@sentry:9000/2"
		raven.Client.__init__(self, self.dsn, auto_log_stacks=True, **kwargs)

		self.handler = SentryHandler(self)
		setup_logging(self.handler)