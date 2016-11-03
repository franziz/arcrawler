import os
import sys

TEST_DIR   = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.join(TEST_DIR, '..')
sys.path.insert(0, PARENT_DIR)

from lib.factory.explorer import ExplorerFactory
import bson.json_util

if __name__ == "__main__":
	explorer = ExplorerFactory.get_explorer(ExplorerFactory.SOURCE_FILES)
	sources  = explorer.explore()

	countries = {}
	for key, value in sources.items():
		if value.COUNTRY not in countries:
			countries.update({value.COUNTRY:1})
		countries[value.COUNTRY] += 1
	print(bson.json_util.dumps(countries, indent=4))