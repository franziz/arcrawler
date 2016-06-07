from pymongo import MongoClient

db = MongoClient("mongodb://mongo:27017/monitor")
db = db.monitor

documents = [document for document in db.queue.find({"is_deployed":False})]

assert len(documents) > 0, "No undeployed jobs."

print("Which one do you want to deploy?")
for idx, document in enumerate(documents): 
	print("{}. [{}] {}".format(idx+1, document["name"], document["link"]))
print("{}. All".format(len(documents)+1))

try:
	selection = input("Selection: ")
	selection = int(selection)
except:
	raise exceptions.ConversionError("Cannot convert data type")
#end try

assert selection >= 1 and selection <= len(documents)+1, "Invalid input."
selection = selection - 1
documents = [documents[selection]] if selection != len(documents) else documents
for document in documents:
	db.queue.update_one(
		{"hash":document["hash"]},
		{"$set":{
			"is_deployed":True
		}}
	)
#end for

# db.queue.update_many({"is_deployed":False},{"$set":{"is_deployed":True}})