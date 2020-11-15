from django.contrib import admin
from .models import Product, Offer, Customer


class CustomerList(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_group', 'phone_number')
    list_filter = ('customer_name', 'customer_group')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'order_time', 'price', 'stock', 'offer_code')
    list_filter = ('customer_name', 'order_time', 'product_name')
    search_fields = ('customer_name',)
    ordering = ['customer_name']


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'description')


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Customer, CustomerList)