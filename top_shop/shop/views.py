from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Users, Products, Orders, Order_items, Cart, CartItem, OrderItem
from .forms import EditForm, ProductsForm, OrdersForm, UsersForm
from django.http import JsonResponse
from django.db import transaction
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
    users = Users.objects.all()
    form = UsersForm()
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = UsersForm()

    return render(request, 'shop/users.html',
                  {'users': users,
                   'form': form})

def delete_users(request, users_id):
    users = Users.objects.get(pk=users_id)
    if request.method == 'POST':
        users.delete()
        return redirect('users')
    else:
        return HttpResponse('Nonono!')

def order_list(request):
    orders = Orders.objects.all()


    return render(request, 'shop/order_list.html', {'orders': orders})

def edit_order(request, order_id):
    instance = get_object_or_404(Orders, id=order_id)
    if request.method == 'POST':
        form = EditForm(request.POST, instance=instance)
        if form.is_valid():
            new_status = form.cleaned_data['status']
            with transaction.atomic():
                order = form.save()
                if new_status == 'cancelled':
                    # Логика для возврата товаров на склад
                    for item in order.orderitem_set.all():
                        product = item.product
                        product.stock += item.quantity
                        product.save()
                elif new_status == 'active':
                    # Логика для возвращения товаров в заказ
                    for item in order.orderitem_set.all():
                        product = item.product
                        product.stock -= item.quantity
                        product.save()
                return redirect('orders')
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = EditForm(instance=instance)
        return render(request, 'shop/edit_order.html', {'form': form, 'instance_id': order_id})


def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = Products.objects.get(pk=product_id)
        quantity = int(request.POST.get('quantity'))
        if product.stock >= quantity:  # Проверка, достаточное ли количество товара на складе
            cart, created = Cart.objects.get_or_create()
            cart_item, created = CartItem.objects.get_or_create(product=product, cart=cart)

            if not created:
                # Если элемент корзины уже существует, увеличиваем количество товара
                cart_item.quantity += quantity
                cart_item.save()
            else:
                # Если элемент корзины только что был создан, задаем начальное количество товара
                cart_item.quantity = quantity
                cart_item.save()


            # Обновление остатка товара на складе
            product.stock -= quantity
            product.save()

            return redirect('cart_detail')
        else:
            # Обработка случая, когда товара недостаточно на складе
            # Здесь вы можете добавить сообщение об ошибке или выполнить другие действия
            return HttpResponse("Недостаточно товара на складе")
    else:
        # Обработка GET-запроса, например, отображение страницы продукта
        product = Products.objects.get(pk=product_id)
        return render(request, 'shop/products_list.html', {'product': product})


@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create()  # Получаем или создаем корзину для текущего пользователя
    cart_items = cart.cartitem_set.all()
    total = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.users = request.user
            order.save()

            for cart_item in cart_items:
                price_cart = cart_item.product.price * cart_item.quantity
                OrderItem.objects.create(order=order, product=cart_item.product, quantity=cart_item.quantity, price_cart=price_cart)
                # Уменьшаем количество товаров на складе при оформлении заказа

            cart.cartitem_set.all().delete()  # Очищаем корзину после оформления заказа

            # Перенаправляем пользователя на страницу с подробной информацией о заказе
            return render(request, 'shop/cart_detail.html', {'order': order})
    else:
        form = OrdersForm()

    return render(request, 'shop/cart_detail.html', {'cart_items': cart_items, 'total': total, 'form': form})

def clear_cart(request):
    cart, created = Cart.objects.get_or_create()
    cart_items = cart.cartitem_set.all()

    for cart_item in cart_items:
        product = cart_item.product
        product.stock += cart_item.quantity  # Возвращение количества товаров на склад
        product.save()

    cart.cartitem_set.all().delete()

    return redirect('cart_detail')
def return_product(request):
    return redirect('products_list')

def order_info(request, id):
    order = Orders.objects.get(pk=id)
    order_detail = OrderItem.objects.filter(order=id)


    return render(request, 'shop/order_info.html', {'order_detail': order_detail})

def delete_order(request, order_id):
    order = Orders.objects.get(pk=order_id)

    if request.method == 'POST':
        if order.status != 'cancelled':  # Проверяем статус заказа
            # Восстанавливаем количество товаров на складе при отмене заказа
            order_items = OrderItem.objects.filter(order=order)
            for order_item in order_items:
                product = order_item.product
                product.stock += order_item.quantity
                product.save()

        order.delete()  # Удаляем заказ

        return redirect('orders')
    else:
        return HttpResponse('Nonono!')

def delete_items(request, id):
    order_detail = OrderItem.objects.get(pk=id)

    if request.method == 'POST':
        # Увеличение количества товара на складе
        product = order_detail.product
        product.stock += order_detail.quantity  # увеличиваем количество товара на складе
        product.save()  # сохраняем изменения

        order_detail.delete()  # удаляем элемент заказа
        return redirect('orders')
    else:
        return HttpResponse('Nonono!')
@login_required
def my_orders(request):
    orders = Orders.objects.filter(users=request.user)

    return render(request, 'shop/my_orders.html', {'orders': orders})

@login_required
def cancel_order(request, order_id):
    try:
        order = Orders.objects.get(id=order_id)
        if order.status == 'active':
            order.status = 'cancelled'
            order.save()
            if order.status == 'cancelled':  # Проверяем статус заказа
                # Восстанавливаем количество товаров на складе при отмене заказа
                order_items = OrderItem.objects.filter(order=order)
                for order_item in order_items:
                    product = order_item.product
                    product.stock += order_item.quantity
                    product.save()
            # Дополнительные действия при отмене заказа, если необходимо
            return redirect('my_orders')  # Перенаправляем пользователя на страницу с подробной информацией о заказе
    except Orders.DoesNotExist:
        # Обработка случая, когда заказ с указанным ID не найден
        return HttpResponse("Order not found")
    return redirect('my_orders')
