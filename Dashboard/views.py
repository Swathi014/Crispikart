from django.shortcuts import render
from django.contrib.auth.models import User

def index(request):

    user = {'name': User.get_username}

    return render(request, 'pages/dashboard.html', user)