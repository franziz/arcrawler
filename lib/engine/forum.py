from ..network_tools     import NetworkTools
from ..factory.parser    import ParserFactory
from ..factory.extractor import ExtractorFactory
from ..factory.generator import GeneratorFactory
from ..exceptions        import CannotFindPost, CannotFindThread
from curtsies            import fmtstr
import copy

class ForumEngine:
	def __init__(self, **kwargs):
		self.name              = kwargs.get("name", None)
		self.network_tools     = kwargs.get("network_tools",NetworkTools(use_proxy=False))
		self.link_to_crawl     = kwargs.get("link_to_crawl",None)
		self.country           = kwargs.get("country",None)
		self.thread_xpath      = kwargs.get("thread_xpath",None)
		self.thread_link_xpath = kwargs.get("thread_link_xpath", None)
		self.last_page_xpath   = kwargs.get("last_page_xpath",None)
		self.prev_xpath        = kwargs.get("prev_xpath",None)
		self.post_xpath        = kwargs.get("post_xpath",None)
		self.fields            = kwargs.get("fields",None)

		if self.name is not None:
			self.name = self.name.title()

		if self.fields is not None and self.link_to_crawl is not None:
			parser        = ParserFactory.get_parser(ParserFactory.FIELDS)
			parser.domain = NetworkTools.get_domain(self.link_to_crawl)
			self.fields   = parser.parse(self.fields)	

	def crawl(self, saver=None):
		assert saver    			  is not None, "saver is not defined."
		assert self.thread_xpath      is not None, "thread_xpath is not defined."
		assert self.thread_link_xpath is not None, "thread_link_xpath is not defined."
		assert self.link_to_crawl     is not None, "link_to_crawl is not defined."
		assert self.last_page_xpath   is not None, "last_page_xpath is not defined."
		assert self.post_xpath 		  is not None, "post_xpath is not defined."
		assert self.name              is not None, "name is not defined."
		assert self.fields            is not None, "fields is not defined."
		assert self.prev_xpath        is not None, "prev_xpath is not defined."

		print("[%s][debug] Finding threads on %s" % (self.name, self.link_to_crawl.encode("utf8")))
		try:
			extractor = ExtractorFactory.get_extractor(ExtractorFactory.THREAD)
			threads   = extractor.extract(
				             link = self.link_to_crawl,
				     thread_xpath = self.thread_xpath,
				thread_link_xpath = self.thread_link_xpath,
				  last_page_xpath = self.last_page_xpath,
				    network_tools = self.network_tools
			)
			print("[%s][debug] found %s thread(s)" % (self.name, len(threads)))
			for thread in threads:
				try:
					has_prev = True
					while has_prev:
						# This will get all the post. For any details about how the function get posts
						# you can refer to extractor.post section
						print("[%s][debug] Extracting post(s) for %s" % (self.name, thread.last_page.encode("utf8")))
						extractor = ExtractorFactory.get_extractor(ExtractorFactory.POST)
						posts     = extractor.extract(
							   	   thread = thread,
							    	xpath = self.post_xpath,
								attribute = self.fields,
							network_tools = self.network_tools
						)
						print("[%s][debug] Found %s post(s)" % (self.name, len(posts)))

						# This will generate default field for each post
						# For example, _insert_time and TTL
						print("[%s][debug] Generating additional post_data" % self.name)
						generator = GeneratorFactory.get_generator(GeneratorFactory.POST_DATA)
						posts     = [generator.generate(post, origin=self.link_to_crawl, country=self.country) for post in posts]
						
						# Exception handling is being handled by batch_save function
						all_saved = saver.batch_save(posts)

						if all_saved:
							extractor        = ExtractorFactory.get_extractor(ExtractorFactory.PREV_PAGE)
							extractor.domain = NetworkTools.get_domain(thread.last_page)
							prev_page        = extractor.extract(
								       thread = thread,
								        xpath = self.prev_xpath,
								network_tools = self.network_tools
							)
							has_prev = prev_page is not None
							if has_prev:
								thread.last_page = copy.copy(prev_page)
						else:
							has_prev = False
					print(fmtstr("[%s][warning] No Previous Page for %s" % (self.name, thread.last_page.encode("utf-8")),"yellow"))
				except CannotFindPost as ex:
					# This exception catched from PostExtractor
					# Assuming if you cannot find any post inside thread, you don't need to continue,
					# Just go to next thread
					print(fmtstr("[%s][error] %s" % (self.name, ex),"red"))
		except CannotFindThread as ex:
			# Cannot find any thread?
			# Just leave it!
			print(fmtstr("[%s][error] %s" % (self.name, ex),"red"))