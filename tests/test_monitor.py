import os
import sys

TEST_DIR   = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.join(TEST_DIR, '..')
sys.path.insert(0, PARENT_DIR)

from lib.monitor import Monitor
import pymongo
import re
import bson

def test_capture_insert_time():
	monitor = Monitor()
	monitor.capture_insert_document("test crawler")

	conn = pymongo.MongoClient("mongodb://%s:%s/%s" % (
		monitor.config["ip"],
		monitor.config["port"],
		monitor.config["database"]
	))
	db   = conn[monitor.config["database"]]
	docs = db.status.find({"crawler_name": re.compile("test crawler", re.IGNORECASE)})

	has_document = docs.count() != 0
	if has_document:
		doc = [doc for doc in docs][0]
		assert doc["crawler_name"] == "Test Crawler"

		db.status.remove({"crawler_name": re.compile("test crawler", re.IGNORECASE)})
	conn.close()
	assert has_document
