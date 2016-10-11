""" This program will help you to create crawlers_meta, 
	please take a look at mongodb crawlers_meta for more information.

	In short, this is just crawler metadata for monitoring and other purpose.
"""
from lib.factory.explorer import ExplorerFactory
from lib.factory.saver    import SaverFactory
from lib.network_tools    import NetworkTools

if __name__ == "__main__":
	explorer = ExplorerFactory.get_explorer(ExplorerFactory.SOURCE_FILES)
	sources  = explorer.explore()

	for key, source in sources.items():
		old_domain = NetworkTools.get_domain(source.LINK_TO_CRAWL[0], with_scheme=False)
		new_domain = old_domain.lower().replace("www.","")
		domain     = "%s%s" % (new_domain[0].title(), new_domain[1:])
		print("Changing %s to %s" % (old_domain, domain))

		document = {
			"domain" : domain,
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
