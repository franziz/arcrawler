class ForumEngineValidator:
	def __init__(self):
		pass

	@classmethod
	def validate(self, forum_engine=None):
		""" This function will throw:
			- AssertionError
		"""

		assert forum_engine 		  		  is not None, "forum_engine is not defined."
		assert forum_engine.name 			  is not None, "name is not defined."
		assert forum_engine.link_to_crawl 	  is not None, "link_to_crawl is not defined."
		assert forum_engine.country       	  is not None, "country is not defined."
		assert forum_engine.thread_xpath  	  is not None, "thread_xpath is not defined."
		assert forum_engine.thread_link_xpath is not None, "thread_link_xpath is not defined."
		assert forum_engine.last_page_xpath   is not None, "last_page_xpath is not defined."
		assert forum_engine.prev_xpath 		  is not None, "prev_xpath is not defined."
		assert forum_engine.post_xpath   	  is not None, "post_xpath is not defined."
		assert forum_engine.fields 			  is not None, "fields is not defined."