from django import forms


class EditForm(forms.Form):
    product_id = forms.IntegerField()
    count = forms.IntegerField()
    name = forms.CharField(max_length=20)
    customer = forms.CharField(max_length=255)
#    type = forms.CharField(max_length=255, choices=[('online', 'Online'), ('offline', 'Offline')])
#    status = forms.CharField(max_length=255, choices=[('active', 'Active'), ('completed', 'Completed'),
 #                                                     ('cancelled', 'Cancelled')])
