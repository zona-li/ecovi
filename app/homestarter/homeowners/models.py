from django.db import models
from search.models import Contractor

class Homeowner(models.Model):
	username = models.CharField(max_length=100)
	useremail = models.EmailField(max_length=70)
	firstname = models.CharField(max_length=25)
	lastname = models.CharField(max_length=25)
	password = models.CharField(max_length=50)
	contractor = models.ForeignKey(Contractor, on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		return self.username
