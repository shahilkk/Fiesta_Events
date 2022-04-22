
from django.db import models


# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=30) 
    client_gst_number = models.CharField(max_length=30) 
    client_id = models.CharField(max_length=30) 
    client_phone = models.CharField(max_length=30)
    client_email = models.CharField(max_length=30)
    client_state = models.CharField(max_length=30)
    client_district = models.CharField(max_length=30)
    client_zipcode = models.CharField(max_length=30)
    client_address = models.CharField(max_length=30)

    class Meta:
        db_table = 'client'

class Product(models.Model):
    food_name = models.CharField(max_length=50)
    catagory = models.CharField(max_length=50)
    priceper_head = models.IntegerField()
    priceper_kg = models.IntegerField()
    food_deatails = models.CharField(max_length=50)

    class Meta:
        db_table = 'product'


class Employee(models.Model):
    employee_name = models.CharField(max_length=50)
    employee_username = models.CharField(max_length=50)
    employee_password = models.CharField(max_length=50)
    employee_phone = models.CharField(max_length=30)
    employee_email = models.CharField(max_length=30)
    employee_state = models.CharField(max_length=30)
    employee_district = models.CharField(max_length=30)
    employee_zipcode = models.CharField(max_length=30)
    employee_address = models.CharField(max_length=30)
    employee_status = models.CharField(max_length=30)

    class Meta:
        db_table = 'employee'


class AddBank(models.Model):
    bank_name = models.CharField(max_length=50)
    bank_holdername = models.CharField(max_length=50)
    bank_ifsc = models.CharField(max_length=30)
    bank_accountname = models.CharField(max_length=30)    
    bank_balance = models.IntegerField()     

    class Meta:
        db_table = 'addBank'



