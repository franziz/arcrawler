import os
import sys

TEST_DIR   = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.join(TEST_DIR, '..')
sys.path.insert(0, PARENT_DIR)

from lib.factory.explorer  import ExplorerFactory
from lib.factory.extractor import ExtractorFactory
from lib.exceptions        import CannotFindCrawler
import click
import copy

@click.command()
@click.option("--crawler_name", prompt="Crawler Name")
def check(crawler_name):
	explorer     = ExplorerFactory.get_explorer(ExplorerFactory.SOURCE_FILES)
	sources      = explorer.explore()
	crawler_name = crawler_name.title()

	if crawler_name not in sources:
		raise CannotFindCrawler("Cannot find %s" % crawler_name)

	crawler   = copy.deepcopy(sources[crawler_name])
	extractor = ExtractorFactory.get_extractor(ExtractorFactory.ARTICLE_LINK)
	for category_link in crawler.CATEGORY_LINKS:
		click.echo("=" * 100)
		click.echo(category_link)

		articles = extractor.extract(
			 home = category_link,
			xpath = crawler.ARTICLE_XPATH
		)
		for article in articles:
			if "//" in article:
				raise Exception("URL error")
		click.echo("Got %s article" % len(articles))
if __name__ == "__main__":
	check()