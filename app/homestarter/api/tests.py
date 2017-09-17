from django.test import TestCase
from .models import Project
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

class ModelTestCase(TestCase):
	
	def setUp(self):
		self.project_name = "cville solar"
		self.project = Project(project_name = self.project_name)

	def test_model_create_project(self):
		old_count = Project.objects.count()
		self.project.save()
		new_count = Project.objects.count()
		self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):

	# Define the test client and other test variables.
	def setUp(self):
		self.client = APIClient()
		self.project_data = {'project_name': 'cville solar'}
		self.response = self.client.post(
			reverse('create'),
			self.project_data,
			format="json")

	# Test the api has project post, get, put delete capability.
	def test_api_can_create_project(self):
		self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

	def test_api_can_get_project(self):
		project = Project.objects.get()
		response = self.client.get(reverse('details'), kwargs={pk: project.id}, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertContains(response, project)

	def test_api_can_update_project(self):
		change_profile = {'project_name': 'another name'}
		res = self.client.put(reverse('details', kwargs={'pk': project.id}), change_profile, format='json')
		self.assertEqual(res.status_code, status.HTTP_200_OK)

	def test_api_can_delete_project(self):
		project = Project.objects.get()
		response = self.client.delete(reverse('details', kwargs={'pk': project.id}), format='json', follow=True)
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
