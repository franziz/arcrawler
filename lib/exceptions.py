class DuplicateKeyError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class PageNotFound(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)
		
class IncorrectXPATHSyntax(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class NotSupported(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class ParseError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class CannotFindThreadLink(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class CannotFindField(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class CannotFindCrawler(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class CannotSetValue(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)