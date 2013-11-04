from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=20)
    publisher = models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    price = models.FloatField()
    seller_id = models.CharField(max_length=20)
    seller_contact = models.CharField(max_length=20)
