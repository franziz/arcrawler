from .    import Parser
from .... import tools

class URL(Parser):
	def __init__(self):
		pass

	def parse(self, value=None, domain=None):
		assert value       is not None				    , "value is not defined."
		assert type(value) is str or type(value) is list, "incorrect value data type."
		assert domain      is not None                  , "domain is not defined."

		if type(value) is str:
			value = tools._expand_link(domain=domain, link=value)			
		elif type(value) is list:
			value = [tools._expand_link(domain=domain, link=r) for r in value if "http://" not in r]
		return value