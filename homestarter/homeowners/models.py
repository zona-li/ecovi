from django.db import models
from search.models import Contractor
from django.contrib.auth.models import User
from django.db.models.signals import post_save	# This is sent at the end of a model’s save() method.
from django.dispatch import receiver			# Connect a receiver decorator to a signal

class Homeowner(models.Model):
	user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
	email_confirmed = models.BooleanField(default=False)
	location = models.CharField(max_length=30, blank=True)
	contractor = models.ForeignKey(Contractor, on_delete=models.SET_NULL, null=True, blank=True)

# Hook the create_user_profile, save_user_profile, and update_user_profile methods to the User model, whenever a save event occurs.
# Reference: https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Homeowner.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     # instance.homeowner.save()

# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
# 	if created:
# 		Homeowner.objects.create(user=instance)
# 	# instance.homeowner.save()