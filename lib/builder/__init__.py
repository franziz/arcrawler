from ..config.factory 		 import ConfigFactory
from ..forum_engine.template import Template
from .section 		 		 import Section
import os
import shutil
import glob
import importlib
import io
import json
import copy

class Builder:

	@classmethod
	def build(self, section=None, log_callback=None):
		assert section is not None, "section is not defined."

		log_callback("[build][debug] Building %s" % section.name)

		# change route inside route.json to the name
		# this will makes me easy to deploy in the future
		log_callback("[build][debug] Changing route.json")
		route_config = ConfigFactory.get(ConfigFactory.ROUTE)
		route_config.change_cd_server_route(to=section.name)

		log_callback("[build][debug] Preparing Build folder")
		build_folder = os.path.join(os.getcwd(), "build")
		if os.path.isdir(build_folder):	shutil.rmtree(build_folder)
		os.makedirs(build_folder)

		log_callback("[build][debug] Preparing crawlers folder")
		crawlers_folder = os.path.join(build_folder, "crawlers")
		if os.path.isdir(crawlers_folder): shutil.rmtree(crawlers_folder)
		os.makedirs(crawlers_folder)

		log_callback("[build][debug] Copying config...")
		shutil.copytree(os.path.join(".","config"),os.path.join(build_folder,"config"))

		log_callback("[build][debug] Copying run...")
		shutil.copyfile(os.path.join(".","run.py"),os.path.join(build_folder,"run.py"))

		log_callback("[build][debug] Copying kick_start...")
		shutil.copyfile(os.path.join(".","kick_start.sh"),os.path.join(build_folder,"kick_start.sh"))

		log_callback("[build][debug] Copying forum_engine...")
		shutil.copytree(os.path.join(".","lib","forum_engine"),os.path.join(build_folder,"lib","forum_engine"))

		log_callback("[build][debug] Copying config library...")
		shutil.copytree(os.path.join(".","lib","config"),os.path.join(build_folder,"lib","config"))

		log_callback("[build][debug] Copying monitor...")
		shutil.copytree(os.path.join(".","lib","monitor"),os.path.join(build_folder,"lib","monitor"))

		log_callback("[build][debug] Copying converter_engine...")
		shutil.copytree(os.path.join(".","lib","converter_engine"),os.path.join(build_folder,"lib","converter_engine"))

		log_callback("[build][debug] Copying proxy_switcher...")
		shutil.copyfile(os.path.join(".","lib","proxy_switcher.py"),os.path.join(build_folder,"lib","proxy_switcher.py"))		

		log_callback("[build][debug] Copying exceptions...")
		shutil.copyfile(os.path.join(".","lib","exceptions.py"),os.path.join(build_folder,"lib","exceptions.py"))		

		log_callback("[build][debug] Copying network_tools...")
		shutil.copyfile(os.path.join(".","lib","network_tools.py"),os.path.join(build_folder,"lib","network_tools.py"))		

		log_callback("[build][debug] Copying tools...")
		shutil.copyfile(os.path.join(".","lib","tools.py"),os.path.join(build_folder,"lib","tools.py"))

		log_callback("[build][debug] Copying database...")
		shutil.copyfile(os.path.join(".","lib","database.py"),os.path.join(build_folder,"lib","database.py"))

		log_callback("[build][debug] Copying runners...")
		shutil.copytree(os.path.join(".","lib","runners"),os.path.join(build_folder,"runners"))
		shutil.copytree(os.path.join(".","lib","runners"),os.path.join(build_folder,"lib","runners"))

		log_callback("[build][debug] Reading source folder")
		crawlers      = []
		found         = [False for f in section.items]
		source_folder = os.path.join(os.getcwd(), "src")
		for file_name in glob.iglob(os.path.join(source_folder,"*.py")):
			file_name = file_name.replace(source_folder,"")
			file_name = file_name.replace(".py","")
			file_name = file_name.replace("/","")
			module    = importlib.import_module("src.%s" % file_name)
			crawler   = module.Crawler()
			if crawler.CRAWLER_NAME in section.items:
				index        = section.items.index(crawler.CRAWLER_NAME)
				found[index] = True
				crawlers.append(crawler)
		for index,f in enumerate(found):
			if not found: raise CannotFindCrawler("Cannot find %s crawler" % section.items[index])

		log_callback("[build][debug] Building crawlers")
		converter_config = {}
		for crawler in crawlers:
			name = crawler.CRAWLER_NAME.replace(" ","_")
			name = name.lower()
			for index,link in enumerate(crawler.LINK_TO_CRAWL):
				template = Template.patch(crawler=crawler, link=link)
				file     = io.open(os.path.join(crawlers_folder,"%s_%s.py" % (name,index)),"w", encoding="utf8")
				file.write(template)
				file.flush()
				file.close()
			converter_config.update({
				crawler.CRAWLER_NAME.lower():{
					"db_address" : crawler.DB_SERVER_ADDRESS,
					   "db_name" : crawler.DB_SERVER_NAME
				}
			})

		log_callback("[build][debug] Generating new run.json file.")
		config_folder = os.path.join(build_folder, "config")
		run_config    = ConfigFactory.get(ConfigFactory.RUN)
		config_file   = open(os.path.join(config_folder,"run.json"),"w")
		document      = {
							"workers" : run_config.get("workers"),
							    "run" : section.items,
							"section" : section.name
						}
		config_file.write(json.dumps(document, indent=4))
		config_file.flush()
		config_file.close()

		log_callback("[build][debug] Generating new converter.json file.")
		converter_path = os.path.join(build_folder, "config")
		if not os.path.isdir(converter_path): raise CannotFindFolder("Cannot find %s folder" % converter_path)		
		old_converter = open(os.path.join(converter_path, "converter.json"), "r")
		old_converter = json.load(old_converter)
		new_converter = copy.deepcopy(old_converter)
		new_converter.update(dict(crawlers=converter_config))
		new_converter = json.dumps(new_converter, indent=4, separators=(",",":"))
		file = open(os.path.join(converter_path,"converter.json"), "w")
		file.write(new_converter)
		file.flush()
		file.close()

		log_callback("[build][debug] Completed!")


	@classmethod
	def get_sections(self):
		run_config   = ConfigFactory.get(ConfigFactory.RUN)
		sections     = run_config.get("sections")
		obj_sections = []
		for section_name, section_items in sections.items():
			obj_sections.append(Section(
				 name = section_name,
				items = section_items
			))
		obj_sections.sort(key=lambda x:x.name)
		return obj_sections

