from django.db import models

# Create your models here.

class Information(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    comment=models.TextField()
    
    def __str__(self):
        return self.firstname
