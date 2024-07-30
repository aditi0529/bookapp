from django.db import models

# Create your models here.
class Book(models.Model):
    #id will be added by ORM
    title =models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    price = models.IntegerField()
    