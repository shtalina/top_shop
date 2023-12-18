from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.products_list, name='products'),
    path('/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('orders', views.order_list, name='orders'),
    path('users', views.users, name='users'),
    #path('createProduct', views.createProduct, name='createProduct'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart_detail/', views.cart_detail, name='cart_detail'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
    #path('/createOrders/', views.createOrders, name='createOrders'),
    path('return_product/', views.return_product, name='return_product'),


]