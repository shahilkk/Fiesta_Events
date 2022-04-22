from django.shortcuts import render,redirect

from .models import Product

# Create your views here.


def master(req):
    return render(req,'master.html')

def index(req):
    context={"is_index":True}
    return render(req,'index.html',context)  

def customer(req):
    context={"is_customer":True}
    return render(req,'customer.html',context)


def addcustomer(req):
    context={"is_customer":True}
    return render(req,'addcustomer.html',context) 

def editcustomer(req):
    context={"is_customer":True}
    return render(req,'editcustomer.html',context)   



def viewcustomer(req):
    context={"is_customer":True}
    return render(req,'viewcustomer.html',context)         


def marketingstaff(req):
    context={"is_marketingstaff":True}
    return render(req,'marketingstaff.html',context)      


def addmstaff(req):
    context={"is_marketingstaff":True}
    return render(req,'addmstaff.html',context)



def editstaff(req):
    context={"is_marketingstaff":True}
    return render(req,'editstaff.html',context)    



def Estimate(req):
    context={"is_estimate":True}
    return render(req,'Estimate.html',context)   


def addestimate(req):
    context={"is_estimate":True}
    return render(req,'addestimate.html',context) 




def editestimate(req):
    context={"is_estimate":True}
    return render(req,'editestimate.html',context)   


def viewestimate(req):
    context={"is_estimate":True}
    return render(req,'viewestimate.html',context) 



def invoicegrid(req):
    context={"is_invoice":True}
    return render(req,'invoicegrid.html',context)        
  

def invoiceList(req):
    context={"is_invoice":True}
    return render(req,'invoiceList.html',context) 


def addinvoice(req):
    context={"is_invoice":True}
    return render(req,'addinvoice.html',context)


def invoicedetails(req):
    context={"is_invoice":True}
    return render(req,'invoicedetails.html',context) 


def editinvoice(req):
    context={"is_invoice":True}
    return render(req,'editinvoice.html',context) 


def bank(req):
    context={"is_bank":True}
    return render(req,'addbank.html',context) 
    

def products(request):
   
    # msg = ''
    if request.method == 'POST':
        food_name = request.POST['food_name']
        catagory = request.POST['catagory']
        priceper_head = request.POST['priceper_head']
        priceper_kg = request.POST['priceper_kg']
        food_deatails = request.POST['food_deatails']
        food_exist = Product(food_name = food_name,catagory = catagory,priceper_head = priceper_head,priceper_kg = priceper_kg,food_deatails = food_deatails)
        food_exist.save()
        print(food_name)
        return redirect('/admin/products')
        # msg = " product added"

    view_product = Product.objects.all()    
    context={
        "is_product":True,
        'view_product': view_product
    }
    return render(request,'products.html',context) 


     


def payment(req):
    context={"is_payment":True}
    return render(req,'payment.html',context)  


def addpayment(req):
    context={"is_payment":True}
    return render(req,'addpayment.html',context)   



def expenses(req):
    context={"is_expenses":True}
    return render(req,'expenses.html',context)          



def addexpenses(req):
    context={"is_expenses":True}
    return render(req,'addexpence.html',context)



def profit(req):
    context={"is_profit":True}
    return render(req,'profit.html',context)          



def addprofit(req):
    context={"is_profit":True}
    return render(req,'addprofit.html',context)




def filter(req):
    context={"is_filter":True}
    return render(req,'filter.html',context) 
      




   
def demo(request):
    return render(request,'demo/index.html')

      
