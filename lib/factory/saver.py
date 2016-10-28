from ..saver.post    import PostSaver
from ..saver.meta    import MetaSaver
from ..saver.article import ArticleSaver
from ..saver.blog    import BlogSaver

class SaverFactory:
	POST 	= 0 
	META 	= 1
	ARTICLE = 2
	BLOG    = 3

	def __init__(self):
		pass

	@classmethod
	def get_saver(self, saver_name=None):
		assert saver_name is not None, "saver_name is not defined."

		if saver_name == SaverFactory.POST:
			return PostSaver()
		elif saver_name == SaverFactory.META:
			return MetaSaver()
		elif saver_name == SaverFactory.ARTICLE:
			return ArticleSaver()
		elif saver_name == SaverFactory.BLOG:
			return BlogSaver()