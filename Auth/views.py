from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# def login(request):
#     return render(request, 'auth/login.html')

# def login_request(request):
# 	if request.method == "POST":
# 			username = request.POST['username']
# 			password = request.POST['password']
# 			user = authenticate(username=username, password=password)
			

# 	return redirect('/dashboard')


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request,'incorrect username or password')
            return redirect('sign-in')
    return render(request,'auth/login.html')

@login_required
def signout(request):
    logout(request)
    return redirect('sign-in')