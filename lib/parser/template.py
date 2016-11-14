import copy

class TemplateParser:
	def __init__(self):
		pass

	def parse(self, crawler_source=None, template=None):
		""" Exceptions
			- AssertionError
		"""
		assert crawler_source is not None, "crawler_source is not defined."
		assert template       is not None, "template is not defined."

		rendered_templates = []
		links 			   = []
		if hasattr(crawler_source, "LINK_TO_CRAWL"):
			links = crawler_source.LINK_TO_CRAWL
		elif hasattr(crawler_source, "CATEGORY_LINKS"):
			links = crawler_source.CATEGORY_LINKS

		for link_to_crawl in links:
			new_source               = copy.deepcopy(crawler_source)
			new_source.LINK_TO_CRAWL = link_to_crawl
			rendered_template        = template.render(template=new_source)
			rendered_templates.append((crawler_source.CRAWLER_NAME, rendered_template,))
		return rendered_templates