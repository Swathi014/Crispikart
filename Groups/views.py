from django.shortcuts import render, redirect
from Menu.models import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from datetime import datetime
# Create your views here.

def index(request):

    groups_list = Group.objects.all()
    groups = Paginator(groups_list,5)
    page = request.GET.get('page')
    s = groups.get_page(page)
    nums = 'a' * s.paginator.num_pages

    return render(request, 'pages/groups/index.html', {"groups": s,'nums':nums})

def addGroup(request):

    if request.method == "POST":
        req = request.POST
        name = req.get('name')
        start_time = req.get('StartTime')
        end_time = req.get('EndTime')
        print(start_time,end_time)
        if not name:
            messages.warning(request, 'Please provide a name for the Group.')
        else:

            try:
                Group.objects.get(name=name)
                messages.warning(request,'Group already exists with same name')
            except Group.DoesNotExist:
                Group.objects.create(name=name,StartTime=start_time,EndTime=end_time)
                messages.success(request,'new Group created')

    return redirect('groups')
    
def editGroup(request):

    name = request.POST.get('name')
    g_id = request.POST.get('id')
    start_time = request.POST.get('StartTime')
    end_time = request.POST.get('EndTime')

    group = Group.objects.get(id=g_id)
    group.name = name
    group.StartTime = start_time
    group.EndTime = end_time
    group.save()
    # print(name,g_id)
    return redirect('groups')

def deleteGroup(request):
    g_id = request.POST.get('id')
    group = Group.objects.get(id=g_id)
    group.delete()
    return redirect('groups')




