from .proxy_switcher import ProxySwitcher
from lxml            import html
from urllib.parse    import urlparse
import inspect
import requests
import socket
import lxml

class NetworkTools(object):
	def __init__(self, use_proxy=True):
		self.use_proxy = use_proxy

	def get_domain(self, url=None):
		assert url is not None, "url is not defined."
		url = urlparse(url)
		return '{uri.scheme}://{uri.netloc}/'.format(uri=url)

	def parse(self,url=None, parse=True):
		assert url is not None, "url is not defined."

		proxy_is_ok = False
		_html       = None
		while not proxy_is_ok:
			try:
				assert url is not None, "URL is not defined."
				
				if self.use_proxy:
					print("[networktools] Using Proxy.")
					switcher = ProxySwitcher()
					page     = requests.get(url, proxies=switcher.get_proxy(), timeout=60)
				else:
					print("[networktools] Direct Connection.")
					page = requests.get(url, timeout=60)

				_html       = html.fromstring(page.content) if parse else page.content
				proxy_is_ok = True
			except requests.exceptions.ProxyError as proxy_error:
				print("Ops! Proxy is not working. Try again...")
				proxy_is_ok = False
			except requests.exceptions.RequestException as another_requests_error: 
				print("Ops! Something wrong. Try again...")
				proxy_is_ok = False
			except socket.timeout:
				print("Ops! Request Time Out")
				proxy_is_ok = False
			except lxml.etree.XMLSyntaxError:
				print("Ops! Something wrong. Leave it~")
				_html       = html.fromstring("<html></html>")
				proxy_is_ok = True
			except:
				raise
			#end try
		#end while
		return _html
	#end def
#end class