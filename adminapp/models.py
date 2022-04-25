
from xmlrpc.client import Boolean
from django.db import models


# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=30) 
    client_gst_number = models.CharField(max_length=30) 
    client_id = models.CharField(max_length=30,default=0) 
    client_phone = models.CharField(max_length=30)
    client_email = models.CharField(max_length=30)
    client_state = models.CharField(max_length=30)
    client_district = models.CharField(max_length=30)
    client_zipcode = models.CharField(max_length=30)
    client_address = models.CharField(max_length=60)
    client_whsatpp = models.CharField(max_length=60)
    client_contact_type = models.CharField(max_length=40,default="")
    client_status = models.CharField(max_length=30 ,default="Active")
    client_bankholder = models.CharField(max_length=60,default="")
    client_bankname = models.CharField(max_length=60,default="")
    client_ifsc = models.CharField(max_length=60,default="")
    client_actnnumber = models.CharField(max_length=60,default="")
    class Meta:
        db_table = 'client'
    def __str__(self):
        return self.client_name 


class Product(models.Model):
    food_name = models.CharField(max_length=50)
    catagory = models.CharField(max_length=50)
    priceper_head = models.IntegerField()
    priceper_kg = models.IntegerField()
    food_deatails = models.CharField(max_length=50)
    food_status = models.BooleanField(default=True)

    class Meta:
        db_table = 'product'
    def __str__(self):
        return self.food_name    


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
    def __str__(self):
        return self.employee_name

class AddBank(models.Model):
    bank_name = models.CharField(max_length=50)
    bank_holdername = models.CharField(max_length=50)
    bank_ifsc = models.CharField(max_length=30)
    bank_accountname = models.CharField(max_length=30) 
    bank_branch = models.CharField(max_length=30)    
    bank_balance = models.IntegerField()     

    class Meta:
        db_table = 'addbank'
        
    def __str__(self):
        return self.bank_name    



