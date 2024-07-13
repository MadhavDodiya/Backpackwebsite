from django.shortcuts import redirect, render
from django.contrib import messages

from webApp.models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def shop(request):
    obj=Imageupload.objects.all()
    return render(request, 'shop.html',{'data':obj})

def blog(request):
    return render(request, 'blog.html')

def account(request):
    return render(request, 'myaccount.html')

def contact(request):
    return render(request, 'contact.html')

def cart(request):
    return render(request, 'cart.html')

def signup(request):
    return render(request, 'signup.html')

def data(request):
    a = request.POST.get('fname')
    b = request.POST.get('lname')
    c = request.POST.get('email')
    d = request.POST.get('comment')
    
    obj=Information(firstname=a,lastname=b,email=c,comment=d)
    obj.save()
    messages.success(request, "Your profile was updated.")
    return redirect("/contact")

def register(request):
    a = request.POST.get('name1')
    b = request.POST.get('pass1')
    c = request.POST.get('email1')
    
    obj = Signup(firstname=a,password=b,email=c)
    obj.save()
    messages.success(request, "Register successfully")
    return redirect('/account')