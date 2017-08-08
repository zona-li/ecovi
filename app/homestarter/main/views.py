from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'main/home.html')

def contact(request):
	return render(request, 'main/basic.html', {'category':['For homeowners: ','For contractors: '], 'products':['remodeling','designing','energy consulting']})
