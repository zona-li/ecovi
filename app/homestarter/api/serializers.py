from rest_framework import serializers
from .models import Project


# Serializer that map the Model instance to JSON format 
class ProjectSerializer(serializers.ModelSerializer):

	owner = serializers.ReadOnlyField(source='owner.username')
	# Map serializer's fields with the model fields. 
	class Meta:
		model = Project
		fields = ('id', 'project_name', 'owner', 'project_description', 'date_modified')
		read_only_fields = ('project_description', 'date_modified')