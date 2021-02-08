from django.shortcuts import render,redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.db.models import Sum
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .filters import FilterServeds
FilterServed=[]
from .forms import RegisterForm,newFORM,reportsForm
from django.forms.models import modelformset_factory
from django.forms import modelform_factory
from .models import *
from .decorators import unauthenticated_user, allowed_users,admin_only
from farm.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@admin_only
def index(request):

    xog =Product.objects.all().values('id','name','amount','product_pic','User__gobolka__name','User__magaalada__name','User__Number','User__user_pic')
  
    context = {'xog':xog,}
    return render(request, "index.html",context)

def index2(request):

    xog =Product.objects.all().values('id','name','amount','product_pic','User__gobolka__name','User__magaalada__name','User__Number')
    
    context = {'xog':xog,}
    return render(request, "buyers.html",context)


def singup(request):
   

    formset= RegisterForm()
    if request.method == 'POST':
        formset = RegisterForm(request.POST)
        if formset.is_valid():
            user=formset.save(commit=False)
            
            group = formset.cleaned_data['group']        
            group.user_set.add(user)
            password = formset.cleaned_data['password']

            #  Use set_password here
            user.set_password(password)
            user.save()
            return redirect('login')
        

    context = {'formset':formset}
    return render(request, "singub.html",context)

def product(request,pk):
    xog =Product.objects.filter(id=pk).values('name','amount','unit','User__name','product_pic','User__gobolka__name','User__magaalada__name','User__Number')
    
    context = {'xog':xog,}
    return render(request, "product.html",context)

def newprices(request):

    xog =pricess.objects.all()
    
    context = {'xog':xog,}
    return render(request, "prices.html",context)

def Maps(request):

    return render(request, "maps.html")
def cars(request):
    xog =Cars.objects.all().values('car_type','owner','info','number','product_pic')
    
    context = {'xog':xog,}
    

    return render(request, "cars.html",context)
def reports(request):
    serveds = Reports.objects.all().values('Product__name','amount','price','total','Date')


    myFilter = FilterServeds(request.GET, queryset=serveds)
    serveds = myFilter.qs 


    context = {'serveds':serveds,'myFilter':myFilter}
    return render(request, "reports.html",context)

def addnew(request):
    formt= newFORM()
    if request.method == 'POST':
        formt = newFORM(request.POST)
        if formt.is_valid():
            commentss=formt.save(commit=False)
            commentss.User = request.user
            commentss.save()
            
            return redirect('home')
    
    context = {'formt':formt}
    return render(request, 'new.html',context)

def newReports(request):
    formt= reportsForm()
    if request.method == 'POST':
        formt = reportsForm(request.POST)
        if formt.is_valid():
            commentss=formt.save(commit=False)
            commentss.total = commentss.amount * commentss.price
            commentss.save()
            return redirect('home')
    
    context = {'formt':formt}
    return render(request, 'newreport.html',context) 

def About(request):

    
    return render(request, "about.html",)

def App(request):

    
    return render(request, "app.html",)