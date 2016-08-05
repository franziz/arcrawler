from ..    import tools
from .base import Preparator as BasePreparator
import copy
import math

class ThreadPreparator(BasePreparator):
	def __init__(self):
		pass

	def get_links(self, source=None):		
		""" This thread will get all the Thread Link provided by THREAD_LINK_XPATH from source.
			The function is usefull when you need to go all the threads and apply xpath from the thread.
			This function also assume that THREAD_XPATH and THREAD_LINK_XPATH is not wrong.
			So! Please make sure that THREAD_XPATH and THREAD_LINK_XPATH are not wrong to run this function properly

			return:
			['http://threadlink.com/threadid','http://threadlink.com/threadid2']
		"""
		assert source is not None, "source is not defined."

		sample_link_to_crawl = super(ThreadPreparator, self).get_links(source) # Calling this function will only get 10% of overall LINK_TO_CRAWL

		all_thread_links 	 = []
		for link in sample_link_to_crawl:
			page    = source.NETWORK_TOOLS.parse(link)
			threads = tools._xpath(page, source.THREAD_XPATH)
			threads = threads[:math.ceil(len(threads)*0.1)] # Only get top 10% of the data, assuming that 
													  		# all the new post is on top of the list.
													  		# Some questions can be raised from here. For example, 
													  		# Why need to get top list of the thread?
													  		# The answer is simple, I found trouble in parsing a date from
													  		# most recent post. Therefore, the top threads are the most recent
													  		# post.
			for thread in threads:
				thread_links     = tools._xpath(thread, source.THREAD_LINK_XPATH)
				all_thread_links = all_thread_links + copy.deepcopy(thread_links)
		return all_thread_links