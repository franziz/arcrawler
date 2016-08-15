from .               import Validator
from ..network_tools import NetworkTools
from ..exceptions    import CannotOpenURL

class URL(Validator):
	def __init__(self):
		pass		

	def validate(self, url=None, **kwargs):
		assert url is not None, "link is not defined."

		Validator.validate(self, **kwargs)

		network_tools = kwargs.get("network_tools",NetworkTools(use_proxy=False))
		page          = network_tools.parse(url, parse=False)
		if str(page) == "<html></html>":
			self.boolean   = False
			self.exception = CannotOpenURL("Invalid url.")
		else:
			self.boolean = True
		return self._return()



