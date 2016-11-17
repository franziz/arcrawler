import os
import sys

TEST_DIR   = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.join(TEST_DIR, '..')
sys.path.insert(0, PARENT_DIR)

import pymongo
import click
import re
import arrow

@click.command()
@click.option("--crawler_name", prompt="Crawler Name")
@click.option("--host", default="220.100.163.132", prompt="Host")
@click.option("--port", default=27017, prompt="Port")
@click.option("--database", default="news_crawler", prompt="Database")
def check(crawler_name, host, port, database):
	conn = pymongo.MongoClient("mongodb://%s:%s/%s" % (host, port, database))
	db   = conn[database]

	count         = db.data.count({"_crawled_by": re.compile(crawler_name, re.IGNORECASE)})
	last_document = db.data.find({"_crawled_by": re.compile(crawler_name, re.IGNORECASE)}).sort([("_insert_time",pymongo.DESCENDING)]).limit(1)
	last_document = [doc for doc in last_document][0]

	last_insert_date = arrow.get(last_document["_insert_time"]).to("Asia/Singapore").humanize()

	click.echo("Total Document: %s" % count)
	click.echo("Last Document ID: %s" % last_document["_id"])
	click.echo("Last Insert Date: %s" % last_insert_date)
	conn.close()

if __name__ == "__main__":
	check()