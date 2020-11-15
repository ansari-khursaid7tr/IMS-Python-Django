from home.models import Product, Dealer, Vendor, Sell, Buy
import django_filters
from django import forms

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['pricerange', 'ram']

class DealerFilter(django_filters.FilterSet):
    class Meta:
        model = Dealer
        fields = ['city']

class VendorFilter(django_filters.FilterSet):
    class Meta:
        model = Vendor
        fields = ['city']
    
    
    
