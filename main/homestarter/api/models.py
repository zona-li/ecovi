from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver


class Project(models.Model):
	project_name = models.CharField(max_length=255, blank=False, unique=True)
	project_description = models.TextField()
	date_modified = models.DateTimeField(auto_now=True)
	owner = models.ForeignKey('auth.User', related_name = 'projects', on_delete = models.CASCADE, default='public')

	def __str__(self):
		return "{}".format(self.name)

# This receiver handles token creation immediately a new user is created
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)