# # -*- coding: utf-8 -*-

# from ..config.factory import ConfigFactory
# from ..exceptions     import CannotFindFolder, CannotFindCrawler
# from .template        import Template
# import glob
# import os
# import importlib
# import shutil
# import copy
# import codecs
# import json

# class Builder:

# 	BUILD_FOLDER    = os.path.join(".","build")
# 	CRAWLERS_FOLDER = os.path.join(BUILD_FOLDER, "crawlers")

# 	def _print_log(self, message=None):
# 		assert message is not None, "message is not defined."
# 		print("[build] %s" % message)

# 	def _init_requirement(self):
# 		if os.path.isdir(Builder.BUILD_FOLDER):
# 			shutil.rmtree(Builder.BUILD_FOLDER)
# 		os.mkdir(Builder.BUILD_FOLDER)
# 		os.mkdir(Builder.CRAWLERS_FOLDER)
		
# 		self._print_log(self, "Copying config...")
# 		shutil.copytree(os.path.join(".","config"),os.path.join(Builder.BUILD_FOLDER,"config"))

# 		self._print_log(self, "Copying run...")
# 		shutil.copyfile(os.path.join(".","run.py"),os.path.join(Builder.BUILD_FOLDER,"run.py"))

# 		self._print_log(self, "Copying kick_start...")
# 		shutil.copyfile(os.path.join(".","kick_start.sh"),os.path.join(Builder.BUILD_FOLDER,"kick_start.sh"))

# 		self._print_log(self, "Copying forum_engine...")
# 		shutil.copytree(os.path.join(".","lib","forum_engine"),os.path.join(Builder.BUILD_FOLDER,"lib","forum_engine"))

# 		self._print_log(self, "Copying config library...")
# 		shutil.copytree(os.path.join(".","lib","config"),os.path.join(Builder.BUILD_FOLDER,"lib","config"))

# 		self._print_log(self, "Copying monitor...")
# 		shutil.copytree(os.path.join(".","lib","monitor"),os.path.join(Builder.BUILD_FOLDER,"lib","monitor"))

# 		self._print_log(self, "Copying converter_engine...")
# 		shutil.copytree(os.path.join(".","lib","converter_engine"),os.path.join(Builder.BUILD_FOLDER,"lib","converter_engine"))

# 		self._print_log(self, "Copying proxy_switcher...")
# 		shutil.copyfile(os.path.join(".","lib","proxy_switcher.py"),os.path.join(Builder.BUILD_FOLDER,"lib","proxy_switcher.py"))		

# 		self._print_log(self, "Copying exceptions...")
# 		shutil.copyfile(os.path.join(".","lib","exceptions.py"),os.path.join(Builder.BUILD_FOLDER,"lib","exceptions.py"))		

# 		self._print_log(self, "Copying network_tools...")
# 		shutil.copyfile(os.path.join(".","lib","network_tools.py"),os.path.join(Builder.BUILD_FOLDER,"lib","network_tools.py"))		

# 		self._print_log(self, "Copying tools...")
# 		shutil.copyfile(os.path.join(".","lib","tools.py"),os.path.join(Builder.BUILD_FOLDER,"lib","tools.py"))

# 		self._print_log(self, "Copying database...")
# 		shutil.copyfile(os.path.join(".","lib","database.py"),os.path.join(Builder.BUILD_FOLDER,"lib","database.py"))

