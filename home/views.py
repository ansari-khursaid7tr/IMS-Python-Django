from django.shortcuts import render, HttpResponse, redirect
from home.models import Connect, Product, Dealer, Vendor, Company, Sell, Buy, Warehouse, Bank
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, update_session_auth_hash
import datetime
from home.forms import ProductForm, DealerForm, VendorForm, CompanyForm, SellForm, BuyForm, WarehouseForm, BankForm
from django.contrib.auth.forms import PasswordChangeForm
from home.filters import ProductFilter, DealerFilter, VendorFilter

# Create your views here.
def index(request):
    companys = Company.objects.all()
    return render(request, 'index.html', {'companys' : companys})
    # return HttpResponse("This is my homepage")

def login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('pswd')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            auth.login(request, user)
            return redirect('/dashboarddata')
        else:
            # No backend authenticated the credentials
            messages.info(request, 'Invalid Username/Password')
            return render(request, 'login.html')
    
    return render(request, 'login.html')
    #return HttpResponse("This is my About page")

def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        username = request.POST['username']
        email = request.POST['email']
        pswd1 = request.POST['pswd1']
        pswd2 = request.POST['pswd2']

        if fname and username and email and pswd1 and pswd2 is not None:
            if pswd1 == pswd2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username already exits')
                elif User.objects.filter(email=email).exists():
                    messages.error(request,'Email already exists')
                else: 
                    user = User.objects.create_user(username=username, password=pswd1, email=email)
                    user.fname =fname
                    user.save()
                    return redirect('/dashboarddata')
            else:
                messages.info(request,'Password not matching')
        else:
            messages.info(request,'Empty Fields Detected')
    return render(request, 'register.html')
    #return HttpResponse("This is my Services page")

def dashboard(request):
    companys = Company.objects.all()
    return render(request, 'dashboard.html', {'companys' : companys})

def dashboarddata(request):
    contents = Product.objects.all()
    companys = Company.objects.all()
    return render(request, 'dashboarddata.html', {'contents' : contents, 'companys' : companys})

