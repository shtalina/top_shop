from django.contrib import admin
from .models import Products
from .models import CartItem
from .models import Cart
from .models import Orders, Users, Order_items

admin.site.register(Products)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Orders)
admin.site.register(Users)
admin.site.register(Order_items)
# Register your models here.
