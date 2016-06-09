from pymongo import MongoClient
from forum_engine import exceptions
import glob
import shutil
import os
import json
import importlib
import copy
import hashlib
import tools
import arrow

def clear_build():
	# removing all files inside build
	print("Clearing build folder...")
	try:
		shutil.rmtree("./build")
		shutil.rmtree("./tests")
	except FileNotFoundError as file_not_found:
		pass
	#end try
#end def

# replace $VAR to STRING
def patch_variable(crawler=None, template=None, variables=None, link_to_crawl=None):
	assert crawler is not None, "crawler is not defined."
	assert template is not None, "template is not defined."
	assert variables is not None, "variables is not defined."
	assert link_to_crawl is not None, "link_to_crawl is not defined."

	new_template = copy.copy(template)

	for variable in variables:
		if "CONDITIONS" != variable and "LINK_TO_CRAWL" != variable:
			value = getattr(crawler,variable)
			value = json.dumps(value) if type(value) is dict or type(value) is list else value

			new_template = new_template.replace(
				"${}".format(variable),
				"'{}'".format(value.replace("'","\\'"))
			)
		#end if
	#end for

	# setting up for LINK_TO_CRAWL variable
	new_template = new_template.replace(
		"$LINK_TO_CRAWL",
		'"{}"'.format(link_to_crawl)
	)


	# find how many tabs in $ASSERTION
	tmp = new_template.find("$ASSERTION")
	tmp = new_template[:tmp]
	tabs = tmp.rfind("\n")
	tabs = tmp[tabs+1:]

	# setting up assertion that something need to be satisfied
	assertion=[]
	for key,value in crawler.CONDITIONS.items():
		new_assertion = "assert {condition}, {exception}".format(
			condition=value["condition"],
			exception=value["exception"]
		)
		assertion.append(new_assertion)
	#end for

	assertion = ["{}{}".format(tabs,value) if idx>0 else value for idx, value in enumerate(assertion)]
	assertion = "\n".join(assertion)
	new_template = new_template.replace(
		"$ASSERTION",
		assertion
	)

	# Detecting what is the engine underlaying the template
	engine = str(crawler.__class__.__base__)
	engine = engine[engine.find("'")+1:engine.find("Template")-1]
	engine = engine.replace(".template","")
	new_template = new_template.replace("$ENGINE",engine)

	return new_template
#end def

assert os.path.isfile("./config.json"), "Cannot find the crawler template" 
with open("./config.json","r") as f:
	config = json.load(f)
#end with

clear_build()

try:
	# copy required library to build folder
	print("Copying library...")
	success_to_copy = False
	while not success_to_copy:
		try:
			shutil.copytree("./forum_engine","./build/forum_engine")
			shutil.copytree("./proxy_switcher","./build/proxy_switcher")
			shutil.copytree("./tools","./build/tools")
			shutil.copytree("./runners","./build/runners")
			success_to_copy = True
		except FileExistsError as file_exists_error:
			shutil.rmtree("./build/forum_engine")
			shutil.rmtree("./build/proxy_switcher")
			shutil.rmtree("./build/tools")
			shutil.rmtree("./build/runners")
		#end try
	#end while

	print("Making __init__.py file")
	with open("./build/__init__.py","w") as f:
		f.write("")
		f.close()
	#end with

	print("Reading template...")
	templates = dict()
	for template in glob.glob("./templates/*.arct"):
		with open(template,"r") as f:
			template = template.split("/")[-1]
			templates.update({template:f.read()})
			f.close()
		#end with
	#end for

	print("Generating consumer...")
	consumer_template = templates["consumer.arct"]
	consumer_template = consumer_template.replace("$MAX_THREAD",str(config["workers"]))
	with open("./build/runners/consumer.py","w") as f:
		f.write(consumer_template)
		f.close()
	#end with

	# open all file inside ./src/ folder
	print("Generating build and test files...")
	if not os.path.exists('./build/crawlers'): os.mkdir('./build/crawlers')
	if not os.path.exists('./tests'): os.mkdir('./tests')

	new_documents = list()
	crawlers = glob.glob("./src/*.py")

	for crawler in crawlers:
		crawler = crawler.replace(".py","")
		crawler = crawler[len("./src/"):]
		crawler_name = copy.copy(crawler)
		
		# import the library using importlib
		crawler = importlib.import_module("src.{}".format(crawler))
		crawler = crawler.Crawler()

		assert crawler.TEMPLATE, "TEMPLATE is not defined."

		# force the LINK_TO_CRAWL to become list if it is str
		if type(crawler.LINK_TO_CRAWL) is str:
			crawler.LINK_TO_CRAWL = [crawler.LINK_TO_CRAWL]
		#end if

		assert type(crawler.LINK_TO_CRAWL) is list, "LINK_TO_CRAWL should use list as data type."

		for idx, link_to_crawl in enumerate(crawler.LINK_TO_CRAWL):
			# start to build template
			# by getting all variables and plug it on template
			variables = [attr for attr in dir(crawler) if not callable(attr) and not attr.startswith("__")]
			new_template = copy.copy(templates[crawler.TEMPLATE])
			new_test_template = copy.copy(templates["test.arct"])

			new_template = patch_variable(
				crawler=crawler,
				template=new_template, 
				variables=variables,
				link_to_crawl=link_to_crawl
			)
			new_test_template = patch_variable(
				crawler=crawler,
				template=new_test_template,
				variables=variables,
				link_to_crawl=link_to_crawl
			)

			crawler_hash = hashlib.sha256(crawler_name.encode("utf-8")).hexdigest()
			document = dict(
				hash="{}_{}".format(crawler_hash,idx),
				link=link_to_crawl,
				name=crawler.CRAWLER_NAME,
				db_to_insert=crawler.DB_SERVER_ADDRESS,
				db_name_to_insert=crawler.DB_SERVER_NAME,
				country=crawler.COUNTRY,
				last_update=arrow.utcnow().datetime,
				is_deployed=False
			)
			new_documents.append(document)
			
			# writing build file
			with open("./build/crawlers/{}_{}.py".format(crawler_hash,idx),"w") as f:
				f.write(new_template)
			#end with

			# writing test file
			with open("./tests/{}.py".format(crawler.CRAWLER_NAME.replace(" ","_"),idx),"w") as f:
				f.write(new_test_template)
			#end with 
		#end for
	#end for

	print("Saving jobs to DB...")
	# updating monitor status for queue
	db = MongoClient("mongodb://mongo:27017/monitor")
	db = db["monitor"]
	tools._force_create_index(db,"queue","hash")
	for document in new_documents:
		_hash = copy.copy(document["hash"])
		del document["hash"]
		old_data = [doc for doc in db.queue.find({"hash":_hash})]

		# if this document havent been inserted into DB,
		# make 2 more new field called status and is_deployed
		# or else, status and is_deployed fields will be preserve
		if len(old_data) == 0: document.update({"status":"idle"})
		db.queue.update({"hash":_hash},{"$set":document},upsert=True)
	#end for
except:
	clear_build()
	raise exceptions.BuildFailed("Build Failed.")
#end try