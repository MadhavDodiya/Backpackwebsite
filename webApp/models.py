from django.db import models

# Create your models here.

class Information(models.Model): #cotact page table
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    comment=models.TextField()
    
    def __str__(self):
        return self.firstname

class Imageupload(models.Model): #shop page image upload table
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=20)
    image=models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.name

class Signup(models.Model): #signup page table
    firstname=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.EmailField(max_length=254)
    
    def __str__(self):
        return self.firstname
    
class cartproduct(models.Model): #cartitem added in cartpage
    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='images')
    price=models.CharField(max_length=20)
    quantity=models.CharField(max_length=20,default=1)
    subtotal=models.CharField(max_length=20,default=50)
    
    def __str__(self):
        return self.name