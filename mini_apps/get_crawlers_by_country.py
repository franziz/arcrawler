import os
import sys

TEST_DIR   = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.join(TEST_DIR, '..')
sys.path.insert(0, PARENT_DIR)

from lib.factory.explorer import ExplorerFactory
import click

@click.command()
@click.option("--country", help="ISO ALPHA-3 Code")
def get_country(country):
	explorer = ExplorerFactory.get_explorer(ExplorerFactory.SOURCE_FILES)
	sources  = explorer.explore()

	results = []
	for key, value in sources.items():
		if value.COUNTRY == country:
			results.append(value.CRAWLER_NAME)
	for result in results:
		click.echo(result)

if __name__ == "__main__":
	get_country()