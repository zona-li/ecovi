from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import GenUserForm
from .models import Generaluser

def create_general_user(request):
	if request.method == 'POST':
		form = GenUserForm(request.POST)
		if form.is_valid():
			useremail = form.cleaned_data['email']
			usr_instance = Generaluser.objects.create(email='useremail')
			usr_instance.save()
	return render(request, 'main/home.html')

def index(request):
	return render(request, 'main/home.html')

def about(request):
	return render(request, 'main/basic.html')

def product(request):
	return render(request, 'main/product.html')

def contact(request):
	return render(request, 'main/includes/contactInfo.html')

def linkedin(request):
	return redirect('https://www.linkedin.com/company-beta/11119216/')

def facebook(request):
	return redirect('https://www.facebook.com/xptgn/')

def instagram(request):
	return redirect('https://www.instagram.com/homelyfit/')

def blog(request):
	return redirect('https://medium.com/@zonali')