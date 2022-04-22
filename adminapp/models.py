from django.db import models


# Create your models here.
class Customer(models.Model):
    client_name = models.CharField(max_length=30) 
    gst_number = models.CharField(max_length=30) 
    client_id = models.CharField(max_length=30) 
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=30)
    address = models.CharField(max_length=30)

class Product(models.Model):
    food_name = models.CharField(max_length=50)
    catagory = models.CharField(max_length=50)
    priceper_head = models.IntegerField()
    priceper_kg = models.IntegerField()
    food_deatails = models.CharField(max_length=50)

    class Meta:
        db_table = 'Product'