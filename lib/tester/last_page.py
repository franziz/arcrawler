from .base import Tester as BaseTester

class LastPageTester(BaseTester):
	def __init__(self, source=None):
		self.source = source
		pass

	def test(self, object_to_test=None, link=None):
		""" The test function of LastPageTester will not throw any exception
			because of the nature of LastPage. Some of the forum can have 0 last page
		"""
		assert object_to_test is not None, "object_to_test is not defined."
		assert self.source    is not None, "source is not defined."

		if len(object_to_test) == 0:
			print("[test][warning][{}] Cannot find Last Page".format(self.source.CRAWLER_NAME))
