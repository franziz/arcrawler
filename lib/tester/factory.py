from .thread_link 	 import ThreadLink   as ThreadLinkTester
from .thread  	  	 import Thread       as ThreadTester
from .last_page_link import LastPageLink as LastPageLinkTester
from .prev_link  	 import PrevLink 	 as PrevLinkTester
from .post 			 import Post  		 as PostTester
from .date   		 import Date 		 as DateTester
from .url 			 import URL 		 as URLTester
from .content   	 import Content    	 as ContentTester
import glob
import importlib

class TesterFactory:
	THREAD         = 0
	THREAD_LINK    = 1
	LAST_PAGE_LINK = 2
	PREV_LINK      = 3
	POST           = 4
	DATE           = 5
	URL 		   = 6
	CONTENT  	   = 7

	def __init__(self):
		pass

	def get_tester(self, tester_name):
		if tester_name == TesterFactory.THREAD:
			return ThreadTester()
		if tester_name == TesterFactory.THREAD_LINK:
			return ThreadLinkTester()
		if tester_name == TesterFactory.LAST_PAGE_LINK:
			return LastPageLinkTester()
		if tester_name == TesterFactory.PREV_LINK:
			return PrevLinkTester()
		if tester_name == TesterFactory.POST:
			return PostTester()
		if tester_name == TesterFactory.DATE:
			return DateTester()
		if tester_name == TesterFactory.URL:
			return URLTester()
		if tester_name == TesterFactory.CONTENT:
			return ContentTester()

	def get_sources(self):
		sources 	 = []
		source_files = glob.iglob("./src/*.py")
		for file in source_files:
			source = file.replace("./src/","").replace(".py","")
			source = importlib.import_module("src.{}".format(source))
			source = source.Crawler()
			sources.append(source)
		return sources
