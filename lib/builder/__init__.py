# -*- coding: utf-8 -*-

from ..config.factory import ConfigFactory
from ..exceptions     import CannotFindFolder, CannotFindCrawler
from .template        import Template
import glob
import os
import importlib
import shutil
import copy
import codecs

class Builder:

	BUILD_FOLDER    = os.path.join(".","build")
	CRAWLERS_FOLDER = os.path.join(BUILD_FOLDER, "crawlers")

	def _print_log(self, message=None):
		assert message is not None, "message is not defined."
		print("[build] %s" % message)

	def _init_requirement(self):
		if os.path.isdir(Builder.BUILD_FOLDER):
			shutil.rmtree(Builder.BUILD_FOLDER)
		os.mkdir(Builder.BUILD_FOLDER)
		os.mkdir(Builder.CRAWLERS_FOLDER)
		
		self._print_log(self, "Copying config...")
		shutil.copytree(os.path.join(".","config"),os.path.join(Builder.BUILD_FOLDER,"config"))

		self._print_log(self, "Copying run...")
		shutil.copyfile(os.path.join(".","run.py"),os.path.join(Builder.BUILD_FOLDER,"run.py"))

		self._print_log(self, "Copying kick_start...")
		shutil.copyfile(os.path.join(".","kick_start.sh"),os.path.join(Builder.BUILD_FOLDER,"kick_start.sh"))

		self._print_log(self, "Copying forum_engine...")
		shutil.copytree(os.path.join(".","lib","forum_engine"),os.path.join(Builder.BUILD_FOLDER,"lib","forum_engine"))

		self._print_log(self, "Copying config library...")
		shutil.copytree(os.path.join(".","lib","config"),os.path.join(Builder.BUILD_FOLDER,"lib","config"))

		self._print_log(self, "Copying news_engine...")
		shutil.copytree(os.path.join(".","lib","news_engine"),os.path.join(Builder.BUILD_FOLDER,"lib","news_engine"))

		self._print_log(self, "Copying converter_engine...")
		shutil.copytree(os.path.join(".","lib","converter_engine"),os.path.join(Builder.BUILD_FOLDER,"lib","converter_engine"))

		self._print_log(self, "Copying proxy_switcher...")
		shutil.copyfile(os.path.join(".","lib","proxy_switcher.py"),os.path.join(Builder.BUILD_FOLDER,"lib","proxy_switcher.py"))		

		self._print_log(self, "Copying exceptions...")
		shutil.copyfile(os.path.join(".","lib","exceptions.py"),os.path.join(Builder.BUILD_FOLDER,"lib","exceptions.py"))		

		self._print_log(self, "Copying network_tools...")
		shutil.copyfile(os.path.join(".","lib","network_tools.py"),os.path.join(Builder.BUILD_FOLDER,"lib","network_tools.py"))		

		self._print_log(self, "Copying tools...")
		shutil.copyfile(os.path.join(".","lib","tools.py"),os.path.join(Builder.BUILD_FOLDER,"lib","tools.py"))

		self._print_log(self, "Copying runners...")
		shutil.copytree(os.path.join(".","lib","runners"),os.path.join(Builder.BUILD_FOLDER,"lib","runners"))

	@classmethod
	def build(self):		
		# Read config file
		self._print_log(self, "Reading run.json")
		run_config = ConfigFactory.get(ConfigFactory.RUN)

		# Only build whatever crawler inside run_config
		# Because the format is dict, we need to compile everything
		# into single array
		run      = run_config.get("run")
		crawlers = []
		if not type(run) is dict: raise TypeError("crawlers variable should a dict")
		for key,value in run.items():
			crawlers.extend([v.title() for v in value])
		
		# Make a dictionary of {crawler_name : crawler_object}
		# for easy use of and calling the crawler
		self._print_log(self, "Reading %s folder" % os.path.join(".","src"))
		source_folder = os.path.join(".","src")
		sources       = {}
		if not os.path.isdir(source_folder): raise CannotFindFolder("Cannot find %s folder" % source_folder)
		for file_name in glob.iglob(os.path.join(source_folder,"*.py")):
			crawler_object = file_name.replace("%s/" % source_folder, "").replace(".py","")
			crawler_object = importlib.import_module("src.%s" % crawler_object)
			crawler_object = crawler_object.Crawler()
			crawler_name   = crawler_object.CRAWLER_NAME
			sources.update({crawler_name.title():crawler_object})

		# Need to verify the crawler config from run.json
		# If the crawler config cannot find the specific crawler
		# Thrown an error and say that the crawler cannot be found from ./src folder
		self._print_log(self,"Checking run.json configuration")		
		for index, crawler in enumerate(crawlers):
			if not crawler in sources.keys(): raise CannotFindCrawler("Cannot find %s in ./src folder" % crawler)
			crawlers[index] = copy.deepcopy(sources[crawler])		

		self._print_log(self, "Reading templates...")
		template_library = Template()
		template_library.make()

		self._print_log(self, "Patching every single links to the template...")
		patched_crawlers = []
		for index, crawler in enumerate(crawlers):
			for link in crawler.LINK_TO_CRAWL:
				single_link_crawler               = copy.deepcopy(crawler)
				single_link_crawler.LINK_TO_CRAWL = copy.deepcopy(link)

				current_template = template_library.get(single_link_crawler.TEMPLATE)		
				current_template.patch(single_link_crawler)
				
				single_link_crawler.TEMPLATE = current_template
				patched_crawlers.append((crawler.CRAWLER_NAME,str(single_link_crawler.TEMPLATE)))

		self._print_log(self, "Initializing all requirements")
		self._init_requirement(self)

		self._print_log(self, "Making crawlers...")
		if not os.path.isdir(Builder.CRAWLERS_FOLDER): raise CannotFindFolder("Cannot find %s folder." % Builder.CRAWLERS_FOLDER)
		for index, crawler in enumerate(patched_crawlers):
			crawler_name, patched_template = crawler
			file_name    = "%s_%s.py" % (crawler_name, index)
			file_name    = file_name.replace(" ","_")
			file_name    = file_name.lower()
			crawler_file = codecs.open(os.path.join(Builder.CRAWLERS_FOLDER, file_name),"w","utf-8-sig")
			crawler_file.write(patched_template)
			crawler_file.flush()
			crawler_file.close()