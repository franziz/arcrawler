from ..              import tools
from .               import exceptions
import difflib
import lxml
import json

class Parser(object):
	def __init__(self):
		self.network_tools = None

	def get_by_xpath(self, parent=None, xpath=None):
		"""	The xpath will be always string,
		    we need to convert the string to list using eval
		"""
		assert parent      is not None, "parent is not defined."
		assert xpath       is not None, "xpath is not defined."
		assert type(xpath) is str     , "xpath is not str."

		try:
			xpath = json.loads(xpath)
		except ValueError:
			xpath = [xpath]

		result  = ""
		index   = 0
		found   = False
		empty   = False
		while not found and not empty:
			syntax = xpath[index]
			try:
				result = tools._xpath(parent,syntax)
				result = "".join(list(result))
				result = tools._clean_string(result)
			except lxml.etree.XPathEvalError:
				print("[news_egine][error] XPath Syntax Error: {}".format(syntax.encode("utf-8")))
			finally:				
				index = index + 1
				empty = True if len(xpath) <= index else False
				found = True if result else False
		return result

	def find_article_url(self, article=None):
		assert self.network_tools is not None, "network_tools is not defined."
		assert article            is not None, "article is not defined."
		assert article.element    is not None, "element is not defined."
		assert article.domain     is not None, "domain is not defined."
		
		url = tools._xpath(article.element, "./@href")
		if len(url) > 1: raise exceptions.TooManyObjectsFound("Too many links in here")

		url = "".join(url)
		if "http://" not in url and "https://" not in url: raise exceptions.BadURLFormat("{} not an url".format(url.encode("utf-8")))
		
		rules     = [
			"./h3/text()",
			".//h3/text()",
			"./h2/text()",
			".//h2/text()",
			".//h2/span/text()",
			".//span[@class='title']/text()",
			"./h1/text()",
			"./text()"
		]
		void_char = [
			(",",""),
			(" ","-"),
			("(",""),
			(")",""),
			("'",""),
			("?",""),
			("!",""),
		]

		success = False
		idx     = -1
		done    = False
		while not success and not done:
			idx   = idx + 1
			title = tools._xpath(article.element, rules[idx])			
			title = "".join(title)			
			title = title.lower()
			title = tools._clean_string(title)
			for void in void_char:
				something, to_something = void
				title                   = title.replace(something, to_something)
			success = (title and len(title.split("-"))>3)
			done    = idx >= len(rules)-1
		special_url_tag = ["read/","berita/"]
		ignore_url_tag  = ["galeri/","video/", "tag/", "etalase/"]
		idx             = idx + 1
		has_special     = len([s for s in special_url_tag if s in url]) > 0
		has_ignore_list = len([s for s in ignore_url_tag if s in url]) > 0
		ratio           = difflib.SequenceMatcher(None, article.domain, self.network_tools.get_domain(url)).ratio()
		success    		= True  if has_special and not success else success
		success         = False if has_ignore_list             else success

		return url if success else None