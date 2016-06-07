class NoPrevious(Exception):
	def __init__(self,value):
		self.value = value
	#end def

	def __str__(self):
		return repr(self.value)
	#end def
#end class

class NoThreadLink(Exception):
	def __init__(self,value):
		self.value = value
	#end def

	def __str__(self):
		return repr(self.value)
	#end def
#end class

class DuplicateData(Exception):
	def __init__(self,value):
		self.value = value
	#end def

	def __str__(self):
		return repr(self.value)
	#end def
#end class

class CannotFindXPATH(Exception):
	def __init__(self,value):
		self.value = value
	#end def

	def __str__(self):
		return repr(self.value)
	#end def
#end class

def MaxTryExceeded(Exception):
	def __init__(self,value):
		self.value = value
	#end def

	def __str__(self):
		return repr(self.value)
	#end def
#end class