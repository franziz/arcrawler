from pymongo import MongoClient
import pika
import bson.json_util

is_connected = False
max_try      = 10
tried        = 0
while not is_connected and tried< max_try:
	try:
		connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
		channel    = connection.channel()
		channel.queue_declare(queue='crawlers', durable=True)

		is_connected = True
	except pika.exceptions.ConnectionClosed as connection_closed:
		tried = tried + 1
	#end try
#end while

assert tried < max_try,"Max try exceeded."

db = MongoClient("mongodb://mongo:27017/monitor")
db = db.monitor

for document in db.queue.find({"status":"idle", "is_deployed":True}):
	db.queue.update({"hash":document["hash"]},{"$set":{"status":"publishing"}})
	channel.basic_publish(
		   exchange = '',
		routing_key = 'crawlers',
		       body = bson.json_util.dumps(document),
		 properties = pika.BasicProperties(
						delivery_mode = 2, # make message persistent,
						 content_type = "application/json"
					)
	)
	db.queue.update({"hash":document["hash"]},{"$set":{"status":"queuing"}})
#end for
connection.close()