class ConfigNotFound(Exception):
	def __init__(self,value):
		self.value = value
	#end def

	def __str__(self):
		return repr(self.value)
	#end def
#end class

class CannotFindField(Exception):
	def __init__(self,value):
		self.value = value
	#end def

	def __str__(self):
		return repr(self.value)
	#end def
#end class


class CommandError(Exception):
	def __init__(self,value):
		self.value = value
	#end def

	def __str__(self):
		return repr(self.value)
	#end def
#end class

class InvalidConfigFormat(Exception):
	def __init__(self,value):
		self.value = value
	#end def

	def __str__(self):
		return repr(self.value)
	#end def
#end class

class InvalidDateFormat(BaseException):
	def __init__(self,value):
		self.value = value
	#end def

	def __str__(self):
		return repr(self.value)
	#end def
#end class

class FutureDateError(BaseException):
	def __init__(self,value):
		self.value = value
	#end def

	def __str__(self):
		return repr(self.value)
	#end def
#end class

class CannotOpenURL(BaseException):
	def __init__(self,value):
		self.value = value
	#end def

	def __str__(self):
		return repr(self.value)
	#end def
#end class

class PageNotFound(Exception):
	def __init__(self,value):
		self.value = value
	#end def

	def __str__(self):
		return repr(self.value)
	#end def
#end class