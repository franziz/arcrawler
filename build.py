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
	builder.build_consumer(
		templates = templates,
		   config = config
	)

	new_documents = list()
	crawlers      = builder.get_sources("./src")
	builder._print_log("Building crawlers and tests")
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
			crawler_test_template = builder.patch_variables(
											  crawler = crawler,
										     template = crawler_test_template,
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
			builder.write_file(
				 location = "./tests",
				  content = crawler_test_template,
				file_name = "{}.py".format(crawler.CRAWLER_NAME.replace(" ","_"))
			)
		#end for
	#end for	

	# updating monitor status for queue
	for document in new_documents:
		crawler_hash = copy.copy(document["hash"])
		old_data     = [doc for doc in db.queue.find({"hash":crawler_hash})]
		del document["hash"]

		# if a have new document, add status field to new document
		# or else, preserve old status
		if len(old_data) == 0: document.update({"status":"idle"})
		# print(old_data)
		db.queue.update_one({"hash":crawler_hash},{"$set":document},upsert=True)
	#end for

	# builder.clear_build()
except exceptions.ConfigNotFound as config_not_found:
	print(config_not_found.value)
except:
	builder._print_log("Build Failed")
	builder.clear_build()
#end try