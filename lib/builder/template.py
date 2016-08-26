from ..exceptions import CannotFindTemplate, CannotFindFolder
import os
import glob
import json
import copy

class Template:

	def __init__(self, **kwargs):
		self.templates = None
		self.template  = kwargs.get("template",None)

	def __str__(self):
		return self.template if self.template is not None else ""

	def make(self):
		""" This function will try to make self.templates.
			Run this function first before running others
		"""	
		template_folder = os.path.join(".","templates")
		self.templates       = {}
		if not os.path.isdir(template_folder): raise CannotFindFolder("Cannot find %s folder" % template_folder)
		for file_name in glob.iglob(os.path.join(template_folder, "*.arct")):
			template_name = file_name.replace("%s/" % template_folder, "")
			template      = open(file_name,"r")
			template      = template.read()
			self.templates.update({template_name:template})

	def get(self, name=None):
		assert self.templates is not None, "Please run make() first."
		assert name           is not None, "name is not defined."

		if not name in self.templates: raise CannotFindTemplate("Cannot find %s in the template folder" % name)
		return Template(template=self.templates[name])


	def patch(self, crawler=None):
		assert crawler                     is not None, "crawler is not defined."
		assert type(crawler.LINK_TO_CRAWL) is str     , "wront LINK_TO_CRAEL type."

		variables = crawler.get_variables()

		# Pathcing variables
		for variable in variables:
			if  "CONDITIONS"    != variable and \
				"LINK_TO_CRAWL" != variable and \
				"TEMPLATE"      != variable and \
				"NETWORK_TOOLS" != variable:
				value        = getattr(crawler,variable)
				value        = json.dumps(value) if type(value) is dict or type(value) is list else value
				replace_var  = "${}".format(variable)
				replace_to	 = "'{}'".format(value.replace("'","\\'"))
				self.template     = self.template.replace(replace_var, replace_to)
			#end if
		#end for

		# setting up for LINK_TO_CRAWL variable
		link         = '"{}"'.format(crawler.LINK_TO_CRAWL)
		self.template     = self.template.replace("$LINK_TO_CRAWL",link)

		if hasattr(crawler, "NETWORK_TOOLS") and crawler.NETWORK_TOOLS is not None:
			class_string     = str(type(crawler.NETWORK_TOOLS))
			class_string     = class_string[class_string.index("'")+1:]
			class_string     = class_string[:class_string.index("'")]
			class_string     = "{class_string}(use_proxy={use_proxy})".format(
									class_string = class_string,
									   use_proxy = crawler.NETWORK_TOOLS.use_proxy
								)

			import_statement = class_string[:class_string.index("(")]
			import_statement = import_statement.split(".")		
			import_statement = "from {base} import {main}".format(
									base = ".".join(import_statement[:-1]),
									main = import_statement[-1]
								)
			self.template         = self.template.replace("$IMPORT", import_statement)
			self.template         = self.template.replace("$NETWORK_TOOLS", class_string.split(".")[-1])

		# setting up assertion that something need to be satisfied
		if hasattr(crawler,"CONDITIONS"):
			# find how many tabs in $ASSERTION
			tmp  = self.template.find("$ASSERTION")
			tmp  = self.template[:tmp]
			tabs = tmp.rfind("\n")
			tabs = tmp[tabs+1:]

			assertion = []
			for key,value in crawler.CONDITIONS.items():
				new_assertion = "assert {condition}, {exception}".format(
					condition = value["condition"],
					exception = value["exception"]
				)
				assertion.append(new_assertion)
			#end for

			assertion     = ["{}{}".format(tabs,value) if idx>0 else value for idx, value in enumerate(assertion)]
			assertion     = "\n".join(assertion)
			self.template = self.template.replace(
				"$ASSERTION",
				assertion
			)
		#endif

		# Detecting what is the engine underlaying the template
		engine        = str(crawler.__class__.__base__)
		engine        = engine[engine.find("'")+1:engine.find("Template")-1]
		engine        = engine.replace(".template","")
		self.template = self.template.replace("$ENGINE",engine)