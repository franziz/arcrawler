import os
import sys

TEST_DIR   = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.join(TEST_DIR, '..')
sys.path.insert(0, PARENT_DIR)

from lib.factory.cleanser import CleanserFactory

def test_string_cleanser():
	test_string = "\tThis is string\r\r\r \r"

	cleanser   = CleanserFactory.get_cleanser(CleanserFactory.STRING)
	new_string = cleanser.clean(test_string)

	assert new_string == " This is string     "