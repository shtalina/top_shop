from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Products_list, name='products'),
    path('orders', views.Order_list, name='orders'),
    path('orders/<int:order_id>', views.Order_items, name='info')

]