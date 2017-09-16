from django.test import TestCase
from .models import Project

class ModelTestCase(TestCase):
	
	def setUp(self):
		self.project_name = "cville solar"
		self.project = Project(name = self.project_name)

	def test_model_create_project(self):
		old_count = Project.objects.count()
        self.project.save()
        new_count = Project.objects.count()
        self.assertNotEqual(old_count, new_count)
