from django.db import models
import datetime

# Create your models here.
class Connect(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    desc = models.TextField()
    
    def __str__(self):
        return self.name 

class PriceRange(models.Model):
    pricerange = models.CharField(max_length=50)

    def __str__(self):
        return self.pricerange

class Ram(models.Model):
    ram = models.CharField(max_length=50)

    def __str__(self):
        return self.ram

class Dealer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    desc = models.TextField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.BigIntegerField()

    def __str__(self):
        return self.name 
    

class Product(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    manufac = models.CharField(max_length=50)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    price = models.IntegerField()
    pricerange = models.ForeignKey(PriceRange, on_delete = models.CASCADE)
    ram = models.ForeignKey(Ram, on_delete = models.CASCADE)
    desc = models.TextField()
    tprice = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.name 
    
class Vendor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    desc = models.TextField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.BigIntegerField()

    def __str__(self):
        return self.name 
    
class Company(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.BigIntegerField()

    def __str__(self):
        return self.name 

class Sell(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    pname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contact = models.IntegerField() 
    address = models.CharField(max_length=50)  
    desc = models.TextField()


    def __str__(self):
        return self.name 

class Buy(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    pname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contact = models.IntegerField()   
    address = models.CharField(max_length=50) 
    desc = models.TextField()


    def __str__(self):
        return self.name 

class Status(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status

class Warehouse(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.IntegerField()
    status = models.ForeignKey(Status, on_delete = models.CASCADE)
    desc = models.TextField()

    def __str__(self):
        return self.name 

class Bank(models.Model):
    name = models.CharField(max_length=50)
    accno = models.IntegerField()
    address = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    contact = models.IntegerField()
    status = models.ForeignKey(Status, on_delete = models.CASCADE)

    def __str__(self):
        return self.name 



