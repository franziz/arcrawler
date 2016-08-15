class Validator:
	class ReturnType:
		EXCEPTION = 0
		BOOLEAN   = 1

	def __init__(self):
		pass

	def validate(self, **kwargs):
		self.return_type = kwargs.get("return_type",Validator.ReturnType.EXCEPTION)
		self.boolean     = None
		self.exception   = None

	def _return(self, boolean=None, exception=None):
		boolean   = self.boolean if boolean is None else boolean
		exception = self.exception if exception is None else exception

		assert boolean is not None, "boolean is not defined."
		if boolean == False and self.return_type == Validator.ReturnType.EXCEPTION:
			raise exception
		else:
			return boolean
