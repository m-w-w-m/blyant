from django.db import models


class A(models.Model):
	a = models.CharField(max_length=150)

	def __str__(self):
		return self.a