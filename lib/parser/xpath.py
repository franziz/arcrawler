from ..exceptions import IncorrectXPATHSyntax
import lxml

class XPATHParser:
	def __init__(self):
		pass

	def parse(self, element=None, xpath=None):
		""" Exceptions
			- AssertionError
			- IncorrectXPATHSyntax
		"""
		assert element is not None, "element is not defined."
		assert xpath   is not None," xpath is not defined."
	
		try:
			if "re:test" in xpath:
				regexpNS = "http://exslt.org/regular-expressions"
				result   = element.xpath(xpath,namespaces={'re':regexpNS})
			else:
				result = element.xpath(xpath)
		except lxml.etree.XPathEvalError as invalid_expression:
			raise IncorrectXPATHSyntax("Following syntax is not correct: %s" % xpath)
		except UnicodeDecodeError:
			result = None
		return result