from django.contrib import admin
from .models import Products
from .models import CartItem
from .models import Cart
from .models import Orders

admin.site.register(Products)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Orders)
# Register your models here.
