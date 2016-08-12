from lib.tester.factory import TesterFactory
from curtsies		    import fmtstr

def write_summary(label_1, label_2):
	col_1        = 30
	col_2        = 30	
	label_1      = str(label_1).upper()
	label_2      = str(label_2).upper()
	label_2      = "FAILED" if label_2 == "FALSE" else "SUCCESS" if label_2 == "TRUE" else label_2
	col_1_spaces = col_1 - len(label_1)
	col_2_spaces = col_2 - len(label_2)

	if label_2 == "SUCCESS":
		label_2 = fmtstr("SUCCESS", "green")
	elif label_2 == "FAILED":
		label_2 = fmtstr("FAILED", "red")

	print("| %s%s | %s%s |" %(
		label_1,
		" " * col_1_spaces,
		label_2,
		" " * col_2_spaces
	))

if __name__ == "__main__":
	factory = TesterFactory()

	for source in factory.get_sources():
		fields = {}
		for field in source.FIELDS:
			for key,value in field.items():
				fields.update({key:value})

		thread_tester         = factory.get_tester(TesterFactory.THREAD)
		thread_link_tester    = factory.get_tester(TesterFactory.THREAD_LINK)
		last_page_link_tester = factory.get_tester(TesterFactory.LAST_PAGE_LINK)
		prev_link_tester      = factory.get_tester(TesterFactory.PREV_LINK)
		post_tester           = factory.get_tester(TesterFactory.POST)
		date_tester           = factory.get_tester(TesterFactory.DATE)
		url_tester            = factory.get_tester(TesterFactory.URL)
		content_tester        = factory.get_tester(TesterFactory.CONTENT)
		author_name_tester    = factory.get_tester(TesterFactory.CONTENT)
		title_tester          = factory.get_tester(TesterFactory.CONTENT)
			
		thread_success  	   = thread_tester.test(source)
		thread_link_success    = thread_link_tester.test(source)
		last_page_link_success = last_page_link_tester.test(source)
		prev_link_success      = prev_link_tester.test(source)
		post_success           = post_tester.test(source)
		date_success           = date_tester.test(
							         source = source,
							          props = fields["published_date"],
							          field = "published_date"
							     )
		url_success 		   = url_tester.test(
							         source = source,
							          props = fields["permalink"],
							          field = "permalink"
							     )
		content_success        = content_tester.test(
							         source = source,
							          props = fields["content"],
							          field = "content"
							     )
		author_name_success    = author_name_tester.test(
							         source = source,
							          props = fields["author_name"],
							          field = "author_name"
							     )
		title_success          = title_tester.test(
								     source = source,
									  props = fields["title"],
									  field = "title"
								 )
		
		
		total_length = 67
		print("=" * total_length)
		write_summary("CRAWLER NAME", source.CRAWLER_NAME)
		write_summary("THREAD XPATH", thread_success)
		write_summary("THREAD_LINK XPATH", thread_link_success)
		write_summary("LAST_PAGE XPATH", last_page_link_success)
		write_summary("PREV XPATH", prev_link_success)
		write_summary("POST XPATH", post_success)
		write_summary("PUBLISHED_DATE XPATH", date_success)
		write_summary("PERMALINK XPATH", url_success)
		write_summary("CONTENT XPATH", content_success)
		write_summary("AUTHOR_NAME XPATH", author_name_success)
		write_summary("TITLE XPATH", title_success)
		print("=" * total_length)

# """ This test function will test every *.py files inside ./src folder.
# 	The function, however, will not go in deep to find *.py files. 
# 	It means that the function will not perform recursive searching for *.py files.

# 	Some of the test performed are:
# 	- THREAD_XPATH
# 	- THREAD_LINK_XPATH
# 	- LAST_PAGE_XPATH
# 	- POST_XPATH
# 	- FIELDS

# 	In the FIELDS test, the test function is smartly select which one is the best
# 	tester() and preparator()

# 	underlying this function, the test.py uses lib.tester.Tester() class in order to test, 
# 	and all preparator() and test() are residented inside the lib.tester pacakage.

# 	The test function will give you summary after all *.py files test performed.
# 	It is a good practice to limit which one you want to test, because if the test
# 	fails in the middle, you will be easily see the error and why.
# """

# from lib.tester.preparator.thread import ThreadPreparator
# from lib.tester.preparator.post   import PostPreparator
# from lib.tester.last_page         import LastPageTester
# from lib.tester.date 		 	  import DateTester
# from lib.tester.string 		  	  import StringTester
# from lib.tester.url 			  import UrlTester
# from lib.tester 				  import Tester, exceptions
# from lib 						  import tools
# from curtsies					  import fmtstr
# import lxml
# import copy

