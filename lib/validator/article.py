from ..exceptions import ValidationError

class ArticleValidator:
	def __init__(self):
		pass

	def validate(self, article=None):
		assert article is not None, "article is not defined."

		if "title" not in article:
			raise ValidationError("Cannot find 'title' inside article")

		if "published_date" not in article:
			raise ValidationError("Cannot find 'published_date' inside article")

		if "author_name" not in article:
			raise ValidationError("Cannot find 'author_name' inside article")

		if "content" not in article:
			raise ValidationError("Cannot find 'content' inside article")

		if not article["content"]:
			raise ValidationError("content cannot be emtpy.")

		if not article["title"]:
			raise ValidationError("title cannot be empty.")

		if not article["published_date"]:
			raise ValidationError("published_date cannot be empty.")

		if not article["author_name"]:
			raise ValidationError("author_name cannot be empty.")
		