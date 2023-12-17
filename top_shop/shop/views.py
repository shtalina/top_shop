from django.shortcuts import render, get_object_or_404, redirect
from .models import Users, Products, Orders, Order_items, Cart, CartItem
from .forms import EditForm
from .forms import ProductsForm
from .forms import OrdersForm
# Create your views here.

def products_list(request):
    products = Products.objects.all()

    return render(request, 'shop/products_list.html', {'products': products})

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
def createProduct(request):
    form = ProductsForm()
    if request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = ProductsForm()

    return render (request, 'shop/createProduct.html',  {'form': form})
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
        return render(request, 'product_detail.html', {'product': product})

def cart_detail(request):
    cart, created = Cart.objects.get_or_create()
    cart_items = cart.cartitem_set.all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'shop/cart_detail.html', {'cart_items': cart_items, 'total': total})

def clear_cart(request):
    cart, created = Cart.objects.get_or_create()
    cart.cartitem_set.all().delete()
    return redirect('cart_detail')

def createOrders(request):
    form = OrdersForm()
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = OrdersForm()

    return render (request, 'shop/order_info.html',  {'form': form})
