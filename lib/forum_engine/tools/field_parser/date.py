from .    import Parser
from .... import tools

class Date(Parser):
	def __init__(self):
		pass

	def parse(self, value=None):
		assert value       is not None                  , "value is not defined."
		assert type(value) is str or type(value) is list, "incorrect value data type."

		if type(value) is str:
			value = tools._date_parser(value)
		elif type(value) is list:
			value = [tools._date_parser(r) for r in value]
		return value