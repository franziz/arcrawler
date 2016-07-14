from ..network_tools import NetworkTools
from ..              import tools
from .               import exceptions
import difflib

class Parser(object):
	def find_article_url(self, article=None):
		assert article         is not None, "article is not defined."
		assert article.element is not None, "element is not defined."
		assert article.domain  is not None, "domain is not defined."
		
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
		network_tools   = NetworkTools()
		special_url_tag = ["read/","berita/"]
		ignore_url_tag  = ["galeri/","video/", "tag/", "etalase/"]
		idx             = idx + 1
		has_special     = len([s for s in special_url_tag if s in url]) > 0
		has_ignore_list = len([s for s in ignore_url_tag if s in url]) > 0
		ratio           = difflib.SequenceMatcher(None, article.domain, network_tools.get_domain(url)).ratio()
		success    		= True  if has_special and not success else success
		success         = False if has_ignore_list             else success

		return url if success else None