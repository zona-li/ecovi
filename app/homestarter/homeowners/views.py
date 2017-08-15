from django.contrib.auth import login, authenticate
from homeowners.forms import SignUpForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/homeowners/signup_confirm/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def signup_confirm(request):
	return render(request, 'main/home.html')