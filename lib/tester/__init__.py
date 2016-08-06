from ..       		  import tools, exceptions
from .base    		  import Tester as BaseTester
from .preparator.base import Preparator as BasePreparator
from curtsies 		  import fmtstr
import glob
import importlib
import lxml

class Tester(object):
	def __init__(self):
		pass

	def get_sources(self):
		sources 	 = []
		source_files = glob.iglob("./src/*.py")
		for file in source_files:
			source = file.replace("./src/","").replace(".py","")
			source = importlib.import_module("src.{}".format(source))
			source = source.Crawler()
			sources.append(source)
		return sources

	def xpath_test(self, source=None, parent_xpath=None, child_xpath=None, tester=BaseTester(), preparator=BasePreparator()):
		""" This function will test based on the parent and child xpaths
			if child_xpath is not provided, the function will only test parent_xpath

			variables:
			source       = a Crawler class from ./src folder
			parent_xpath = a XPATH for parent. The return of parent xpath should be a list
			child_xpath  = a XPATH for child. The parent of the child is this the parent_xpath result.
			tester       = a tester class variable that can do the test.
						   The default value of the tester variable is BaseTester()
			preparator   = a preparator class. The preparator will help to prepare
			   	  		   which link to be crawled using this test.
			   	  		   The default value of this preparator is BasePreparator()
		"""
		assert parent_xpath is not None, "parent_xpath is not defined."
		assert source       is not None, "source is not defined."
		assert tester		is not None, "test is not defined."

		try:
			has_link = False
			for link in preparator.get_links(source):
				has_link = True
				print("[test][debug][{}] Link: {}".format(source.CRAWLER_NAME, link.encode("utf-8")))
				page = source.NETWORK_TOOLS.parse(link, parse=False)				

				if page == "<html></html>":
					raise exceptions.TestIsNotPassed("Invalid Link.")

				page 	= lxml.html.fromstring(page)
				parents = tools._xpath(parent=page, syntax=parent_xpath)
				if child_xpath is not None:
					for parent in parents:
						children = tools._xpath(parent=parent, syntax=child_xpath)
						tester.test(children)
				else:
					tester.test(parents, link=link)
			# Sometimes preparator.get_links() returns nothing.
			# As a result, the xpath_test() should return me False or Failed
			return True if has_link else False
		except lxml.etree.XPathEvalError:
			print(fmtstr("[test][error][{}] XPATH is not valid.".format(source.CRAWLER_NAME), "red"))
			return False
		except exceptions.TestIsNotPassed as e:
			print(fmtstr("[test][error][{}] {}.".format(source.CRAWLER_NAME, e), "red"))
			return False
		except UnicodeDecodeError:
			print(fmtstr("[test][error][{}] XPATH is not valid.".format(source.CRAWLER_NAME), "red"))
	#end def




# from .date_tester import DateTester
# import glob
# import importlib

# class Tester(object):
# 	def __init__(self):
# 		pass

# 	def get_test_files(self):
# 		""" This function will return you a list of crawler file names
# 			It will remove the path and .py extension.

# 			return sample:
# 				['kaskus_co_id', 'kompas_com', 'detik_com']
# 		"""
# 		crawlers = glob.glob("./tests/*.py")
# 		crawlers = [crawler.replace("./tests/","").replace(".py","") for crawler in crawlers]
# 		return crawlers

# 	def get_source_files(self):
# 		""" This function will return you a list of crawler file names. 
# 			However, the difference between get_test_files and get_source_files is
# 			get_test_files will return you file names insisde ./tests folder wherease
# 			get_source_files willr eturn you file names inside ./src folder. 

# 			This function will not go search all the .py inside the src. In other words,
# 			This function will not search deep childern.

# 			return sample:
# 				['kaskus_co_id', 'kompas_com', 'detik_com']
# 		"""
# 		sources = glob.glob("./src/*.py")
# 		sources = [source.replace("./src/","").replace(".py","") for source in sources]
# 		return sources

# 	def test(self, crawlers=None):
# 		""" This function will test everything. 
# 			The function will print you documents of posts.
# 			The behavior of this function is:
# 				1. Get last category from LINK_TO_CRAWL
# 				2. Go to LINK_TO_CRAWL
# 				3. Get all the threads
# 				4. Go to Last Page
# 				5. Parse all the post in the Last Page
# 				6. Display the last post
# 		"""
# 		assert type(crawlers) is list, "crawlers is not a list."

# 		for crawler_name in crawlers:
# 			module 	= "tests.{}".format(crawler_name)
# 			crawler = importlib.import_module(module)
# 			crawler = crawler.Crawler()
# 			crawler.crawl()
# 		#end for

# 	def field_test(self, crawlers=None, field=None):
# 		assert type(crawlers) is list    , "crawlers is not a list."
# 		assert field          is not None, "field is not defined."

# 		tester = None
# 		if field == "published_date":
# 			tester = DateTester()
# 		assert tester is not None, "cannot find tester class."
		
# 		# This crawlers depends on the what kind of test we are going to perform
# 		# If the tester need to use DateTester(), then variable crawler will use sources
# 		for crawler in crawlers:
# 			tester.test(crawler)