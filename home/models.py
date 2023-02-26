from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from nectar import settings
from nectar.manager import UserManager


def nameFile(instance, filename):
    return '/'.join(['images', str(instance.email), filename])

def productImageFile(instance, filename):
    return '/'.join(['products', str(instance.id), filename])

class UserModel(AbstractUser):
    first_name = models.CharField(max_length=64,null= False)
    last_name = models.CharField(max_length=64, null= True,blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128,null=False)
    profile_image = models.ImageField(upload_to=nameFile, blank=True, null=True)
    username = None

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    

class ProductModel(models.Model):
    product_name = models.CharField(max_length=64,null= False)
    product_image = models.ImageField(upload_to=productImageFile, blank=True, null=True)
    product_dic = models.CharField(max_length=64,null= True,blank=True)
    product_price = models.FloatField(max_length=5,null= False,blank=False)
    product_discount_price = models.FloatField(max_length=5,null=True,blank=True)
    product_type = models.CharField(max_length=64,null=False,blank=False)

    def __str__(self):
        return self.product_name
    


    
