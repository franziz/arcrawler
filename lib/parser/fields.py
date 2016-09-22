from ..obj.field import Field

class FieldsParser:

	def __init__(self, **kwargs):
		self.domain = kwargs.get("domain", None)

	def parse(self, fields=None):
		assert fields       is not None, "fields is not defined."
		assert type(fields) is list    , "incorrect fields data type."

		parsed_fields = {}
		for field in fields:
			for key,values in field.items():
				if values["data_type"] == "url":
					parsed_field = Field(domain=self.domain)
				else:
					parsed_field = Field()
				parsed_field.name      = key
				parsed_field.single    = values["single"]
				parsed_field.concat    = values["concat"]
				parsed_field.data_type = values["data_type"]
				parsed_field.xpath     = values["xpath"]
				parsed_fields.update({key:parsed_field})
		return parsed_fields