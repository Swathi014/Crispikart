from django.shortcuts import render,redirect
from Orders.models import *

# Create your views here.

def list_orders(request):
    orders = Order.objects.all()
    context = {
        'orders':orders
    }
    return render(request,'pages/orders/List-orders.html', context)

def delete_order(request):
    order_id = request.POST.get('order-id')
    order = Order.objects.get(id = order_id)
    order.delete()
    return redirect('list-orders')