from rest_framework.permissions import BasePermission
from .models import Project

class IsOwner(BasePermission):
	"""Custom permission class to allow only project owners to edit them."""

	def has_object_permission(self, request, view, obj):
		"""Retuen True if permission is granted to the project owner."""
		if isinstance(obj, Project):
			return obj.owner == request.user
		return obj.owner == request.user