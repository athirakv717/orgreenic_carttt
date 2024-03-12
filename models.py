from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class  Categories(models.Model):
    category_name=models.CharField(max_length=100,unique=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.category_name



class Products(models.Model):
    product_name=models.CharField(max_length=100,unique=True)
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    price=models.PositiveIntegerField()
    image=models.ImageField(upload_to="images",null=True)
    description=models.CharField(max_length=250,null=True)

    def __str__(self):
        return self.product_name        
    

class UserRegister(AbstractUser):
     phonenumber=models.CharField(max_length=20)   
     usertype=models.CharField(max_length=200)     

     def __str__(self):
        return self.username


class Cart(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE) 
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE) 
    order_date=models.DateTimeField(auto_now_add=True,null=True)
    quantity=models.PositiveIntegerField(default=1)
    options=(
        ('in-cart','in-cart'),
        ('order-placed','order-placed'),
        ('cancelled','cancelled')
    )
    status=models.CharField(max_length=100,choices=options,default="in-cart")