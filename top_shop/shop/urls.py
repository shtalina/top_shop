from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.products_list, name='products'),
    path('orders', views.order_list, name='orders'),
    path('cart', views.cart, name='cart'),
    path('users', views.users, name='users'),
    path('orders/<int:order_id>', views.order_info, name='info')

]