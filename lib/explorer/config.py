import os
import shutil

class ConfigExplorer:
	def __init__(self):
		pass

	def copy(self, file_or_folder=None, **kwargs):
		assert file_or_folder is not None, "file_or_folder is not defined."

		origin_location = kwargs.get("origin_location", os.path.join(os.getcwd(),"config"))
		target_location = kwargs.get("target_location", os.path.join(os.getcwd()))

		outside_lib = kwargs.get("outside_lib", False)
		if not outside_lib:
			target_location = os.path.join(target_location,"config")
		
		origin_file = kwargs.get("origin_file", os.path.join(origin_location, file_or_folder))
		target_file = kwargs.get("target_file", os.path.join(target_location, file_or_folder))

		if os.path.isdir(origin_file):
			shutil.copytree(origin_file, target_file)
		elif os.path.isfile(origin_file):
			shutil.copyfile(origin_file, target_file)
		return True