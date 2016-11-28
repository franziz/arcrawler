import os
import sys

TEST_DIR   = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.join(TEST_DIR, '..')
sys.path.insert(0, PARENT_DIR)

from lib.proxy_switcher import ProxySwitcher

def test_get_proxy():
	switcher = ProxySwitcher()
	proxy    = switcher.get_proxy()
	print(proxy)
	assert "http"     in proxy