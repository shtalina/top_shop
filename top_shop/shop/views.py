from django.shortcuts import render, get_object_or_404, redirect
from .models import Users, Products, Orders, Order_items
from .forms import EditForm
# Create your views here.

def products_list(request):
    products = Products.objects.all()

    return render(request, 'shop/products_list.html', {'products': products})

def cart(request):

    return render(request, 'shop/cart.html')

def users(request):

    return render(request, 'shop/users.html')

def order_list(request):
    orders = Orders.objects.all()

    return render(request, 'shop/order_list.html', {'orders': orders})

def order_info(request, order_id):
    order = Orders.objects.get(pk=order_id)
    data = Order_items.objects.get(pk=order_id)


    return render(request, 'shop/order_info.html', {'data': data, 'order': order})

def edit_order(request, order_id):
    edit = get_object_or_404(order_items, pk=order_id)

    if request.method == 'POST':
        form = EditForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('order_info', order_id=order_id)
    else:
        form = EditForm(instance=edit)

    return render(request, 'edit_order.html', {'form': form, 'edit': edit})



