from django.db import models

class Contractor(models.Model):
	name = models.CharField(max_length=100)
	contactInfo = models.TextField()
	specialties = models.TextField()
	ratings = models.IntegerField()

	def __str__(self):
		return self.name