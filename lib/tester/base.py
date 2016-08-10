from .exceptions import TestIsNotPassed
from .. 		 import tools
import random

class Tester(object):
	def __init__(self):
		pass

	def test(self, object_to_test=None, link=None):
		try:
			assert object_to_test is not None, "object_to_test is not defined."

			if len(object_to_test) == 0:
				raise TestIsNotPassed("No test object.")
		except:
			raise TestIsNotPassed("No test object.")

class FieldTester(Tester):
	def __init__(self, **kwargs):			
		self.source = kwargs.get("source", None)
		self.concat = kwargs.get("concat", False)
		self.single = kwargs.get("single", True)

	def test(self, object_to_test=None):
		pass

	def _prepare_value(self, value=None):
		try:
			assert value is not None, "value is not defined."
			# TODO: Because this codes below are similar to forum_engine/engine.py
			#		you need to make it a class. So that, there will be no duplicate.

			if (self.single and self.concat) or (not self.single and self.concat):
				value = " ".join(value)
				value = str(value)
			elif self.single and not self.concat:
				value = value[0] if type(value) is list and len(value)>0 else value
				value = str(value)
			else:
				value = list(value)
			#end if
			
			assert type(value) is str or type(value) is list

			# removing some unwanted data such as \xc2\xa0
			if type(value) is str:
				value = tools._clean_string(value)
			elif type(value) is list:
				value = [tools._clean_string(r) for r in value]
			#end if
			return value
		except AssertionError:
			raise TestIsNotPassed("Assertion is not passed.")
		except TypeError:
			raise TestIsNotPassed("TypeError occured! Could be because of XPATH problem.")
#end class
		