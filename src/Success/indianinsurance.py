from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "indianinsurance"
	CRAWLER_NAME = "indianinsurance crawler"
	LINK_TO_CRAWL = [
		"http://www.indianinsurance.com/forumdisplay.php/2-Indian-Insurance-Announcements-Indian-Insurance-Updates?",
		"http://www.indianinsurance.com/forumdisplay.php/3-Indian-Insurance-News-Insurance-News-India?",		
		"http://www.indianinsurance.com/forumdisplay.php/6-Meet-and-Greet-Members-India-Insurance-Online?",
		"http://www.indianinsurance.com/forumdisplay.php/7-Indian-Insurance-Industry-Insurance-Sector-in-India?",		
		"http://www.indianinsurance.com/forumdisplay.php/12-Life-Insurance-Corporation-of-India?",
		"http://www.indianinsurance.com/forumdisplay.php/16-Bajaj-Allianz-Life-Insurance?",		
		"http://www.indianinsurance.com/forumdisplay.php/18-HDFC-Standard-Life-Insurance?",				
		"http://www.indianinsurance.com/forumdisplay.php/21-Max-New-York-Life-Insurance?",
		"http://www.indianinsurance.com/forumdisplay.php/22-MetLife-India-Insurance-Company?",
		"http://www.indianinsurance.com/forumdisplay.php/23-Kotak-Mahindra-Old-Mutual-Life-Insurance?",
		"http://www.indianinsurance.com/forumdisplay.php/24-SBI-Life-Insurance?",
		"http://www.indianinsurance.com/forumdisplay.php/28-Reliance-Life-Insurance-Company?",
		"http://www.indianinsurance.com/forumdisplay.php/25-TATA-AIG-Life-Insurance-Company?",
		"http://www.indianinsurance.com/forumdisplay.php/27-Aviva-Life-Insurance-India?",
		"http://www.indianinsurance.com/forumdisplay.php/72-Star-Union-Dai-ichi-Life-Insurance-Co.?",
		"http://www.indianinsurance.com/forumdisplay.php/75-IDBI-Fortis-Life-Insurance-Co.?",
		"http://www.indianinsurance.com/forumdisplay.php/77-Sahara-India-Life-Insurance-Company?",
		"http://www.indianinsurance.com/forumdisplay.php/78-Shriram-Life-Insurance?",
		"http://www.indianinsurance.com/forumdisplay.php/79-Bharti-AXA-Life-Insurance?",
		"http://www.indianinsurance.com/forumdisplay.php/80-Future-Generali-India-Life-Insurance?",		
		"http://www.indianinsurance.com/forumdisplay.php/82-AEGON-Religare-Life-Insurance?",
		"http://www.indianinsurance.com/forumdisplay.php/83-DLF-Pramerica-Life-Insurance?",		
		"http://www.indianinsurance.com/forumdisplay.php/30-New-India-Assurance-Company?",
		"http://www.indianinsurance.com/forumdisplay.php/32-United-India-Insurance-Company?",
		"http://www.indianinsurance.com/forumdisplay.php/31-Oriental-Insurance-Company?",		
		"http://www.indianinsurance.com/forumdisplay.php/38-TATA-AIG-General-Insurance?",
		"http://www.indianinsurance.com/forumdisplay.php/99-Bharti-AXA-General-Insurance?",
		"http://www.indianinsurance.com/forumdisplay.php/33-Bajaj-Allianz-General-Insurance?",		
		"http://www.indianinsurance.com/forumdisplay.php/36-Reliance-General-Insurance?",
		"http://www.indianinsurance.com/forumdisplay.php/35-IFFCO-Tokio-General-Insurance?",
		"http://www.indianinsurance.com/forumdisplay.php/41-HDFC-ERGO-General-Insurance?",
		"http://www.indianinsurance.com/forumdisplay.php/98-Future-Generali-India-General-Insurance?",		
		"http://www.indianinsurance.com/forumdisplay.php/37-Royal-Sundaram-General-Insurance?",		
		"http://www.indianinsurance.com/forumdisplay.php/15-General-Insurance-Corporation-of-India",				
		"http://www.indianinsurance.com/forumdisplay.php/62-TATA-AIG-Travel-Insurance?",		
		"http://www.indianinsurance.com/forumdisplay.php/64-ICICI-Lombard-Travel-Insurance?",		
		"http://www.indianinsurance.com/forumdisplay.php/49-Indian-Health-Insurance-Health-Insurance-India?",		
		"http://www.indianinsurance.com/forumdisplay.php/60-ICICI-Lombard-Health-Insurance?",		
		"http://www.indianinsurance.com/forumdisplay.php/61-Apollo-Munich-Health-Insurance?",								
		"http://www.indianinsurance.com/forumdisplay.php/94-ICICI-Lombard-Student-Insurance?",				
		"http://www.indianinsurance.com/forumdisplay.php/97-Oriental-Home-Insurance?",				
		"http://www.indianinsurance.com/forumdisplay.php/71-TATA-AIG-Life-Insurance?",
		"http://www.indianinsurance.com/forumdisplay.php/73-Star-Union-Dai-ichi-Life-Insurance?",		
		"http://www.indianinsurance.com/forumdisplay.php/76-IDBI-Fortis-Life-Insurance?",
		"http://www.indianinsurance.com/forumdisplay.php/84-Life-Insurance-Corporation-of-India?",
		"http://www.indianinsurance.com/forumdisplay.php/85-Reliance-Life-Insurance?",
		"http://www.indianinsurance.com/forumdisplay.php/86-ICICI-Prudential-Life-Insurance?",
		"http://www.indianinsurance.com/forumdisplay.php/90-Bajaj-Allianz-Life-Insurance?",		
		"http://www.indianinsurance.com/forumdisplay.php/91-Indian-Insurance-Job-Insurance-Jobs-in-India?",
		"http://www.indianinsurance.com/forumdisplay.php/46-Indian-Insurance-Agent-Insurance-Agents-in-India?",
		"http://www.indianinsurance.com/forumdisplay.php/9-Insurance-Regulatory-and-Development-Authority-IRDA-India?",
		"http://www.indianinsurance.com/forumdisplay.php/44-Indian-Insurance-Ombudsmen-Insurance-Complaint-amp-Grievances-in-India?",				
		"http://www.indianinsurance.com/forumdisplay.php/89-Indian-General-Insurance-Council-General-Insurance-Council-in-India?"
        ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//ol[@class='stickies' or @class='threads']//li[re:test(@class,'thread_*')]"
	THREAD_LINK_XPATH = ".//a[re:test(@id,'thread_title_*')]/@href"
	LAST_PAGE_XPATH = "//div[@class='pagination_top']//span[@class='first_last']/a/@href"
	PREV_XPATH = "//div[@class='pagination_top']//span[@class='prev_next']/a/@href"
	POST_XPATH = "//ol[@class='posts']/li[re:test(@id,'post_*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			# "xpath":"substring-before(.//span[@class='date']//text(),'GMT')"
			"xpath":".//span[@class='date']//text()"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//div[@class='userinfo']//a/strong/text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[re:test(@class,'postrow*')]//text()"
			# "xpath":".//div[@class='postrow']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//a[@class='postcounter']/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//span[@class='threadtitle']//text()"
			# "xpath":"//div[@class='pagetitle']/h1/span[@class='threadtitle']//text()"
		}}       
	]
	CONDITIONS={
		"has_to_have_content":{
			"condition":'"content" in document',
			"exception":'"Content is not defined"'
		},
		"content_cannot_be_empty":{
			"condition":'len(document["content"]) > 0',
			"exception":'"Content cannot be empty"'
		}
	}
#end class
