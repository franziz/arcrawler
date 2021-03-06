from ..network_tools     import NetworkTools
from ..factory.parser    import ParserFactory
from ..factory.extractor import ExtractorFactory
from ..factory.generator import GeneratorFactory
from ..factory.validator import ValidatorFactory
from ..exceptions        import CannotFindPrevLink, CannotFindPost, CannotFindThreadLink
from curtsies            import fmtstr
import copy
import logging

class ForumEngine:
	def __init__(self, **kwargs):
		""" Exceptions:
			- AssertionError (ForumEngineValidator, FieldsParser)
		"""

		# Initialize Logging function
		self.logger = logging.getLogger(__name__)

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

		# If not valid, just throw the error
		# We cannot continue with error
		validator = ValidatorFactory.get_validator(ValidatorFactory.FORUM_ENGINE)
		validator.validate(self)

		if self.name is not None:
			self.name = self.name.title()

		if self.fields is not None and self.link_to_crawl is not None:
			parser        = ParserFactory.get_parser(ParserFactory.FIELDS)
			parser.domain = NetworkTools.get_domain(self.link_to_crawl)
			self.fields   = parser.parse(self.fields)

	def get_threads(self):
		""" Exceptions:
			- AssertionError (ForumEngineValidator, ThreadExtractor)
			- CannotFindThread (ThreadExtractor)
			- IncorrectXPATHSyntax (ThreadExtractor)
		"""
		validator = ValidatorFactory.get_validator(ValidatorFactory.FORUM_ENGINE)
		validator.validate(self)

		extractor = ExtractorFactory.get_extractor(ExtractorFactory.THREAD)
		threads   = extractor.extract(
			 		 link = self.link_to_crawl,
				    xpath = self.thread_xpath,
			network_tools = self.network_tools
		)
		return threads

	def get_thread_link(self, thread=None):
		""" Exceptions:
			- AssertionError (ForumEngineValidator, ThreadLinkExtractor)
			- IncorrectXPATHSyntax (ThreadLinkExtractor)
			- CannotFindThreadLink (ThreadLinkExtractor)
		"""
		assert thread is not None, "thread is not defined."
		validator = ValidatorFactory.get_validator(ValidatorFactory.FORUM_ENGINE)
		validator.validate(self)

		extractor        = ExtractorFactory.get_extractor(ExtractorFactory.THREAD_LINK)
		extractor.domain = NetworkTools.get_domain(self.link_to_crawl)
		return extractor.extract(
				   thread = thread.element,
			 		xpath = self.thread_link_xpath,
			network_tools = self.network_tools
		)

	def get_last_page(self, thread=None):
		""" Exceptions:
			- AssertionError (ForumEngineValidator, LastPageExtractor)
			- IncorrectXPATHSyntax (LastPageExtractor)
		"""
		assert thread is not None, "thread is not defined."
		validator = ValidatorFactory.get_validator(ValidatorFactory.FORUM_ENGINE)
		validator.validate(self)

		extractor        = ExtractorFactory.get_extractor(ExtractorFactory.LAST_PAGE)
		extractor.domain = NetworkTools.get_domain(self.link_to_crawl)
		return extractor.extract(
			  thread_link = thread.link,
			        xpath = self.last_page_xpath,
			network_tools = self.network_tools
		)

	def extract_post(self, thread):
		""" Exceptions
			- AssertionError (ForumEngineValidator)
			- CannotFindPost (PostExtractor)
			- IncorrectXPATHSyntax (PostExtractor)
		"""
		assert thread is not None, "thread is not defined."
		validator = ValidatorFactory.get_validator(ValidatorFactory.FORUM_ENGINE)
		validator.validate(self)

		extractor = ExtractorFactory.get_extractor(ExtractorFactory.POST)
		return extractor.extract(
			   	   thread = thread,
			    	xpath = self.post_xpath,
				attribute = self.fields,
			network_tools = self.network_tools
		)

	def crawl_thread(self, thread):
		""" Exceptions
			- AssertionError (extract_post, PostDataGenerator, PostSaver.batch_save, PrevPageExtractor)
			- CannotFindPost (extract_post)
			- IncorrectXPATHSyntax (extract_post, PrevPageExtractor)
			- CannotFindField (PostSaver.batch_save)
			- ValidationError (PostSaver.batch_save)
		"""
		print("[%s][debug] Extracting Post(s)" % self.name)
		posts = self.extract_post(thread)
		print("[%s][debug] Found %s post(s)" % (self.name, len(posts)))

		print("[%s][debug] Generating additional post_data" % self.name)
		generator = GeneratorFactory.get_generator(GeneratorFactory.POST_DATA)
		posts     = [generator.generate(post, origin=self.link_to_crawl, crawled_by= self.name, country=self.country) for post in posts]

		# All saved means, all document are saved without any duplicate
		# Possible you will have prev_page,
		# Find any prev_page.
		all_saved = self.saver.batch_save(posts)

		if all_saved:
			try:
				extractor        = ExtractorFactory.get_extractor(ExtractorFactory.PREV_PAGE)
				extractor.domain = NetworkTools.get_domain(thread.last_page)
				prev_page        = extractor.extract(
					       thread = thread,
					        xpath = self.prev_xpath,
					network_tools = self.network_tools
				)

				# assuming the extractor does not thrown CannotFindPrevLink exception
				print("[%s][debug] Go to previous page" % self.name)
				thread.last_page = copy.copy(prev_page)
				self.crawl_thread(copy.deepcopy(thread))
			except CannotFindPrevLink as ex:
				pass

	def crawl(self, saver=None):
		""" Exceptions:
			- AssertionError (ForumEngineValidator, get_threads, get_thread_link, get_last_page, crawl_thread)
			- CannotFindThread (get_threads)
			- IncorrectXPATHSyntax (get_threads, get_thread_link, get_last_page, crawl_thread)
			- CannotFindField (crawl_thread)
			- ValidationError (crawl_thread)
			This is the main function for ForumEngine crawler.
		"""
		assert saver is not None, "saver is not defined."
		self.saver = saver
		validator  = ValidatorFactory.get_validator(ValidatorFactory.FORUM_ENGINE)
		validator.validate(self)

		print("[%s][debug] Finding threads on %s" % (self.name, self.link_to_crawl.encode("utf8")))
		threads = self.get_threads()
		print("[%s][debug] Thread found!" % self.name)

		for thread in threads:
			try:
				print("[%s][debug] Getting Thread Link" % self.name)
				thread.link = self.get_thread_link(thread)

				print("[%s][debug] Getting Last Page Link" % self.name)
				thread.last_page = self.get_last_page(thread)

				self.crawl_thread(thread)
			except CannotFindPost as ex:
				self.logger.error(str(ex), exc_info=True)
			except CannotFindThreadLink as ex:
				self.logger.error(str(ex), exc_info=True)
