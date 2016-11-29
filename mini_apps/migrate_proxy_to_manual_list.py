import os
import sys

TEST_DIR   = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.join(TEST_DIR, '..')
sys.path.insert(0, PARENT_DIR)

import click
import pymongo

@click.command()
@click.option("--location", default=os.path.join(os.getcwd(),"data","proxy.txt"))
@click.option("--mongodb", default="mongodb://220.100.163.132/proxies")
def migrate(location, mongodb):
	conn = pymongo.MongoClient(mongodb)
	db   = conn["proxies"]

	file = open(location,"r")
	for line in file.readlines():
		line = line.replace("\n","")
		proxy = line.split(":")
		document = {
			"ip": proxy[0],
			"port": proxy[1],
			"username": proxy[2],
			"password": proxy[3]
		}
		db.manual.insert(document)
	conn.close()	

if __name__ == "__main__":
	migrate()