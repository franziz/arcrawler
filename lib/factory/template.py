from ..template.mention import MentionTemplate

class TemplateFactory:
	MENTION = 0	

	def __init__(self):
		pass

	@classmethod
	def get_template(self, template_name=None):
		assert template_name is not None, "template_name is not defined."

		if template_name == TemplateFactory.MENTION:
			return MentionTemplate()