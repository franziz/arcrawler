from .url         import URL as URLValidator
from .future_date import FutureDate as FutureDateValidator

class ValidatorFactory:
	URL         = 0
	FUTURE_DATE = 1

	def __init__(self):
		pass

	@classmethod
	def get_validator(self, validator_name=None):
		assert validator_name is not None, "validator_name is not defined."

		if validator_name == ValidatorFactory.URL:
			return URLValidator()
		elif validator_name == ValidatorFactory.FUTURE_DATE:
			return FutureDateValidator()