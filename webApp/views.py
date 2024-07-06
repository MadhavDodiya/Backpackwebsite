from django.shortcuts import redirect, render
from django.contrib import messages

from webApp.models import Information

# Create your views here.

def index(request):
    return render(request, 'index.html')

def shop(request):
    return render(request, 'shop.html')

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
    