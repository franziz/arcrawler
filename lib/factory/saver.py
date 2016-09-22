from ..saver.post import PostSaver

class SaverFactory:
	POST = 0 

	def __init__(self):
		pass

	@classmethod
	def get_saver(self, saver_name=None):
		assert saver_name is not None, "saver_name is not defined."

		if saver_name == SaverFactory.POST:
			return PostSaver()