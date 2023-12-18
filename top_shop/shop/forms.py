from django import forms
from .models import Products, Orders, Users
class EditForm(forms.Form):
    class Meta:
        model = Orders
        fields = ['customer', 'phone', 'user_id', 'type', 'status']
class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price','stock', 'image']

class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['customer', 'phone', 'user_id', 'type', 'status']

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name']