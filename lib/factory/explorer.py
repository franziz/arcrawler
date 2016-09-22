from ..explorer.source   import SourceFilesExplorer
from ..explorer.template import TemplateFilesExplorer
from ..explorer.library  import LibraryExplorer
from ..explorer.config   import ConfigExplorer

class ExplorerFactory:
	SOURCE_FILES   = 0
	TEMPLATE_FILES = 1
	LIBRARY        = 2
	CONFIG         = 3

	def __init__(self):
		pass

	@classmethod
	def get_explorer(self, explorer_name=None):
		assert explorer_name is not None, "explorer_name is not defined."

		if explorer_name == ExplorerFactory.SOURCE_FILES:
			return SourceFilesExplorer()
		elif explorer_name == ExplorerFactory.TEMPLATE_FILES:
			return TemplateFilesExplorer()
		elif explorer_name == ExplorerFactory.LIBRARY:
			return LibraryExplorer()
		elif explorer_name == ExplorerFactory.CONFIG:
			return ConfigExplorer()