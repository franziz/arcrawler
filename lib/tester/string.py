from .base 		 import FieldTester
from .exceptions import TestIsNotPassed
import copy

class StringTester(FieldTester):
	def __init__(self, **kwargs):
		super(StringTester, self).__init__(**kwargs)

	def test(self, object_to_test):
		assert object_to_test is not None, "object_to_test is not defined."

		string = copy.copy(object_to_test)
		string = self._prepare_value(string)

		if type(string) is str:
			if not string:
				raise TestIsNotPassed("String cannot be empty")
		elif type(string) is list:
			if len(string) == 0:
				raise TestIsNotPassed("String cannot be empty")
		#end if