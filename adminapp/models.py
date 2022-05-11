
from http import client
from unicodedata import category
from xmlrpc.client import Boolean
from django.db import models
# from datetime import date
import datetime

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
    client_address = models.CharField(max_length=60000)
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
    food_deatails = models.CharField(max_length=500000)
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
    employee_address = models.CharField(max_length=300000)
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


class Estimates(models.Model):
    clientd = models.ForeignKey(Client,on_delete=models.CASCADE )
    est_fromdate = models.CharField(max_length=50)
    est_todate = models.CharField(max_length=50)
    est_balance = models.IntegerField(default=0)
    est_status = models.CharField(max_length=50 , default='Pending' )
    est_active = models.BooleanField(default=True)
    class Meta:
        db_table = 'estimates'

     





class Category(models.Model):
    category = models.CharField(max_length=50)


class EstimateProduct(models.Model):
    est_category = models.CharField(max_length=50)
    est_amount = models.IntegerField()
    est_qty = models.CharField(max_length=50)
    est_price = models.IntegerField()
    productid = models.ForeignKey(Product,on_delete=models.CASCADE )
    estimateid = models.ForeignKey(Estimates,on_delete=models.CASCADE  )
  


class PaymentDetails(models.Model):
    clientid = models.ForeignKey(Client,on_delete=models.CASCADE )
    bankid = models.ForeignKey(AddBank,on_delete=models.CASCADE )
    estimateId = models.ForeignKey(Estimates,on_delete=models.CASCADE )
    paymentdate = models.CharField(max_length=50)
    clientbank = models.CharField(max_length=50)
    paymentamount = models.IntegerField()
 

class Expences(models.Model):
    clientid = models.ForeignKey(Client,on_delete=models.CASCADE )
    expencescategory = models.CharField(max_length=50)
    expencesnote = models.CharField(max_length=30000)
    expencesdate = models.DateField(default=datetime.date.today)
    expencesasamount = models.IntegerField(default = 0)
    expencestatus = models.CharField(max_length=50)



class Terms(models.Model):
    estimateid = models.ForeignKey(Estimates,on_delete=models.CASCADE )
    term = models.CharField(max_length=5000)
    note = models.CharField(max_length=3000)



class Income(models.Model):
    date = models.DateField(default=datetime.date.today)
    incomestatus = models.CharField(max_length=3000)
    incomeamount = models.IntegerField(default = 0)
    estimateId = models.ForeignKey(Estimates,on_delete=models.CASCADE )


class Preview(models.Model):
    estimateId = models.ForeignKey(Estimates,on_delete=models.CASCADE )
    discount = models.IntegerField(default = 0)
    prviewnumber = models.CharField(max_length=3000,default="")

    