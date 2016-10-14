from lib.engine.news   import NewsEngine
from lib.factory.saver import SaverFactory

if __name__ == "__main__":
	engine = NewsEngine(
		                name = "Anycar Crawler",
		             country = "VNM",
		       category_link = "http://anycar.vn/tin-tuc/thi-truong-quoc-te-nc11-nsc22.html",
		       article_xpath = "//div[@class='box-title']/h4/a/@href",
		         title_xpath = "//h1[@class='title-news-detail']/text()",
		published_date_xpath = "concat(substring(substring-after(//p[@class='time-posted']/text(),','),11,2),'/',substring(substring-after(//p[@class='time-posted']/text(),','),2,2),'/',substring(substring-after(//p[@class='time-posted']/text(),','),18))",
		   author_name_xpath = "concat('Anycar','')" ,
		       content_xpath = "//div[@class='detail-news-cont']//text()"
	)
	engine.crawl(saver=SaverFactory.get_saver(SaverFactory.ARTICLE))