import json

class Config(object):
	def __init__(self):
		self._config  = None
		self.location = "/root/app/config.json"
		self.read()

	@property
	def config(self):
		if self._config is None:
			return dict()
		else:
			return self._config
	

	def read(self):
		f            = open(self.location,"r")
		self._config = json.load(f)