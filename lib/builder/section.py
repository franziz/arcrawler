class Section:
	def __init__(self, **kwargs):
		self.name  = kwargs.get("name",None)
		self.items = kwargs.get("items",[])