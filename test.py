from lib.network_tools import NetworkTools
from lib.engine.forum  import ForumEngine
from lib.factory.saver import SaverFactory
from lib.logger        import Logger

class Crawler:
	def __init__(self):
		Logger()

	def crawl(self):
		saver            = SaverFactory.get_saver(SaverFactory.POST)
		saver.db_address = "mongo:27017"
		saver.db_name    = "pakwheels"
		
		engine = ForumEngine(
			             name = "Pakwheels Crawler",
			    network_tools = NetworkTools(use_proxy=False),
			    link_to_crawl = "http://www.pakwheels.com/forums/corolla/",
			          country = "PAK",
			     thread_xpath = "//ol//li[re:test(@id,'thread*')]",
			thread_link_xpath = ".//a[@class='title']/@href",
			  last_page_xpath = "//span[@class='first_last']/a/@href",
			       prev_xpath = "//span[@class='prev_next']/a[@rel='prev']/@href",
			       post_xpath = "//ol//li[re:test(@id,'post*')]",
			           fields = [{'published_date': {'data_type': 'date', 'concat': False, 'xpath': "concat(substring-before(substring-after(substring-after(concat(.//span[@class='date']/text(),' ', .//span[@class='time']/text()),'-'),'-'),' '),'/',substring-before(substring-after(concat(.//span[@class='date']/text(),' ', .//span[@class='time']/text()),'-'),'-'),'/',substring-before(substring-after(concat(.//span[@class='date']/text(),' ', .//span[@class='time']/text()),'-'),'-'),' ',substring-after(substring-after(substring-after(concat(.//span[@class='date']/text(),' ', .//span[@class='time']/text()),'-'),'-'),' '))", 'single': True}}, {'permalink': {'data_type': 'url', 'concat': False, 'xpath': ".//div[@class='posthead']//span[@class='nodecontrols']/a[@class='postcounter']/@href", 'single': True}}, {'author_name': {'data_type': 'string', 'concat': False, 'xpath': "normalize-space(.//a[re:test(@class,'username*')]//strong/text())", 'single': True}}, {'content': {'data_type': 'string', 'concat': True, 'xpath': ".//div[@class='content']//div[re:test(@id,'post_*')]//text()", 'single': True}}, {'title': {'data_type': 'string', 'concat': True, 'xpath': "//div[@class='pagetitle']//span[@class='threadtitle']//text()", 'single': True}}]
		)
		engine.crawl(saver=saver)

if __name__ == "__main__":
	crawler = Crawler()
	crawler.crawl()



# from lib.tester.factory import TesterFactory
# from curtsies		    import fmtstr

# def write_summary(label_1, label_2):
# 	col_1        = 30
# 	col_2        = 30	
# 	label_1      = str(label_1).upper()
# 	label_2      = str(label_2).upper()
# 	label_2      = "FAILED" if label_2 == "FALSE" else "SUCCESS" if label_2 == "TRUE" else label_2
# 	col_1_spaces = col_1 - len(label_1)
# 	col_2_spaces = col_2 - len(label_2)

# 	if label_2 == "SUCCESS":
# 		label_2 = fmtstr("SUCCESS", "green")
# 	elif label_2 == "FAILED":
# 		label_2 = fmtstr("FAILED", "red")

# 	print("| %s%s | %s%s |" %(
# 		label_1,
# 		" " * col_1_spaces,
# 		label_2,
# 		" " * col_2_spaces
# 	))

# if __name__ == "__main__":
# 	factory = TesterFactory()

# 	for source in factory.get_sources():
# 		fields = {}
# 		for field in source.FIELDS:
# 			for key,value in field.items():
# 				fields.update({key:value})

# 		thread_tester         = factory.get_tester(TesterFactory.THREAD)
# 		thread_link_tester    = factory.get_tester(TesterFactory.THREAD_LINK)
# 		last_page_link_tester = factory.get_tester(TesterFactory.LAST_PAGE_LINK)
# 		prev_link_tester      = factory.get_tester(TesterFactory.PREV_LINK)
# 		post_tester           = factory.get_tester(TesterFactory.POST)
# 		date_tester           = factory.get_tester(TesterFactory.DATE)
# 		url_tester            = factory.get_tester(TesterFactory.URL)
# 		content_tester        = factory.get_tester(TesterFactory.CONTENT)
# 		author_name_tester    = factory.get_tester(TesterFactory.CONTENT)
# 		title_tester          = factory.get_tester(TesterFactory.CONTENT)
			
# 		thread_success  	   = thread_tester.test(source)
# 		thread_link_success    = thread_link_tester.test(source)
# 		last_page_link_success = last_page_link_tester.test(source)
# 		prev_link_success      = prev_link_tester.test(source)
# 		post_success           = post_tester.test(source)
# 		date_success           = date_tester.test(
# 							         source = source,
# 							          props = fields["published_date"],
# 							          field = "published_date"
# 							     )
# 		url_success 		   = url_tester.test(
# 							         source = source,
# 							          props = fields["permalink"],
# 							          field = "permalink"
# 							     )
# 		content_success        = content_tester.test(
# 							         source = source,
# 							          props = fields["content"],
# 							          field = "content"
# 							     )
# 		author_name_success    = author_name_tester.test(
# 							         source = source,
# 							          props = fields["author_name"],
# 							          field = "author_name"
# 							     )
# 		title_success          = title_tester.test(
# 								     source = source,
# 									  props = fields["title"],
# 									  field = "title"
# 								 )
		
		
# 		total_length = 67
# 		print("=" * total_length)
# 		write_summary("CRAWLER NAME", source.CRAWLER_NAME)
# 		write_summary("THREAD XPATH", thread_success)
# 		write_summary("THREAD_LINK XPATH", thread_link_success)
# 		write_summary("LAST_PAGE XPATH", last_page_link_success)
# 		write_summary("PREV XPATH", prev_link_success)
# 		write_summary("POST XPATH", post_success)
# 		write_summary("PUBLISHED_DATE XPATH", date_success)
# 		write_summary("PERMALINK XPATH", url_success)
# 		write_summary("CONTENT XPATH", content_success)
# 		write_summary("AUTHOR_NAME XPATH", author_name_success)
# 		write_summary("TITLE XPATH", title_success)
# 		print("=" * total_length)