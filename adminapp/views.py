
from django.shortcuts import render , redirect
from . models import Employee,Product,AddBank


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



def viewcustomer(requsest,id):
    print(id)
    details = Employee.objects.get(id=id)
    context={
        'details':details
    }
    return render(requsest,'viewcustomer.html',context)         


def marketingstaff(req):
    employeelist=Employee.objects.all()
    context={
    "is_marketingstaff":True,
    "employeelist":employeelist
    }
    return render(req,'marketingstaff.html',context)      


def addmstaff(request):
    context={"is_marketingstaff":True}
    if request.method=='POST':
        employee_name=request.POST['employee_name']
        employee_username=request.POST['employee_username']
        employee_password=request.POST['employee_password']
        employee_phone=request.POST['employee_phone']
        employee_email=request.POST['employee_email']
        employee_state=request.POST['employee_state']
        employee_district=request.POST['employee_district']
        employee_zipcode=request.POST['employee_zipcode']
        employee_address=request.POST['employee_address']
        print(employee_name)
        emplyoeedetails=Employee(employee_name=employee_name, employee_username=employee_username, employee_password=employee_password, employee_phone=employee_phone, employee_email=employee_email, employee_state=employee_state, employee_district=employee_district, employee_zipcode=employee_zipcode, employee_address=employee_address, employee_status='Active')
        emplyoeedetails.save()
        return redirect('/admin/marketingstaff')
        
    return render(request,'addmstaff.html',context)



def editstaff(request,staff_id):
    print(staff_id)
    if request.method=='POST':
        employee_name=request.POST['employee_name']
        employee_username=request.POST['employee_username']
        employee_phone=request.POST['employee_phone']
        employee_email=request.POST['employee_email']
        employee_state=request.POST['employee_state']
        employee_district=request.POST['employee_district']
        employee_zipcode=request.POST['employee_zipcode']
        employee_address=request.POST['employee_address']
        Employee.objects.filter(id=staff_id).update(employee_zipcode=employee_zipcode,employee_address=employee_address,  employee_email=employee_email,employee_state=employee_state, employee_district=employee_district,  employee_name=employee_name, employee_username=employee_username,employee_phone=employee_phone )
        return render(request,'editstaff.html',{'status':1})
    else:
        staffdetails = Employee.objects.get(id=staff_id)
        print(staffdetails)
        
    context={
        "is_marketingstaff":True,
        'staffdetails':staffdetails,
        'status':0
        }
    return render(request,'editstaff.html',context)    



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


def bank(request):
    if request.method == 'POST':
        bank_name = request.POST['bank_name']
        bank_holdername = request.POST['bank_holdername']
        bank_accountname = request.POST['bank_accountname']
        bank_ifsc = request.POST['bank_ifsc']
        bank_branch = request.POST['bank_branch']
        addbank= AddBank(bank_name=bank_name, bank_holdername=bank_holdername, bank_accountname=bank_accountname, bank_ifsc=bank_ifsc, bank_branch=bank_branch, bank_balance=0)
        addbank.save()
        return render(request,'addbank.html',{'status':1,})
    else:
        context={
        "is_bank":True,
        'status':0,
        }
        return render(request,'addbank.html',context)
        

        

        
        
    



    
     
    

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
      


def profitandloss(req):
    context={
        "is_profitandloss":True
        }
    return render(req,'profit&loss.html',context)



   
def demo(request):
    return render(request,'demo/index.html')



    
        

      
