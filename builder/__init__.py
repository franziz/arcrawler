import exceptions
import tools
import os
import glob
import json
import shutil
import copy
import importlib
import hashlib
import arrow

CONFIG = None
TEMPLATES = None

def _print_log(string=None):
	assert string is not None, "string is not defined."
	print("[build] {}".format(string))
#end def

def write_file(location=None, file_name=None, content=None):
	assert location  is not None, "location is not defined."
	assert file_name is not None, "file_name is not defined."
	assert content   is not None, "content is not defined."

	location = location[:-1] if "/" in location[-1] else location
	_location = "{location}/{file_name}".format(
		 location = location,
		file_name = file_name
	)

	try:
		with open(_location,"w") as f:
			f.write(content)
			f.close()
		#end with
	except FileNotFoundError as file_not_found:
		os.mkdir(location)
	#end try
#end def

def generate_monitor_document(crawler=None, crawler_hash=None, link_to_crawl=None, random_index=None):
	assert crawler_hash  is not None, "crawler_hash is not defined."
	assert link_to_crawl is not None, "link_to_crawl is not defined."
	assert crawler       is not None, "crawler is not defined."
	assert random_index  is not None, "random_index is not defined."

	complete_hash = "{}_{}".format(crawler_hash,random_index)
	document      = dict(
					 hash = complete_hash,
					 link = link_to_crawl,
				     name = crawler.CRAWLER_NAME,
		     db_to_insert = crawler.DB_SERVER_ADDRESS,
		db_name_to_insert = crawler.DB_SERVER_NAME,
		          country = crawler.COUNTRY,
		      last_update = arrow.utcnow().datetime,
		      is_deployed = False
	)
	return document
#end def

def generate_hash(crawler=None):
	""" Generating hash using CRAWLER_NAME variable. 
	    This hash is generated using sha256 variable.
	"""
	assert crawler  is not None, "crawler is not defined."
	assert crawler.CRAWLER_NAME, "CRAWLER_NAME is not defined."

	hash_string = crawler.CRAWLER_NAME.encode("utf-8")
	return hashlib.sha256(hash_string).hexdigest()
#end def

def patch_variables(crawler=None, template=None, variables=None, link_to_crawl=None):
	assert crawler       is not None, "crawler is not defined."
	assert template      is not None, "template is not defined."
	assert variables     is not None, "variables is not defined."
	assert link_to_crawl is not None, "link_to_crawl is not defined."

	# Pathcing variables
	for variable in variables:
		if "CONDITIONS" != variable and "LINK_TO_CRAWL" != variable:
			value        = getattr(crawler,variable)
			value        = json.dumps(value) if type(value) is dict or type(value) is list else value
			replace_var  = "${}".format(variable)
			replace_to	 = "'{}'".format(value.replace("'","\\'"))
			template = template.replace(replace_var, replace_to)
		#end if
	#end for

	# setting up for LINK_TO_CRAWL variable
	link         = '"{}"'.format(link_to_crawl)
	template = template.replace("$LINK_TO_CRAWL",link)

	# setting up assertion that something need to be satisfied
	if hasattr(crawler,"CONDITIONS"):
		# find how many tabs in $ASSERTION
		tmp  = template.find("$ASSERTION")
		tmp  = template[:tmp]
		tabs = tmp.rfind("\n")
		tabs = tmp[tabs+1:]

		assertion=[]
		for key,value in crawler.CONDITIONS.items():
			new_assertion = "assert {condition}, {exception}".format(
				condition = value["condition"],
				exception = value["exception"]
			)
			assertion.append(new_assertion)
		#end for

		assertion    = ["{}{}".format(tabs,value) if idx>0 else value for idx, value in enumerate(assertion)]
		assertion    = "\n".join(assertion)
		template = template.replace(
			"$ASSERTION",
			assertion
		)
	#endif

	# Detecting what is the engine underlaying the template
	engine       = str(crawler.__class__.__base__)
	engine       = engine[engine.find("'")+1:engine.find("Template")-1]
	engine       = engine.replace(".template","")
	template = template.replace("$ENGINE",engine)
	return template
#end def

def get_sources(location="./src"):
	_location = "{}/*.py".format(location)
	crawlers  = glob.glob(_location)
	crawlers  = [crawler.replace(".py","").replace("{}/".format(location),"") for crawler in crawlers]
	return crawlers
