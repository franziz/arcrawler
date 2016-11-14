import os
import sys

TEST_DIR   = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.join(TEST_DIR, '..')
sys.path.insert(0, PARENT_DIR)

from lib.factory.extractor import ExtractorFactory

def test_last_page_extractor():
	link            = "http://example.com/"
	last_page_xpath = "/html/body/div/h1/text()"

	extractor        = ExtractorFactory.get_extractor(ExtractorFactory.LAST_PAGE)
	extractor.domain = "http://example.com/"
	result           = extractor.extract(
		thread_link = link,
		      xpath = last_page_xpath
	)

	assert result == "http://example.com/Example Domain"

def test_last_page_extractor_cannot_find_last_page():
	link            = "http://example.com/"
	last_page_xpath = "/bad/xpath/here"

	extractor        = ExtractorFactory.get_extractor(ExtractorFactory.LAST_PAGE)
	extractor.domain = "http://example.com/"
	result           = extractor.extract(
		thread_link = link,
		      xpath = last_page_xpath
	)

	assert result == "http://example.com/"