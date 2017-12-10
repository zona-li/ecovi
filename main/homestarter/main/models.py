from django.db import models

class Generaluser(models.Model):
	email = models.EmailField(max_length=50)

	def __str__(self):
		return self.email