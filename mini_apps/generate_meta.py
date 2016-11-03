""" This program will help you to create crawlers_meta, 
	please take a look at mongodb crawlers_meta for more information.

	In short, this is just crawler metadata for monitoring and other purpose.
"""
import os
import sys

TEST_DIR   = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.join(TEST_DIR, '..')
sys.path.insert(0, PARENT_DIR)

from lib.factory.explorer import ExplorerFactory
from lib.factory.saver    import SaverFactory
from lib.network_tools    import NetworkTools
import inspect

if __name__ == "__main__":
	explorer = ExplorerFactory.get_explorer(ExplorerFactory.SOURCE_FILES)
	sources  = explorer.explore()

	for key, source in sources.items():		
		document = {
			"name" : source.CRAWLER_NAME.title(),
			  "db" : {
					    "name" : source.DB_SERVER_NAME,
					    "host" : "220.100.163.132",
					    "port" : 27017,
				  "collection" : "data"
			  },
			"type" : source.TYPE
		}
		saver = SaverFactory.get_saver(SaverFactory.META)
		saver.save(document)
