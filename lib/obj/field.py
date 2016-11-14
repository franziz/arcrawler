from ..exceptions        import NotSupported, CannotSetValue, ParseError
from ..factory.generator import GeneratorFactory
from ..parser.date       import DateParser

class Field:
	name      = None
	single    = True
	concat    = False
	data_type = "string"
	xpath     = None
	_value    = None

	def __init__(self, **kwargs):
		self.domain = kwargs.get("domain",None)

	@property
	def value(self):
		return self._value

	@value.setter
	def value(self,new_value):
		""" Exceptions:
			- CannotSetValue
			- NotSupported
		"""
		if type(new_value) is list:
			new_value = [str(val) for val in new_value]
		if len(new_value) == 0:
			raise CannotSetValue("Cannot set %s since new_value is Nothing" % self.name)

		if self.single and self.concat:
			new_value = "".join(new_value)
		elif self.single and not self.concat:
			new_value = new_value[0] if type(new_value) is list else new_value
		elif not self.single and self.concat:
			raise NotSupported("You request is does not make sense! How come you can 'Not Single' but 'Concat'")

		if self.data_type == "date":
			try:
				parser    = DateParser()
				new_value = parser.parse(new_value)
			except ParseError as ex:
				self.logger.error(str(ex), exc_info=True)
				raise CannotSetValue("You have date error, in that case, the crawler cannot set any value")
		elif self.data_type == "url":
			generator = GeneratorFactory.get_generator(GeneratorFactory.LINK)
			new_value = generator.generate(self.domain, new_value)
		self._value = new_value