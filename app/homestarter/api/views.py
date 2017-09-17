from django.shortcuts import render
from rest_framework import generics
from .serializers import ProjectSerializer
from .models import Project

# Define the create behavior of the api
class CreateView(generics.ListCreateAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer

	# Save the post data when creating a new project.
	def perform_create(self, serializer):
		serializer.save()

# Handle the http GET, PUT and DELETE requests.
class DetailsView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer