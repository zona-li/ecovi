from django.shortcuts import render, redirect
from django.http import HttpResponse

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
	return redirect('https://www.facebook.com/HomelyFit-501081020234805/')

def instagram(request):
	return redirect('https://www.instagram.com/homelyfit/')

def blog(request):
	return redirect('https://medium.com/@zonali')