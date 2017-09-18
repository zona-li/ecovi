from django.db import models

class Project(models.Model):
	project_name = models.CharField(max_length=255, blank=False, unique=True)
	project_description = models.TextField()
	date_modified = models.DateTimeField(auto_now=True)
	owner = models.ForeignKey('auth.User', related_name = 'projects', on_delete = models.CASCADE, default='public')

	def __str__(self):
		return "{}".format(self.name)