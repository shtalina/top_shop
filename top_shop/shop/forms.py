from django import forms
from .models import Products, Orders, Users
class EditForm(forms.ModelForm):
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
        fields = ['customer', 'phone', 'user_id', 'type']

        widgets = {
            'status': forms.HiddenInput(),  # Делаем поле статуса скрытым на форме
        }

        def __init__(self, *args, **kwargs):
            super(OrdersForm, self).__init__(*args, **kwargs)
            self.fields['status'].initial = 'active'  # Устанавливаем значение "active" по умолчанию
class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name']



