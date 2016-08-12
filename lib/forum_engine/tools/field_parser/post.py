from . import Parser
from .... import tools

class Post(Parser):
	def __init__(self):
		pass

	def parse(self, page=None, post_xpath=None):
		assert page       is not None, "page is not defined."
		assert post_xpath is not None, "post_xpath is not defined."
		
		posts = tools._xpath(page, post_xpath)
		return posts

