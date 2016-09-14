class Palette:
	def __init__(self):
		self.palette = []

	def append(self, palette=[]):
		if type(palette) is list:
			self.palette.extend(palette)
		elif type(palette) is tuple:
			self.palette.append(palette)

	def __iter__(self):
		for palette in self.palette:
			yield palette