from . import Config
import os

class ConverterConfig(Config):
	def __init__(self):
		Config.__init__(self, os.path.join(".","config","converter.json"))

	@property
	def target_connection_string(self):
		config = self.config.get("converter")["target"]
		assert "ip" in config, "ip is not defined."
		
		if "username" in config and "password" in config and "authenticationDatabase" in config:
			connection_string = "mongodb://{username}:{password}@{ip}/test?authSource={authenticationDatabase}"
			connection_string = connection_string.format(
									              username = config["username"],
									              password = config["password"],
									                    ip = config["ip"],
									authenticationDatabase = config["authenticationDatabase"]
								)
		else:
			connection_string = "mongodb://{ip}:27017/test"
			connection_string = connection_string.format(ip=config["ip"])
		return connection_string