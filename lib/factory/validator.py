from ..validator.article       import ArticleValidator
from ..validator.forum_engine  import ForumEngineValidator
from ..validator.sentry_config import SentryConfigValidator

class ValidatorFactory:
	ARTICLE       = 0
	FORUM_ENGINE  = 1
	SENTRY_CONFIG = 2

	def __init__(self):
		pass

	@classmethod
	def get_validator(self, validator_name=None):
		""" Exceptions:
			- AssertionError
		"""
		assert validator_name is not None, "validator_name is not defined."

		if validator_name == ValidatorFactory.ARTICLE:
			return ArticleValidator()
		elif validator_name == ValidatorFactory.FORUM_ENGINE:
			return ForumEngineValidator()
		elif validator_name == ValidatorFactory.SENTRY_CONFIG:
			return SentryConfigValidator()