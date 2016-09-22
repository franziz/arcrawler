import jinja2
import os
import glob

class TemplateFilesExplorer:
	def __init__(self):
		pass

	def explore(self):
		template_path = os.path.join(os.getcwd(),"templates")
		file_names    = glob.iglob(os.path.join(template_path, "*.arct"))

		templates = {}
		for file_name in file_names:
			file_name = file_name.replace(template_path,"")
			file_name = file_name.replace("/","")

			loader 	 = jinja2.FileSystemLoader(searchpath=template_path)
			env 	 = jinja2.Environment(loader=loader)
			template = env.get_template(file_name)
			templates.update({file_name:template})
		return templates