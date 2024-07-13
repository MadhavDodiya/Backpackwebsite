from django.db import models

# Create your models here.

class Information(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    comment=models.TextField()
    
    def __str__(self):
        return self.firstname

class Imageupload(models.Model):
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=20)
    image=models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.name

class Signup(models.Model):
    firstname=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.EmailField(max_length=254)
    
    def __str__(self):
        return self.firstname