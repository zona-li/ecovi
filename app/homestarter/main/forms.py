from django.forms import ModelForm
from .models import Generaluser

class GenUserForm(ModelForm):
	class Meta:
		model = Generaluser
		fields = ['email']