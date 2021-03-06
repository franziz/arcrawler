from ..factory.explorer import ExplorerFactory
from ..factory.config   import ConfigFactory
from ..factory.parser   import ParserFactory
from ..factory.writer   import WriterFactory
from ..exceptions       import CannotFindCrawler
from .section 			import Section
import os
import shutil

class Builder:
	BUILD_PATH = os.path.join(os.getcwd(),"build")

	def __init__(self):
		pass

	@classmethod
	def build(self, section=None, callback=None):
		""" Exceptions:
			- AssertionError (TemplateParser, CrawlerWriter, LibraryExplorer, RunConfigWriter, RouteWriter)
			- CannotFindCrawler
		"""
		assert section       is not None, "section_name is not defined."
		assert callback      is not None, "callback is not defined."
		assert type(section) is Section, "incorrect section data type."

		# This explorer will return you Crawler object o source files <dict>
		callback("[build][debug] Exploring Source Files")
		explorer = ExplorerFactory.get_explorer(ExplorerFactory.SOURCE_FILES)
		sources  = explorer.explore()

		callback("[build][debug] Filtering crawler by name")
		selected_sources = []
		for crawler_name in section.items:
			if crawler_name not in sources:
				raise CannotFindCrawler("Cannot find %s inside config files" % crawler_name)
			selected_sources.append(sources[crawler_name])
		if len(selected_sources) == 0: raise CannotFindCrawler("Cannot find crawlers inside config files.")

		# This explorer will return you template object of template files <dict>
		callback("[build][debug] Exploring Templates")
		explorer  = ExplorerFactory.get_explorer(ExplorerFactory.TEMPLATE_FILES)
		templates = explorer.explore()

		callback("[build][debug] Injecting Crawler inside Template")
		template_parser  = ParserFactory.get_parser(ParserFactory.TEMPLATE)
		crawlers         = []
		for source in selected_sources:
			crawlers.extend(template_parser.parse(source, templates[source.TEMPLATE]))

		if os.path.isdir(Builder.BUILD_PATH): shutil.rmtree(Builder.BUILD_PATH)
		os.makedirs(Builder.BUILD_PATH)

		callback("[build][debug] Building selected crawlers")
		writer = WriterFactory.get_writer(WriterFactory.CRAWLER)
		index  = 0
		for crawler_name, template_file in crawlers:
			crawler_name = crawler_name.lower()
			crawler_name = crawler_name.replace(" ","_")
			crawler_name = "%s_%s" % (crawler_name, index)
			index        = index + 1
			writer.write(template_file, name=crawler_name, location=Builder.BUILD_PATH)

		callback("[build][debug] Copying dependecy")
		explorer = ExplorerFactory.get_explorer(ExplorerFactory.LIBRARY)
		explorer.copy("config", target_location=Builder.BUILD_PATH)
		explorer.copy("engine", target_location=Builder.BUILD_PATH)
		explorer.copy("validator", target_location=Builder.BUILD_PATH)
		explorer.copy("extractor", target_location=Builder.BUILD_PATH)
		explorer.copy("factory", target_location=Builder.BUILD_PATH)
		explorer.copy("generator", target_location=Builder.BUILD_PATH)
		explorer.copy("obj", target_location=Builder.BUILD_PATH)
		explorer.copy("cleanser", target_location=Builder.BUILD_PATH)
		explorer.copy("parser", target_location=Builder.BUILD_PATH)
		explorer.copy("logger", target_location=Builder.BUILD_PATH)
		explorer.copy("saver", target_location=Builder.BUILD_PATH)
		explorer.copy("monitor", target_location=Builder.BUILD_PATH)
		explorer.copy("template", target_location=Builder.BUILD_PATH)
		explorer.copy("exceptions.py", target_location=Builder.BUILD_PATH)
		explorer.copy("network_tools.py", target_location=Builder.BUILD_PATH)
		explorer.copy("proxy_switcher.py", target_location=Builder.BUILD_PATH)
		explorer.copy("database.py", target_location=Builder.BUILD_PATH)
		explorer.copy("run.py", target_location=Builder.BUILD_PATH, outside_lib=True)
		explorer.copy("kick_start.sh", target_location=Builder.BUILD_PATH, outside_lib=True)
		explorer.copy("proxy_crawler.py", target_location=Builder.BUILD_PATH, outside_lib=True)
		
		callback("[build][debug] Making new run.json")
		writer = WriterFactory.get_writer(WriterFactory.RUN_CONFIG)
		writer.write(workers=section.workers, section=section.name, run=section.items, location=Builder.BUILD_PATH)

		callback("[build][debug] Making new route.json (%s)" % section.name)
		writer = WriterFactory.get_writer(WriterFactory.ROUTE_CONFIG)
		writer.write(route=section.name, location=Builder.BUILD_PATH)

		callback("[build][debug] Making new sentry.json")
		writer = WriterFactory.get_writer(WriterFactory.SENTRY_CONFIG)
		writer.write(location=Builder.BUILD_PATH)

		callback("[build][debug] Making new monitor.json")
		writer = WriterFactory.get_writer(WriterFactory.MONITOR_CONFIG)
		writer.write(location=Builder.BUILD_PATH)
		
		callback("[build][debug] Completed!")

	@classmethod
	def get_sections(self):
		""" Exceptions:
			- AssertionError (RunConfig)
			- CannotFindField (RunConfig)
		"""
		run_config   = ConfigFactory.get_config(ConfigFactory.RUN)
		sections     = run_config.get("sections")
		obj_sections = []
		for section_name, section_items in sections.items():
			obj_sections.append(Section(
				   name = section_name,
				  items = [item.title() for item in section_items["crawlers"]],
		    	workers = section_items["workers"]
			))
		obj_sections.sort(key=lambda x:x.name)
		return obj_sections