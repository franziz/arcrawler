from ..generator.post import PostDataGenerator
from ..generator.link import LinkGenerator

class GeneratorFactory:
	POST_DATA = 0
	LINK      = 1

	def __init__(self):
		pass

	@classmethod
	def get_generator(self, generator_name=None):
		assert generator_name is not None, "generator_name is not defined."

		if generator_name == GeneratorFactory.POST_DATA:
			return PostDataGenerator()
		elif generator_name == GeneratorFactory.LINK:
			return LinkGenerator()