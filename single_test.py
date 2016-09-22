from lib.factory.extractor import ExtractorFactory
from lib.network_tools     import NetworkTools

if __name__ == "__main__":
	last_page     = "http://www.kaskus.co.id/thread/54a8f734c1cb176d188b4569/all-about-car-audio---part-1/329"
	network_tools = NetworkTools(use_proxy=False)
	page          = network_tools.parse(last_page)

	extractor        = ExtractorFactory.get_extractor(ExtractorFactory.PREV_PAGE)
	extractor.domain = NetworkTools.get_domain(last_page)

	print(extractor.extract(
		last_page = page,
		    xpath = "//a[@class='tooltips previous-page']/@href"
	))
