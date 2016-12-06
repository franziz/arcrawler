from ..exceptions import ValidationError

class MonitorConfigValidator:
	def validate(self, config=None):
		""" Exceptions:
			- CannotFindField (MonitorConfig.get)
			- AssertionError
			- ValidationError
		"""
		assert config is not None, "config is not defined."

		config = config.get("monitor")
		if "ip" not in config:
			raise ValidationError("ip is not defined.")
		if "port" not in config:
			raise ValidationError("port is not defined.")
		if "database" not in config:
			raise ValidationError("database is not defined.")