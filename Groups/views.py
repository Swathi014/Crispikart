from django.shortcuts import render, redirect
from Menu.models import Group
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):

    groups = Group.objects.all()

    return render(request, 'pages/groups/index.html', {"groups": groups})

def addGroup(request):

    if request.method == "POST":
        
        # Group.objects.create(name=request.POST['name'],)
        req = request.POST
        name = req.get('name')

        try:
            Group.objects.get(name=name)
            messages.warning(request,'category already exists with same name')
        except:
            Group.objects.create(name=name)
            messages.success(request,'new category created')

        return redirect('groups')
    
def editGroup(request):

    name = request.POST.get('name')
    g_id = request.POST.get('id')

    group = Group.objects.get(id=g_id)
    group.name = name
    group.save()
    # print(name,g_id)
    return redirect('groups')

def deleteGroup(request):
    g_id = request.POST.get('id')
    group = Group.objects.get(id=g_id)
    group.delete()
    return redirect('groups')


