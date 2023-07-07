from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages

def login(request):
    return render(request, 'auth/login.html')

def login_request(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		# login(user)
	return redirect('/dashboard')