def reports(request):
    return render(request, 'reports.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Connect(name= name, email=email, desc= desc)
        contact.save()
        messages.success(request, 'Successfully Submitted!')
        
    return render(request, 'contact.html')
    #return HttpResponse("This is my Contact page")

#def forgotpassword(request):
    #return render(request, 'forgot-password.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def addunit(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ProductForm()
        else:
            product = Product.objects.get(pk=id)
            form = ProductForm(instance=product)
        return render(request, 'addunit.html', {'form' : form})
    
    else:
        if id==0:
            form = ProductForm(request.POST)
        else:
            product = Product.objects.get(pk=id)
            form = ProductForm(request.POST, instance=product)
        if form.is_valid():
                form.save()
        return redirect('/products')

def products(request):
        contents = Product.objects.all()

        myfilter = ProductFilter(request.GET, queryset=contents)
        contents = myfilter.qs

        return render(request, 'products.html', {'contents' : contents, 'myfilter' : myfilter})
    
def productdetails(request):
    contents = Product.objects.all()
    return render(request, 'productdetails.html', {'contents' : contents})
    
def delete(request, id):
    contents = Product.objects.get(pk=id)
    contents.delete()
    return redirect("/products")

def deletevendor(request, id):
    contents = Vendor.objects.get(pk=id)
    contents.delete()
    return redirect("/vendors")

def deletedealer(request, id):
    contents = Dealer.objects.get(pk=id)
    contents.delete()
    return redirect("/dealers")

def dealers(request):
    contents = Dealer.objects.all()

    myfilter = DealerFilter(request.GET, queryset=contents)
    contents = myfilter.qs

    return render(request, 'dealers.html', {'contents' : contents, 'myfilter' : myfilter})

def adddealer(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = DealerForm()
        else:
            deals = Dealer.objects.get(pk=id)
            form = DealerForm(instance=deals)
        return render(request, 'adddealer.html', {'form' : form})
    
    else:
        if id==0:
            form = DealerForm(request.POST)
        else:
            deals = Dealer.objects.get(pk=id)
            form = DealerForm(request.POST, instance=deals)
        if form.is_valid():
                form.save()
        return redirect('/dealers')

def addvendor(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = VendorForm()
        else:
            venders = Vendor.objects.get(pk=id)
            form = VendorForm(instance=venders)
        return render(request, 'addvendor.html', {'form' : form})
    
    else:
        if id==0:
            form = VendorForm(request.POST)
        else:
            venders = Vendor.objects.get(pk=id)
            form = VendorForm(request.POST, instance=venders)
        if form.is_valid():
                form.save()
        return redirect('/vendors')

def vendors(request):
    contents = Vendor.objects.all()

    myfilter = VendorFilter(request.GET, queryset=contents)
    contents = myfilter.qs

    return render(request, 'vendors.html', {'contents' : contents, 'myfilter' : myfilter})

def editcompany(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = CompanyForm()
        else:
            venders = Company.objects.get(pk=id)
            form = CompanyForm(instance=venders)
        return render(request, 'editcompany.html', {'form' : form})
    
    else:
        if id==0:
            form = CompanyForm(request.POST)
        else:
            venders = Company.objects.get(pk=id)
            form = CompanyForm(request.POST, instance=venders)
        if form.is_valid():
                form.save()
        return redirect('/company')

def company(request):
    companys = Company.objects.all()
    return render(request, 'company.html', {'companys' : companys})

def addsell(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = SellForm()
        else:
            product = Sell.objects.get(pk=id)
            form = SellForm(instance=product)
        return render(request, 'addsell.html', {'form' : form})
    
    else:
        if id==0:
            form = SellForm(request.POST)
        else:
            product = Sell.objects.get(pk=id)
            form = SellForm(request.POST, instance=product)
        if form.is_valid():
                form.save()
        return redirect('/sales')

def sales(request):
        contents = Sell.objects.all()
        return render(request, 'sales.html', {'contents' : contents})

def deletesell(request, id):
    contents = Sell.objects.get(pk=id)
    contents.delete()
    return redirect("/sales")

def addbuy(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = BuyForm()
        else:
            product = Buy.objects.get(pk=id)
            form = BuyForm(instance=product)
        return render(request, 'addbuy.html', {'form' : form})
    
    else:
        if id==0:
            form = BuyForm(request.POST)
        else:
            product = Buy.objects.get(pk=id)
            form = BuyForm(request.POST, instance=product)
        if form.is_valid():
                form.save()
        return redirect('/buy')

def buy(request):
        contents = Buy.objects.all()
        return render(request, 'buy.html', {'contents' : contents})

def deletebuy(request, id):
    contents = Buy.objects.get(pk=id)
    contents.delete()
    return redirect("/buy")

def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data= request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/dashboarddata')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'changepassword.html', {'form' : form})

def addwarehouse(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = WarehouseForm()
        else:
            product = Warehouse.objects.get(pk=id)
            form = WarehouseForm(instance=product)
        return render(request, 'addwarehouse.html', {'form' : form})
    
    else:
        if id==0:
            form = WarehouseForm(request.POST)
        else:
            product = Warehouse.objects.get(pk=id)
            form = WarehouseForm(request.POST, instance=product)
        if form.is_valid():
                form.save()
        return redirect('/warehouse')

def warehouse(request):
        contents = Warehouse.objects.all()
        return render(request, 'warehouse.html', {'contents' : contents})

def deletewarehouse(request, id):
    contents = Warehouse.objects.get(pk=id)
    contents.delete()
    return redirect("/warehouse")

def addbank(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = BankForm()
        else:
            product = Bank.objects.get(pk=id)
            form = BankForm(instance=product)
        return render(request, 'addbank.html', {'form' : form})
    
    else:
        if id==0:
            form = BankForm(request.POST)
        else:
            product = Bank.objects.get(pk=id)
            form = BankForm(request.POST, instance=product)
        if form.is_valid():
                form.save()
        return redirect('/bank')

def bank(request):
        contents = Bank.objects.all()
        return render(request, 'bank.html', {'contents' : contents})

def deletebank(request, id):
    contents = Bank.objects.get(pk=id)
    contents.delete()
    return redirect("/bank")

def settings(request):
    return render(request, 'settings.html')

def about(request):
    return render(request, 'about.html')
    