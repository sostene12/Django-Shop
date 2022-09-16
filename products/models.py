from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=255,null=False)
    price=models.FloatField(null=False)
    stock=models.IntegerField(null=True)
    image_url=models.CharField(max_length=2083)

class Offer(models.Model):
    code = models.CharField(null=True,max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField(null=False)