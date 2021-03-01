from django.db import models
from .answers import Answers


class Questions(models.Model):
	question_id = models.BigAutoField(primary_key=True)
	question = models.TextField()
	answers = models.ForeignKey(Answers, on_delete=models.PROTECT)

	class Meta:
		pass