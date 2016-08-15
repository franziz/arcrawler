from ..exceptions import FutureDateError
from .            import Validator
import datetime
import copy
import arrow

class FutureDate(Validator):
	def __init__(self):
		pass

	def validate(self, date=None, **kwargs):
		assert date       is not None         , "date is not defined."
		assert type(date) is datetime.datetime, "incorrect date data type."

		Validator.validate(self, **kwargs)
		current_date = arrow.now().replace(days=1).datetime
		maybe_future = copy.copy(date)
		if maybe_future > current_date:
			self.exception = FutureDateError("Future: %s" % maybe_future)
			self.boolean   = False
		else:
			self.boolean = True
		return self._return()

