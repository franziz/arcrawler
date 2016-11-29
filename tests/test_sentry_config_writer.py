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
	writer = WriterFactory.get_writer(WriterFactory.SENTRY_CONFIG)
	writer.write(location=os.path.join(os.getcwd(),"sentry_test"))

	file = open(os.path.join(os.getcwd(), "sentry_test", "config", "sentry.json"))
	content = file.read()
	content = json.loads(content)

	found_sentry = "sentry" in content

	# Clean up
	shutil.rmtree(os.path.join(os.getcwd(), "sentry_test"))
	assert found_sentry == True