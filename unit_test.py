# import dateparser
# from lib.network_tools import NetworkTools
# from lib import tools

# net = NetworkTools(use_proxy=False)
# page = net.parse("http://www.welovecivic.com/forum/index.php?topic=18682.msg1837567")
# posts = tools._xpath(page,"//form[@id='quickModForm']//td[re:test(@class,'windowbg*')]")
# for post in posts:
# 	hasil = "".join(tools._xpath(post,"normalize-space(substring-before(.//table[@border='0']//span[@class='smalltext']//text()[2],'»'))"))
# 	print(hasil.encode("utf-8"))
# 	print(dateparser.parse(hasil))

import dateparser
import ftfy

hasil = ftfy.fix_encoding("20 กุมภาพันธ์ 2016, 20:31:32")
print(dateparser.parse(hasil))