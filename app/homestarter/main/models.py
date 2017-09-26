from django.db import models

class Generaluser(models.Model):
	email = models.EmailField(max_length=50)
