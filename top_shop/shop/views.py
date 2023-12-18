from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Users, Products, Orders, Order_items, Cart, CartItem
from .forms import EditForm, ProductsForm, OrdersForm
# Create your views here.

def products_list(request):
    products = Products.objects.all()
    form = ProductsForm()
    if request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = ProductsForm()

    return render(request, 'shop/products_list.html',
                  {'products': products,
                   'form': form})

def delete_product(request, product_id):
    product = Products.objects.get(pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    else:
        return HttpResponse('Nonono!')

def users(request):

    return render(request, 'shop/users.html')

def order_list(request):
    orders = Orders.objects.all()

    return render(request, 'shop/order_list.html', {'orders': orders})

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

def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = Products.objects.get(pk=product_id)
        cart, created = Cart.objects.get_or_create()
        cart_item, created = CartItem.objects.get_or_create(product=product, cart=cart)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return redirect('cart_detail')
    else:
        # Обработка GET-запроса, например, отображение страницы продукта
        product = Products.objects.get(pk=product_id)
        return render(request, 'shop/products_list.html', {'product': product})

def cart_detail(request):
    cart, created = Cart.objects.get_or_create()
    cart_items = cart.cartitem_set.all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    form = OrdersForm()
    #Two_form = Order_itemsForm()

    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            #last_order = Orders.objects.latest('id')
            #table_order = Orders.objects.get(id=last_order.id)
            #Two_form = Order_items(order_id=table_order, product_id=3, count=548, discount=0, cost=548)
            #Two_form.save()
        else:
            form = OrdersForm()

    return render(request, 'shop/cart_detail.html', {'cart_items': cart_items, 'total': total, 'form': form})

def clear_cart(request):
    cart, created = Cart.objects.get_or_create()
    cart.cartitem_set.all().delete()
    return redirect('cart_detail')
def return_product(request):
    return redirect('products_list')

def order_info(request, id):
    order = Orders.objects.get(pk=id)
    order_detail = Order_items.objects.filter(order_id=id)

    return render(request, 'shop/order_info.html', {'order_detail': order_detail})

