import os
import sys

TEST_DIR = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.join(TEST_DIR, '..')
sys.path.insert(0, PARENT_DIR)

from lib.converter_engine.engine import Engine
from curtsies                    import fmtstr
import time
import random
import pymongo

if __name__ == "__main__":
	while True:
		engine = Engine()
		engine.convert()

		rnd = random.randint(60,360)
		print("=" * 100)
		print("Sleeping %s" % rnd)
		print("=" * 100)
		time.sleep(rnd)