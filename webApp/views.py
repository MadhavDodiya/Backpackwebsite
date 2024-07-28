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
    obj1=cartproduct.objects.all()
    newobj=list(obj1)
    total=0
    for i in newobj:
        total=total+int(i.subtotal)
    length=len(obj1)
    return render(request, 'cart.html',{'data':obj1,"length":length,'totalAmount':total})

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
        if ((i.firstname== a) or (i.email== a)  and i.password == b):
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
    
    obj=cartproduct(name=a, image=b,price=c)
    obj.save()
    messages.success(request, "Item Add to Cart")
    return redirect("/shop")

def deletecart(request):
    a=request.POST.get('cartproduct')
    
    obj=cartproduct.objects.get(id=a)
    obj.delete()
    messages.success(request, "Item Delete!!")
    return redirect('/cart')

def increment(request):
    a=request.POST.get('id')
    
    obj=cartproduct.objects.get(id=a)
    obj.quantity=int(obj.quantity)+1
    obj.subtotal=int(obj.subtotal)+50
    obj.save()
    
    return redirect('/cart')

def decriment(request):
    a=request.POST.get('id')
    
    obj=cartproduct.objects.get(id=a)
    obj.quantity=int(obj.quantity)-1
    obj.subtotal=int(obj.subtotal)-50
    obj.save()
    
    if obj.quantity == 0:
        obj.delete()
    return redirect('/cart')