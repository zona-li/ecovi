from django.shortcuts import render
from rest_framework import generics, permissions
from .permissions import IsOwner
from .serializers import ProjectSerializer
from .models import Project
from rest_framework import permissions

# Define the create behavior of the api
class CreateView(generics.ListCreateAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner)

	# Save the post data when creating a new project.
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

# Handle the http GET, PUT and DELETE requests.
class DetailsView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner)