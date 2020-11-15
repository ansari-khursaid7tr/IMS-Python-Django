from django.contrib import admin
from home.models import Connect
from home.models import Product, Dealer, Vendor, Company, PriceRange, Ram, Status, Sell, Buy, Warehouse, Bank

# Register your models here.
admin.site.register(Connect)
admin.site.register(Product)
admin.site.register(Dealer)
admin.site.register(Vendor)
admin.site.register(Company)
admin.site.register(PriceRange)
admin.site.register(Ram)
admin.site.register(Sell)
admin.site.register(Buy)
admin.site.register(Status)
admin.site.register(Warehouse)
admin.site.register(Bank)
