""" This program will help you to create crawlers_meta, 
	please take a look at mongodb crawlers_meta for more information.

	In short, this is just crawler metadata for monitoring and other purpose.
"""
from lib.factory.explorer import ExplorerFactory
from lib.factory.saver    import SaverFactory

if __name__ == "__main__":
	explorer = ExplorerFactory.get_explorer(ExplorerFactory.SOURCE_FILES)
	sources  = explorer.explore()

	for key, source in sources.items():
		document = {
			"name" : source.CRAWLER_NAME.title(),
			  "db" : {
			      		"name" : source.DB_SERVER_NAME,
			      		"host" : "220.100.163.132",
			            "port" : 27017,
			      "collection" : "data"
			  }
		}
		
		saver = SaverFactory.get_saver(SaverFactory.META)
		saver.save(document)
