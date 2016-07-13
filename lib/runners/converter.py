import os
import sys

TEST_DIR = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.join(TEST_DIR, '..')
sys.path.insert(0, PARENT_DIR)

from pymongo                     import MongoClient
from lib.converter_engine.engine import Engine
from lib.converter_engine.object import MentionDB, AuthorInfoDB
import bson.json_util
import pymongo
import arrow

def mention_converter_callback(source_db=None, mention=None):
	try:
		mention_db.mention = mention
		mention_db.save()

		author_info_db.generate_info(mention)
		author_info_db.save()
	except pymongo.errors.DuplicateKeyError:
		print("[arcrawler] Ops! Duplicate mention")	
	finally:
		mention_db.set_as_converted(source_db=source_db)

if __name__ == "__main__":
	global mention_db
	global author_info_db
	mention_db     = MentionDB()
	author_info_db = AuthorInfoDB()


	engine = Engine()
	engine.convert(callback=mention_converter_callback)