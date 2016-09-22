import os
import importlib
import glob

class SourceFilesExplorer:
	def __init__(self):
		pass

	def explore(self):
		source_path = os.path.join(os.getcwd(), "src")
		file_names  = glob.iglob(os.path.join(source_path,"*.py"))

		crawlers = {}
		for file_name in file_names:
			file_name = file_name.replace(source_path,"")
			file_name = file_name.replace(".py","")
			file_name = file_name.replace("/","")
			
			module  = importlib.import_module("src.%s" % file_name)
			crawler = module.Crawler()
			crawlers.update({crawler.CRAWLER_NAME:crawler})
		return crawlers
