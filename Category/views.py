from django.shortcuts import render, redirect
from django.http import JsonResponse
from Menu.models import Category
from django.core.paginator import Paginator
from django.contrib import messages
# Create your views here.
def index(request):

    categories_list = Category.objects.all()
    categories = Paginator(categories_list,5)
    page = request.GET.get('page')
    s = categories.get_page(page)
    nums = 'a' * s.paginator.num_pages

    return render(request, 'pages/categories/index.html', {"categories": s,'nums':nums})

def addCategory(request):

    if request.method == "POST":
        name = request.POST.get('name')
        if not name:
            messages.warning(request, 'Please provide a name for the Group.')
        else:

            try:
                Category.objects.get(name=name)
                messages.warning(request,'category already exists with same name')
            except Category.DoesNotExist:
                Category.objects.create(
                group_id = 1,
                name=request.POST['name'],
            )
                messages.success(request,'new category created')
        
            

        return redirect('/categories')
        
