import os
import sys

TEST_DIR   = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.join(TEST_DIR, '..')
sys.path.insert(0, PARENT_DIR)

from lib.factory.writer import WriterFactory
import os
import json
import shutil

def test_write():
	writer = WriterFactory.get_writer(WriterFactory.MONITOR_CONFIG)
	writer.write(location=os.path.join(os.getcwd(),"monitor_test"))

	file = open(os.path.join(os.getcwd(), "monitor_test", "config", "monitor.json"))
	content = file.read()
	content = json.loads(content)

	found_monitor = "monitor" in content
	assert found_monitor == True