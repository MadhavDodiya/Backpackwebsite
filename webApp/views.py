from django.shortcuts import render

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