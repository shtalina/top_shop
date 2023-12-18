from django import forms
from .models import Products, Orders, Users, Order_items
class EditForm(forms.Form):
    product_id = forms.IntegerField()
    count = forms.IntegerField()
    name = forms.CharField(max_length=20)
    customer = forms.CharField(max_length=255)
#    type = forms.CharField(max_length=255, choices=[('online', 'Online'), ('offline', 'Offline')])
#    status = forms.CharField(max_length=255, choices=[('active', 'Active'), ('completed', 'Completed'),
#                                                     ('cancelled', 'Cancelled')])
class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price','stock', 'image']

class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['name', 'customer', 'phone', 'type', 'status']

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'status']      
 
     