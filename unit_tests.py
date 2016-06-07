# import importlib
# crawler = importlib.import_module(
# 	"build.07112dd211e98cdc57d6d7df9a4fd6d5d1e7e3669e072124772f428526dc2db7_0"
# )
# crawler = crawler.Crawler()
# crawler.crawl()

# with("./test.txt","w") as f:
# 	f.write("halo")
# 	f.close()
# #end with
# import time
# time.sleep(10)
# import shutil
# shutil.remove("./test.txt")

# from proxy_switcher import ProxyCrawler
# switcher = ProxyCrawler()
# print(switcher.crawl())

# from proxy_switcher import ProxySwitcher
# switcher = ProxySwitcher()
# print(switcher.get_proxy())










# from forum_engine import Engine
# import bson.json_util
# import json

# def crawl_callback(engine, documents):
# 	for document in documents:
# 		print(bson.json_util.dumps(document,indent=4, separators=(",",":")))
# 		# print(json.dumps(document,indent=4, separators=(",",":"), default=bson.json_util.default))
# 	#end for
# 	#engine.crawl_next()
# #end def

# engine = Engine()
# engine.set_method(engine.BACKWARD)

# # engine.set_link_to_crawl("https://www.tsikot.com/forums/more-than-looks-9/")
# # engine.set_thread_xpath("//h3[@class='threadtitle']")
# # engine.set_thread_link_xpath("./a/@href")
# # engine.set_last_page_xpath("//span[@class='first_last']/a/@href")
# # engine.set_prev_xpath("//a[@rel='prev']/@href")
# # engine.set_post_xpath("//ol[@class='posts']/li")

# # engine.add_field(
# # 	title="permalink",
# # 	xpath=".//div[@class='postbody']//span[@class='nodecontrols']/a/@href",
# # 	data_type="url"
# # )
# # engine.add_field(
# # 	title="published_date",
# # 	xpath="concat(.//span[@class='date']/text(),.//span[@class='date']/span/text())",
# # 	data_type="date"
# # )

# # engine.set_link_to_crawl("http://www.kaskus.co.id/forum/570/kendaraan-roda-4")
# # engine.set_thread_xpath("//div[@class='post-title']")
# # engine.set_thread_link_xpath("./a/@href")
# # engine.set_last_page_xpath("//a[@class='tooltips last-page']/@href")
# # engine.set_prev_xpath("//a[@class='tooltips previous-page']/@href")
# # engine.set_post_xpath("//div[@class='row nor-post']")

# # engine.add_field(
# # 	title="permalink",
# # 	xpath=".//div[@class='permalink']/a/@href",
# # 	data_type="url"
# # )
# # engine.add_field(
# # 	title="published_date",
# # 	xpath=".//time[@class='entry-date']/@datetime",
# # 	data_type="date"
# # )

# # engine.set_link_to_crawl("http://forum.detik.com/mobil-f80.html")
# # engine.set_thread_xpath("//tbody[@id='threadbits_forum_80']/tr")
# # engine.set_thread_link_xpath(".//a[re:test(@id,'thread_title_*')]/@href")
# # engine.set_last_page_xpath("//a[re:test(@title,'Last Page*')]/@href")
# # engine.set_prev_xpath("//a[@rel='prev']/@href")
# # engine.set_post_xpath("//table[re:test(@id,'post*')]")

# # engine.add_field(
# # 	title="permalink",
# # 	xpath=".//a[re:test(@id,'postcount*')]/@href",
# # 	data_type="url"
# # )
# # engine.add_field(
# # 	title="published_date",
# # 	xpath=".//tr[1]//td[1]/text()",
# # 	data_type="date",
# # 	concat=True
# # )

# engine.set_link_to_crawl("http://www.modifikasi.com/forumdisplay.php/368-Berita-Otomotif-Mobil")
# engine.set_thread_xpath("//h3[@class='threadtitle']")
# engine.set_thread_link_xpath("./a/@href")
# engine.set_last_page_xpath("//span[@class='first_last']/a/@href")
# engine.set_prev_xpath("//a[@rel='prev']/@href")
# engine.set_post_xpath("//ol[@class='posts']/li")

# engine.add_field(
# 	title="permalink",
# 	xpath=".//div[@class='posthead']//span[@class='nodecontrols']/a/@href",
# 	data_type="url"
# )
# engine.add_field(
# 	title="published_date",
# 	xpath="concat(.//span[@class='date']/text(),.//span[@class='date']/span/text())",
# 	data_type="date"
# )

# threads = engine.get_threads()
# engine.crawl(threads[1], callback=crawl_callback)