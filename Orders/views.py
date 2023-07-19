from django.shortcuts import render,redirect
from Orders.models import *
from django.core.paginator import Paginator

# Create your views here.

def list_orders(request):
    orders_list = Order.objects.all()
    orders = Paginator(orders_list,5)
    page = request.GET.get('page')
    s = orders.get_page(page)
    nums = 'a' * s.paginator.num_pages

    return render(request,'pages/orders/List-orders.html', {"orders": s,'nums':nums})

def delete_order(request):
    order_id = request.POST.get('order-id')
    order = Order.objects.get(id = order_id)
    order.delete()
    return redirect('list-orders')