#end def

def get_variables(crawler=None):
	assert crawler is not None, "crawler is not defined."
	variables = list()
	for attribute in dir(crawler):
		if not callable(attribute) and not attribute.startswith("__"):
			variables.append(attribute)
	#end for
	return variables
#end def

def import_crawler(crawler=None):
	assert crawler       is not None, "crawler is not defined."
	assert type(crawler) is str     , "crawler has to be str."

	crawler               = importlib.import_module("src.{}".format(crawler))
	crawler               = crawler.Crawler()
	crawler.LINK_TO_CRAWL = [crawler.LINK_TO_CRAWL] if type(crawler.LINK_TO_CRAWL) is str else crawler.LINK_TO_CRAWL

	# preflight check before delivering
	assert crawler.TEST_TEMPLATE              , "TEST_TEMPLATE is not defined."
	assert crawler.TEMPLATE                   , "TEMPLATE is not defined."
	assert type(crawler.LINK_TO_CRAWL) is list, "LINK_TO_CRAWL should use list as data type."

	return crawler
#end def

def build_consumer(templates=None, config=None):
	""" This is consumer for running all the crawlers.
	    Please modify the consumer template if you want to do something with the crawler.

	    Assumption:
	    - All consumer will run any crawler which has same data structure
	"""
	_templates = templates if templates is not None else TEMPLATES
	_config    = config    if config    is not None else CONFIG

	assert _templates is not None, "templates is not defined."
	assert _config    is not None, "config is not defined."

	_print_log("Building consumer...")
	consumer_template = _templates["consumer.arct"]
	consumer_template = consumer_template.replace("$MAX_THREAD",str(config["workers"]))
	with open("./build/runners/consumer.py","w") as f:
		f.write(consumer_template)
		f.close()
	#end with
#end def

def read_template(location="./templates"):
	_print_log("Reading templates...")
	
	templates = dict()
	location  = "{}/*.arct".format(location)
	for template in glob.glob(location):
		with open(template,"r") as f:
			template = template.split("/")[-1]
			templates.update({template:f.read()})
			f.close()
		#end with
	#end for

	TEMPLATES = copy.deepcopy(templates)
	return templates
#end def

def make_init_file(location=None):
	assert location       is not None, "location is not defined."
	assert type(location) is str     , "location has to be a str."

	_print_log("Making __init__.py inside {}...".format(location))
	location = "{location}/__init__.py".format(location=location)
	with open(location,"w") as f:
		f.write("")
		f.close()
	#end with
#end def

def read_config_file():
	_print_log("Reading config...")
	tools._assert(os.path.isfile("./config.json"), exceptions.ConfigNotFound("Cannot find config."))
	with open("./config.json","r") as f:
		config = json.load(f)
	#end with

	global CONFIG
	CONFIG = copy.deepcopy(config)

	return config
#end def

def clear_build():
	try:
		_print_log("Clearing build folder...")
		shutil.rmtree("./build")

		_print_log("Clearing tests folder...")
		shutil.rmtree("./tests")
	except FileNotFoundError as file_not_found:
		pass
	#end try
#end def

def copy_requirement():
	success_to_copy = False
	while not success_to_copy:
		try:
			_print_log("Copying forum_engine...")
			shutil.copytree("./forum_engine","./build/forum_engine")

			_print_log("Copying news_engine...")
			shutil.copytree("./news_engine","./build/news_engine")

			_print_log("Copying proxy_switcher...")
			shutil.copytree("./proxy_switcher","./build/proxy_switcher")

			_print_log("Copying tools...")
			shutil.copytree("./tools","./build/tools")

			_print_log("Copying runners...")
			shutil.copytree("./runners","./build/runners")

			_print_log("Making crawlers folder...")
			if not os.path.exists('./build/crawlers'): os.mkdir('./build/crawlers')

			_print_log("Making tests folder...")
			if not os.path.exists('./tests'): os.mkdir('./tests')

			success_to_copy = True
		except FileExistsError as file_exists_error:
			shutil.rmtree("./build/forum_engine")
			shutil.rmtree("./build/news_engine")
			shutil.rmtree("./build/proxy_switcher")
			shutil.rmtree("./build/tools")
			shutil.rmtree("./build/runners")
		#end try
	#end while
#end def