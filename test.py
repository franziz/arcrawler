from lib.forum_engine import exceptions
import glob
import importlib

crawlers = glob.glob("./tests/*.py")
crawlers = [crawler.replace("./tests/","").replace(".py","") for crawler in crawlers]

assert len(crawlers)>0, "Cannot find test files."

print("Which crawler do you want to test?")
for idx,crawler in enumerate(crawlers):
	print("{}. {}".format(idx+1, crawler))
#end for
print("{}. All".format(len(crawlers)+1))

try:
	selection = input("Selection: ")
	selection = int(selection)
except:
	raise exceptions.ConversionError("Cannot convert data type")
#end try

assert selection >= 1 and selection <= len(crawlers)+1, "Invalid input."

selection = selection - 1
crawlers  = [crawlers[selection]] if selection != len(crawlers) else crawlers
for crawler in crawlers:
	print("Testing: {}".format(crawler))
	crawler = importlib.import_module(
		"tests.{}".format(crawler)
	)
	crawler = crawler.Crawler()
	crawler.crawl()
#end for