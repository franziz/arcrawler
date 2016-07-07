import os
import sys

TEST_DIR = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.join(TEST_DIR, '..')
sys.path.insert(0, PARENT_DIR)

import lib.proxy_switcher

crawler = lib.proxy_switcher.ProxyCrawler()
crawler.crawl()