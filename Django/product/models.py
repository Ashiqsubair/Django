from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=225)
    price=models.FloatField()
    stock=models.IntegerField()
    image=models.CharField(max_length=2550,blank=True)
class Offers(models.Model):
    code=models.CharField(max_length=20)
    name=models.CharField(max_length=225)
    