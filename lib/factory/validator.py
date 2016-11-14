from ..validator.article      import ArticleValidator
from ..validator.forum_engine import ForumEngineValidator

class ValidatorFactory:
	ARTICLE      = 0
	FORUM_ENGINE = 1

	def __init__(self):
		pass

	@classmethod
	def get_validator(self, validator_name=None):
		assert validator_name is not None, "validator_name is not defined."

		if validator_name == ValidatorFactory.ARTICLE:
			return ArticleValidator()
		elif validator_name == ValidatorFactory.FORUM_ENGINE:
			return ForumEngineValidator()