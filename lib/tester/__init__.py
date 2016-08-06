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

				if page == "<html><head></head><body></body></html>":
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
		except lxml.etree.XMLSyntaxError:
			print(fmtstr("[test][error][{}] Something wrong with HTML tag.".format(source.CRAWLER_NAME), "red"))
			return False
		except exceptions.TestIsNotPassed as e:
			print(fmtstr("[test][error][{}] {}.".format(source.CRAWLER_NAME, e), "red"))
			return False
		except UnicodeDecodeError:
			print(fmtstr("[test][error][{}] XPATH is not valid.".format(source.CRAWLER_NAME), "red"))
			return False
	#end def
#end class