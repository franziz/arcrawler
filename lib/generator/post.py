import arrow

class PostDataGenerator:
	def __init__(self):
		pass

	def generate(self, post=None, **kwargs):
		assert post       is not None, "post is not defined."
		assert type(post) is dict    , "incorrect post data type."
			
		post.update({"_insert_time": arrow.now().datetime})
		post.update({"converted":False})
		post.update({"TTL":arrow.utcnow().datetime})
		for key,value in kwargs.items():
			key = "_%s" % key
			post.update({key:value})
		return post