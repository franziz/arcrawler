""" Assumptions lies on the build.py are
	- Assume that the docker machine is dead, so it is safe for the builder to remove all the queue document
	  inside monitor database.
"""

from pymongo import MongoClient
from lib     import exceptions, builder, tools
import pymongo
import copy

try:
	config = builder.read_config_file()

	db = MongoClient("mongodb://mongo:27017/monitor")
	db = db["monitor"]
	tools._force_create_index(db,"queue","hash")

	builder.clear_build()
	builder.copy_requirement()
	builder.make_init_file("./build")

	templates = builder.read_template()

	new_documents = list()
	crawlers      = builder.get_sources("./src")
	builder._print_log("Building crawlers")
	for crawler in crawlers:
		crawler   = builder.import_crawler(crawler=crawler)
		variables = builder.get_variables(crawler=crawler)
		
		for idx, link_to_crawl in enumerate(crawler.LINK_TO_CRAWL):
			crawler_hash          = builder.generate_hash(crawler=crawler)
			crawler_template      = copy.copy(templates[crawler.TEMPLATE])
			crawler_test_template = copy.copy(templates[crawler.TEST_TEMPLATE])

			crawler_template 	  = builder.patch_variables(
										      crawler = crawler,
										     template = crawler_template,
										    variables = variables,
										link_to_crawl = link_to_crawl
									)
			document              = builder.generate_monitor_document(
										      crawler = crawler,
										 crawler_hash = crawler_hash,
										 random_index = idx,
										link_to_crawl = link_to_crawl
									)
			new_documents.append(copy.deepcopy(document))
			builder.write_file(
				 location = "./build/crawlers",
				  content = crawler_template,
				file_name = "{crawler_hash}_{random_index}.py".format(
								crawler_hash = crawler_hash,
								random_index = idx
							)
			)
		#end for
	#end for	

	# updating monitor status for queue
	builder._print_log("Saving to database...")	
	db.queue.remove({})
	for document in new_documents:
		crawler_hash = copy.copy(document["hash"])
		db.queue.update_one({"hash":crawler_hash},{"$set":document},upsert=True)			
	builder._print_log("Build Success!")	
except exceptions.ConfigNotFound as config_not_found:
	print(config_not_found.value)
except:
	builder._print_log("Build Failed!")
	builder.clear_build()
	raise
#end try