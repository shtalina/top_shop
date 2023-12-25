from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.products_list, name='products'),
    path('/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('orders', views.order_list, name='orders'),
    path('my_orders/cancel/<int:order_id>/', views.cancel_order, name='cancel_order'),
    path('my_orders', views.my_orders, name='my_orders'),

    path('/orders/<int:order_id>', views.delete_order, name='delete_order'),
    path('/edit_order/<int:order_id>/', views.edit_order, name='edit_order'),
    path('users', views.users, name='users'),
    path('/delete_users/<int:users_id>', views.delete_users, name='delete_users'),
    #path('createProduct', views.createProduct, name='createProduct'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart_detail/', views.cart_detail, name='cart_detail'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
    #path('/createOrders/', views.createOrders, name='createOrders'),
    path('return_product/', views.return_product, name='return_product'),
    path('/order_info/<int:id>', views.order_info, name='order_info'),
    path('/delete_items/<int:id>', views.delete_items, name='delete_items'),




]