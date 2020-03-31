from django import forms
from django.core import validators
from sales_orders_app.models import Customer, Order, Sale
from django.contrib.auth.models import User

class CustomerForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class CustomerProfileInfoForm(forms.ModelForm):
     class Meta:
         model = Customer
         fields = ('phone', 'info', 'portfolio_site')


class OrderForm(forms.ModelForm):
    class Meta:
        print(' Meta in OrderForm')
        model = Order
        fields = ['customer', 'vendor_code', 'color', 'size']
        #fields = '__all__'

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'
