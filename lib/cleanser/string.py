import copy

class StringCleanser:
	def __init__(self):
		pass

	def clean(self, string=None):
		""" Exceptions:
			- AssertionError
		"""
		assert string is not None, "string is not defined."

		new_string = copy.copy(string)
		new_string = new_string.replace("\r", " ")
		new_string = new_string.replace("\t", " ")
		new_string = new_string.replace("\n", " ")
		return new_string