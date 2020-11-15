from django import forms
from .models import Customer, Offer, Product


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('customer_name', 'customer_group', 'account_number', 'address', 'email', 'phone_number')


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ('code', 'description', 'discount')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('customer_name', 'product_name', 'price', 'stock', 'offer_code', 'order_time')