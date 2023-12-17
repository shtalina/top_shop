from django.contrib import admin
from .models import Products
from .models import CartItem
from .models import Cart

admin.site.register(Products)
admin.site.register(CartItem)
admin.site.register(Cart)
# Register your models here.
