from django.shortcuts import render, redirect
from django.http import JsonResponse
from Menu.models import Category
# Create your views here.
def index(request):

    categories = Category.objects.all()
    return render(request, 'pages/categories/index.html', {"categories": categories})

def addCategory(request):

    if request.method == "POST":
        
        category = Category.objects.create(
            group_id = 1,
            name=request.POST['name'],
        )

        return redirect('/categories')
        

