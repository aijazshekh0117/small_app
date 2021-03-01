from django.db import models


class Answers(models.Model):
	ans_id = models.BigIntegerField(primary_key=True)
	answare = models.CharField(max_length=100)

	class meta:
		pass