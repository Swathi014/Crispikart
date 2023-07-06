from django.db import models

# Create your models here.

class PublicInformation(models.Model):

    user_id = models.IntegerField()
    restorent_name = models.CharField(max_length=255)
    images = models.CharField(max_length=255)
    address = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=300)
    working_time = models.IntegerField()
    order_option = models.IntegerField()
    contact_no = models.CharField(max_length=200)
    whatsapp_no = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)

class PrivateInformation(models.Model):
    user_id = models.IntegerField()
    profile = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=200)
    whatsapp_no = models.CharField(max_length=200)
    email = models.CharField(max_length=255)
    established_year = models.IntegerField()
    no_of_employees = models.IntegerField()
    manager_name = models.CharField(max_length=250)
    manager_contact_no = models.CharField(max_length=200)
    payment_options = models.CharField(max_length=200)
    settlement_type = models.IntegerField()
    settlement_mode = models.IntegerField()

class WorkingTime(models.Model):
    name = models.CharField(255)
    time = models.TimeField(auto_now=False, auto_now_add=False)

class PaymentOption(models.Model):
    name = models.CharField(max_length=255)

class OrderOption(models.Model):
    name = models.CharField(255)            

