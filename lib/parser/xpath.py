from ..exceptions import IncorrectXPATHSyntax

class XPATHParser:
	def __init__(self):
		pass

	def parse(self, element=None, xpath=None):
		assert element is not None, "element is not defined."
		assert xpath   is not None," xpath is not defined."
	
		if "re:test" in xpath:
			try:
				regexpNS = "http://exslt.org/regular-expressions"
				result   = element.xpath(xpath,namespaces={'re':regexpNS})
			except lxml.etree.XPathEvalError as invalid_expression:
				raise IncorrectXPATHSyntax("Following syntax is not correct: %s" % xpath)
			except UnicodeDecodeError:
				result = None
		else:
			try:
				result = element.xpath(xpath)
			except UnicodeDecodeError:
				result = None
		return result