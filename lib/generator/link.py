class LinkGenerator:
	def __init__(self):
		pass

	def generate(self, domain=None, link=None):
		""" Exceptions
			- AssertionError
		"""
		assert domain    is not None                      , "domain is not defined."
		assert "http://" in domain or "https://" in domain, "domain should have http schema."
		assert link      is not None                      , "link is not defined." 

		generated_link = link
		if "http://" not in link and "https://" not in link:
			generated_link = "{domain}{link}".format(domain=domain, link=link)
		if "s=" in generated_link:
			session_string = "s="
		elif "sid=" in generated_link:
			session_string = "sid="
		elif "PHPSESSID=" in generated_link:
			session_string = "PHPSESSID="
		else:
			session_string = "s="
		if session_string in generated_link:
			session_index = generated_link.index(session_string)
			begining_link = generated_link[:session_index]
			tmp           = generated_link[session_index:]
			amp_index     = tmp.index("&") if "&" in tmp else None
			pagar_index   = tmp.index("#") if "#" in tmp else None
			if amp_index is not None and pagar_index is not None:
				ending_index = amp_index if amp_index < pagar_index else pagar_index
				ending_index = ending_index + session_index
				ending_link  = generated_link[ending_index:]
			elif amp_index is not None and pagar_index is None:
				ending_index = amp_index + session_index
				ending_link  = generated_link[ending_index:]
			elif amp_index is None and pagar_index is not None:
				ending_index = pagar_index + session_index
				ending_link  = generated_link[ending_index:]
			else:
				ending_index = -1
				ending_link  = ""
			generated_link = "".join([begining_link, ending_link])
		return generated_link