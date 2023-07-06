from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=200)

class Category(models.Model):
    group_id = models.IntegerField()
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/categories')    

class FoodItems(models.Model):
    group_ids = models.IntegerField()
    category_ids = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.CharField(max_length=300)
    quantity = models.FloatField()
    price = models.FloatField()
    availability = models.IntegerField()
    quantity = models.FloatField()