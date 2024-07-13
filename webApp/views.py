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

def logincheck(request):
    a = request.POST.get('name1')
    b = request.POST.get('pass1')
    
    obj=Signup.objects.all()
    login = False
    
    for i in obj:
        if ((i.firstname== a) or (i.email== a))   and i.password == b:
            login=True
            messages.success(request, "Login successfully")
            return redirect('/index')
                                                                                                                                                        
        if login == False:
            messages.warning(request, "Login invalid!!")
            return redirect('/account')
            
def cartitem(request):
    a=request.POST.get('name')
    b=request.POST.get('img')
    c=request.POST.get('prc')
    
    obj=cartproduct(name=a,img=b,price=c)
    obj.save()
    
    obj1=cartproduct.objects.all()
    
    return render(request,'cart.html',{'data':obj1})