import os
import shutil
import uuid
import io

class CrawlerWriter:
	def __init__(self):
		pass

	def write(self, crawler=None, **kwargs):
		assert crawler       is not None, "crawler is not defined."
		assert type(crawler) is str     , "incorrect crawler data type."

		name     = kwargs.get("name", uuid.uuid4())
		location = kwargs.get("location", os.path.join(os.getcwd()))
		location = os.path.join(location, "crawlers")

		if not os.path.isdir(location):
			os.makedirs(location)

		with io.open(os.path.join(location,"%s.py" % name),"w", encoding="utf8") as file:
			file.write(crawler)
			file.flush()
			file.close()