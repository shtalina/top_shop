from django.contrib import admin
from .models import Products
from .models import CartItem
from .models import Cart
from .models import Orders, Order_items, Users

admin.site.register(Products)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Orders)
admin.site.register(Order_items)
admin.site.register(Users)
# Register your models here.
