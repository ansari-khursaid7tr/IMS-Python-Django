from django import forms
from home.models import Product, Dealer, Vendor, Company, Sell, Buy, Warehouse, Bank
import django_filters

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name','quantity','manufac','dealer','pricerange', 'ram', 'price', 'desc','photo', 'tprice')
        labels = {
            'name' : 'Product Name',
            'manufac' : 'Manufacturer',
            'pricerange' : 'Price Range',
            'ram' : 'RAM',
            'desc' : 'Specifications',
            'photo' : 'Product Image',
            'price' : 'Base Price',
            'tprice' : 'Total Price'
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['pricerange'].empty_label = "Select"
        self.fields['ram'].empty_label = "Select"
        self.fields['dealer'].empty_label = "Select"
        self.fields['manufac'].required = False
        self.fields['dealer'].required = False
        self.fields['desc'].required = False
        self.fields['photo'].required = False

class DealerForm(forms.ModelForm):
    class Meta:
        model = Dealer
        fields = ('name','email','address','city','contact', 'desc')
        labels = {
            'name' : 'Dealer Name',
            'email' : 'Email Address',
            'address' : 'Address',
            'city' : 'City',
            'desc' : 'Description'
        }

    def __init__(self, *args, **kwargs):
        super(DealerForm, self).__init__(*args, **kwargs)
        self.fields['desc'].required = False

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ('name','email','address','city','contact', 'desc')
        labels = {
            'name' : 'Vendor Name',
            'email' : 'Email Address',
            'address' : 'Address',
            'city' : 'City',
            'desc' : 'Description'
        }

    def __init__(self, *args, **kwargs):
        super(VendorForm, self).__init__(*args, **kwargs)
        self.fields['desc'].required = False

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name','address','city','contact')
        labels = {
            'name' : 'Company Name',
            'address' : 'Address',
            'city' : 'City',
        }

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)

class SellForm(forms.ModelForm):
    class Meta:
        model = Sell
        fields = ('name','email', 'address' ,'pname', 'quantity', 'contact', 'desc')
        labels = {
            'name' : 'Customer Name',
            'pname' : 'Product Name',
            'desc' : 'Description',
        }

    def __init__(self, *args, **kwargs):
        super(SellForm, self).__init__(*args, **kwargs)
        self.fields['desc'].required = False

class BuyForm(forms.ModelForm):
    class Meta:
        model = Buy
        fields = ('name','email', 'address' ,'pname', 'quantity', 'contact', 'desc')
        labels = {
            'name' : 'Name',
            'pname' : 'Product Name',
            'desc' : 'Description',
        }

    def __init__(self, *args, **kwargs):
        super(BuyForm, self).__init__(*args, **kwargs)
        self.fields['desc'].required = False

class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ('name', 'address' ,'city', 'status', 'contact', 'desc')
        labels = {
            'name' : 'Warehouse Name',
            'desc' : 'Description',
        }

    def __init__(self, *args, **kwargs):
        super(WarehouseForm, self).__init__(*args, **kwargs)
        self.fields['desc'].required = False
        self.fields['status'].empty_label = "Select"
    
class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ('name', 'accno' , 'address' ,'branch', 'status', 'contact')
        labels = {
            'name' : 'Bank Name',
            'accno' : 'Account Number',
        }

    def __init__(self, *args, **kwargs):
        super(BankForm, self).__init__(*args, **kwargs)
        self.fields['status'].empty_label = "Select"




      
