class Section:
	def __init__(self, **kwargs):
		self.name    = kwargs.get("name",None)
		self.workers = kwargs.get("workers",10)
		self.items   = kwargs.get("items",[])