# if __name__ == "__main__":
# 	tester    = Tester()
# 	sources   = tester.get_sources()
# 	summaries = []
# 	for source in sources:
# 		print("[test][debug] Testing: {}".format(source.CRAWLER_NAME))
# 		summary = []

# 		# ======================================================================
# 		#                            THREAD_XPATH                               
# 		# ======================================================================
# 		print("[test][debug] Testing THREAD_XPATH")
# 		success = tester.xpath_test(
# 			      source = source, 
# 			parent_xpath = source.THREAD_XPATH
# 		)
# 		if success:
# 			summary.append(("THREAD_XPATH", "SUCCESS"))
# 			print(fmtstr("[test][success] THREAD_XPATH test passed!", "green"))
# 		else:
# 			summary.append(("THREAD_XPATH", fmtstr("FAILED","red")))


# 		# ======================================================================
# 		#                            THREAD_LINK_XPATH                               
# 		# ======================================================================
# 		print("[test][debug] Testing THREAD_LINK_XPATH")
# 		success = tester.xpath_test(
# 			      source = source,
# 			parent_xpath = source.THREAD_XPATH,
# 			 child_xpath = source.THREAD_LINK_XPATH
# 		)
# 		if success:
# 			summary.append(("THREAD_LINK_XPATH", "SUCCESS"))
# 			print(fmtstr("[test][success] THREAD_LINK_XPATH test passed!", "green"))
# 		else:
# 			summary.append(("THREAD_LINK_XPATH", fmtstr("FAILED","red")))

# 		# ======================================================================
# 		#                            LAST_PAGE_XPATH                               
# 		# ======================================================================
# 		print("[test][debug] Testing LAST_PAGE_XPATH")
# 		success = tester.xpath_test(
# 			      source = source,
# 			  preparator = ThreadPreparator(),
# 			parent_xpath = source.LAST_PAGE_XPATH,
# 			      tester = LastPageTester(source) # Why need LastPageTester()?
# 			      								  # Because the testing logic is slightly different from BaseTester, therefore
# 		)
# 		if success:
# 			summary.append(("LAST_PAGE_XPATH", "SUCCESS"))
# 			print(fmtstr("[test][success] LAST_PAGE_XPATH test passed!", "green"))
# 		else:
# 			summary.append(("LAST_PAGE_XPATH", fmtstr("FAILED","red")))

# 		# ======================================================================
# 		#                              POST_XPATH                               
# 		# ======================================================================
# 		print("[test][debug] Testing POST_XPATH")
# 		success = tester.xpath_test(
# 				  source = source,
# 			  preparator = PostPreparator(),
# 			parent_xpath = source.POST_XPATH
# 		)
# 		if success:
# 			summary.append(("POST_XPATH", "SUCCESS"))
# 			print(fmtstr("[test][success] POST_XPATH test passed!", "green"))
# 		else:
# 			summary.append(("POST_XPATH", fmtstr("FAILED","red")))


# 		# ======================================================================
# 		#                              FIELDS                               
# 		# ======================================================================
# 		for field in source.FIELDS:
# 			items 			   = list(field.items())[0]
# 			field_name, values = items

# 			print("[test][debug] Testing \"{}\" field".format(field_name))
# 			success          = False
# 			field_tester     = None
# 			field_preparator = PostPreparator()
# 			if values["data_type"] == "date":
# 				field_tester = DateTester(source=source, concat=values["concat"], single=values["single"])
# 			elif values["data_type"] == "string":
# 				field_tester = StringTester(source=source, concat=values["concat"], single=values["single"])
# 			elif values["data_type"] == "url":
# 				field_tester 	 = UrlTester(source=source, concat=values["concat"], single=values["single"])
# 				field_preparator = PostPreparator(last_post_only=True)
# 			success = tester.xpath_test(
# 				      source = source,
# 				  preparator = field_preparator,
# 				parent_xpath = source.POST_XPATH,
# 				 child_xpath = values["xpath"],
# 				      tester = field_tester
# 			)
# 			if success:
# 				summary.append((field_name.upper(), "SUCCESS"))
# 				print(fmtstr("[test][success] \"{}\" test passed!".format(field_name), "green"))
# 			else:
# 				summary.append((field_name.upper(), fmtstr("FAILED","red")))
# 		summaries.append((source.CRAWLER_NAME, copy.copy(summary)))
# 	for summary in summaries:
# 		crawler_name, summary = summary
# 		print("============================================")
# 		print("NAME: {}".format(crawler_name))
# 		for result in summary:
# 			field, status = result
# 			print("{}: {}".format(field.upper(), status.upper()))
# 		print("============================================")
# #end if