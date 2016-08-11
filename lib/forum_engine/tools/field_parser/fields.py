from .    import Parser
from .... import tools

class Fields(Parser):
	def __init__(self):
		pass

	def parse(self, post=None, xpath=None, props=None, field=None):
		assert post  is not None, "post is not defined."
		assert xpath is not None, "xpath is not defined."
		assert props is not None, "props is not defined."
		assert field is not None, "field is not defined."

		value = tools._xpath(post,xpath)
		if len(value) == 0:
			value = []
			print("[forum_engine][error] Cannot find {} given XPATH.".format(field))
		# if the props is not single, but they want to concat, it means force it to single value and concat
		if (props["single"] and props["concat"]) or (not props["single"] and props["concat"]):
			value = " ".join(value)
			value = str(value)
		elif props["single"] and not props["concat"]:
			value = value[0] if type(value) is list and len(value)>0 else value
			value = str(value)
		else:
			value = list(value)		

		# removing some unwanted data such as \xc2\xa0
		if type(value) is str:
			value = tools._clean_string(value)
		elif type(value) is list:
			value = [tools._clean_string(r) for r in value]		
		return value