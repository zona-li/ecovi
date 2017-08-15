from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    firstname = forms.CharField(max_length=30, required=False, help_text='Optional.')
    lastname = forms.CharField(max_length=30, required=False, help_text='Optional.')
    useremail = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'firstname', 'lastname', 'useremail', 'password',)