# 		self._print_log(self, "Copying runners...")
# 		shutil.copytree(os.path.join(".","lib","runners"),os.path.join(Builder.BUILD_FOLDER,"runners"))
# 		shutil.copytree(os.path.join(".","lib","runners"),os.path.join(Builder.BUILD_FOLDER,"lib","runners"))

# 	def _get_sources(self):
# 		source_folder = os.path.join(".","src")
# 		sources       = {}
# 		if not os.path.isdir(source_folder): raise CannotFindFolder("Cannot find %s folder" % source_folder)
# 		for file_name in glob.iglob(os.path.join(source_folder,"*.py")):
# 			crawler_object = file_name.replace("%s/" % source_folder, "").replace(".py","")
# 			crawler_object = importlib.import_module("src.%s" % crawler_object)
# 			crawler_object = crawler_object.Crawler()
# 			crawler_name   = crawler_object.CRAWLER_NAME
# 			sources.update({crawler_name.title():crawler_object})
# 		return sources

# 	@classmethod
# 	def build(self):		
# 		# Read config file
# 		self._print_log(self, "Reading run.json")
# 		run_config = ConfigFactory.get(ConfigFactory.RUN)

# 		# Only build whatever crawler inside run_config
# 		# Because the format is dict, we need to compile everything
# 		# into single array
# 		run      = run_config.get("run")
# 		crawlers = []
# 		if not type(run) is dict: raise TypeError("crawlers variable should a dict")
# 		for key,value in run.items():
# 			crawlers.extend([v.title() for v in value])
		
# 		# Make a dictionary of {crawler_name : crawler_object}
# 		# for easy use of and calling the crawler
# 		self._print_log(self, "Reading %s folder" % os.path.join(".","src"))
# 		sources = self._get_sources(self)

# 		# Need to verify the crawler config from run.json
# 		# If the crawler config cannot find the specific crawler
# 		# Thrown an error and say that the crawler cannot be found from ./src folder
# 		self._print_log(self,"Checking run.json configuration")		
# 		for index, crawler in enumerate(crawlers):
# 			if not crawler in sources.keys(): raise CannotFindCrawler("Cannot find %s in ./src folder" % crawler)
# 			crawlers[index] = copy.deepcopy(sources[crawler])		

# 		self._print_log(self, "Reading templates...")
# 		template_library = Template()
# 		template_library.make()

# 		self._print_log(self, "Patching every single links to the template...")
# 		patched_crawlers = []
# 		converter_config = {}
# 		for index, crawler in enumerate(crawlers):
# 			converter_config.update({
# 				crawler.CRAWLER_NAME.lower():{
# 					"db_address" : crawler.DB_SERVER_ADDRESS,
# 					   "db_name" : crawler.DB_SERVER_NAME
# 				}
# 			})
# 			for link in crawler.LINK_TO_CRAWL:
# 				single_link_crawler               = copy.deepcopy(crawler)
# 				single_link_crawler.LINK_TO_CRAWL = copy.deepcopy(link)

# 				current_template = template_library.get(single_link_crawler.TEMPLATE)		
# 				current_template.patch(single_link_crawler)
				
# 				single_link_crawler.TEMPLATE = current_template
# 				patched_crawlers.append((crawler.CRAWLER_NAME,str(single_link_crawler.TEMPLATE)))

# 		self._print_log(self, "Initializing all requirements")
# 		self._init_requirement(self)

# 		self._print_log(self, "Making crawlers...")
# 		if not os.path.isdir(Builder.CRAWLERS_FOLDER): raise CannotFindFolder("Cannot find %s folder." % Builder.CRAWLERS_FOLDER)
# 		for index, crawler in enumerate(patched_crawlers):
# 			crawler_name, patched_template = crawler
# 			file_name    = "%s_%s.py" % (crawler_name, index)
# 			file_name    = file_name.replace(" ","_")
# 			file_name    = file_name.lower()
# 			crawler_file = codecs.open(os.path.join(Builder.CRAWLERS_FOLDER, file_name),"w","utf-8-sig")
# 			crawler_file.write(patched_template)
# 			crawler_file.flush()
# 			crawler_file.close()

# 		# Reading old converter_config file, 
# 		# and apply that to new converter_config.
# 		self._print_log(self, "Making converter config...")
# 		converter_path = os.path.join(Builder.BUILD_FOLDER, "config")
# 		if not os.path.isdir(converter_path): raise CannotFindFolder("Cannot find %s folder" % converter_path)		
# 		old_converter = open(os.path.join(converter_path, "converter.json"), "r")
# 		old_converter = json.load(old_converter)
# 		new_converter = copy.deepcopy(old_converter)
# 		new_converter.update(dict(crawlers=converter_config))
# 		new_converter = json.dumps(new_converter, indent=4, separators=(",",":"))
# 		file = open(os.path.join(converter_path,"converter.json"), "w")
# 		file.write(new_converter)
# 		file.flush()
# 		file.close()