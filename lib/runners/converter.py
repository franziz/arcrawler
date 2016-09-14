import os
import sys

TEST_DIR = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.join(TEST_DIR, '..')
sys.path.insert(0, PARENT_DIR)

from lib.converter_engine.engine import Engine
from lib.converter_engine.object import MentionDB, AuthorInfoDB
from multiprocessing 			 import Pool
import bson.json_util
import pymongo
import arrow

# def execute_worker(args=None):
# 	source_db, document = args
# 	print(document)

# def mention_converter_callback(source_db=None, documents=None):
# 	with Pool(10) as pool:
# 		documents = [(source_db, document) for document in documents]
# 		pool.map(execute_worker, documents)
	# mention_db     = MentionDB()
	# author_info_db = AuthorInfoDB()
	# try:
	# 	mention_db.mention = mention
	# 	mention_db.save()

	# 	author_info_db.generate_info(mention)
	# 	author_info_db.save()
	# 	print("[arcrawler][debug] Converted one document!")
	# except pymongo.errors.DuplicateKeyError:
	# 	print("[arcrawler][error] Ops! Duplicate mention")
	# finally:
	# 	mention_db.delete_source(source_db=source_db)

if __name__ == "__main__":
	engine = Engine()
	engine.convert()
	# engine.convert(callback=mention_converter_callback)