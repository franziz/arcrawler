import os
import sys

TEST_DIR   = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.join(TEST_DIR, '..')
sys.path.insert(0, PARENT_DIR)

from lib.factory.extractor import ExtractorFactory
from lib.network_tools     import NetworkTools
import pytest

def test_thread_extractor():
	link 	     = "http://www.kaskus.co.id/forum/570/kendaraan-roda-4"
	thread_xpath = "//tr[re:test(@id,'thread*')]"

	extractor = ExtractorFactory.get_extractor(ExtractorFactory.THREAD)
	threads   = extractor.extract(link=link, xpath=thread_xpath)

	count = 0
	for thread in threads:
		count += 1
	assert count == 20

def test_thread_link_extractor_raise_exception():
	with pytest.raises(Exception):
		net  = NetworkTools(use_proxy=False)
		page = net.parse("http://example.com/")

		extractor        = ExtractorFactory.get_extractor(ExtractorFactory.THREAD_LINK)
		extractor.domain = "example.com"
		link             = extractor.extract(
			thread = page,
			 xpath = "/html/body/div/h1/text()"
		)

def test_thread_link_extractor():
	net  = NetworkTools(use_proxy=False)
	page = net.parse("http://example.com/")

	extractor        = ExtractorFactory.get_extractor(ExtractorFactory.THREAD_LINK)
	extractor.domain = "http://example.com/"
	link             = extractor.extract(
		thread = page,
		 xpath = "/html/body/div/h1/text()"
	)
	assert link == "http://example.com/Example Domain"
