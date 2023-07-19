from django.shortcuts import render, redirect
from Menu.models import Group
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.core.exceptions import ValidationError
# Create your views here.

def index(request):

    groups_list = Group.objects.all()
    groups = Paginator(groups_list,15)
    page = request.GET.get('page')
    s = groups.get_page(page)
    
    groupsCount = Group.objects.count()

    return render(request, 'pages/groups/index.html', {"groups": s, 'groupsCount': groupsCount})

def addGroup(request):

    if request.method == "POST":        
        req = request.POST
        try:
            name_field = req.get('name', '').strip()
            errors = {}
            if not name_field:
                errors['name'] = 'Group name field is required'
            if Group.objects.filter(name=name_field).exists():
                errors['name'] = 'Group is already exists with same name'
            if errors:
                return JsonResponse(errors, status=400)    
            Group.objects.create(name=name_field)        
            return JsonResponse({"message": "Group created successfully"})
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=500)

    
def editGroup(request):

    req = request.POST
    g_id = request.POST.get('id')

    try:
        name_field = req.get('name', '').strip()
        errors = {}
        if not name_field:
            errors['name'] = 'Group name field is required'
        if Group.objects.exclude(id = g_id).filter(name = name_field).exists():
            errors['name'] = 'Group is already exists with same name'
        if errors:
            return JsonResponse(errors, status=400)    

        group = Group.objects.get(id=g_id)
        group.name = name_field
        group.save()
        return JsonResponse({"message": "Group updated successfully"})
    except ValidationError as e:    
         return JsonResponse({'error': str(e)}, status=500)
    

def deleteGroup(request):
    
    g_id = request.POST.get('id')
    group = Group.objects.get(id=g_id)
    group.delete()
    
    return JsonResponse({"message": "Group deleted successfully"})





