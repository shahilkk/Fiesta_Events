
from django.shortcuts import render , redirect

from . models import Employee,Product,AddBank,Client
import random
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
# Create your views here.


def master(req):
    return render(req,'master.html')

def index(req):
    context={"is_index":True}
    return render(req,'index.html',context)  

def customer(req):
    # context={"is_customer":True}
    customerlist=Client.objects.all()
    context={
        "is_customer":True,
     "customerlist":customerlist
    }
    return render(req,'customer.html',context)



def addcustomer(request):
   
    context={"is_customer":True}
    rand=random.randint(10000,9999999)
    client_uid = 'CLT'+str(rand)
    if request.method=='POST':
       
        client_name=request.POST['client_name']
        client_gst_number=request.POST['client_gst_number']
        client_whsatpp=request.POST['client_whsatpp']
        client_phone=request.POST['client_phone']
        client_email=request.POST['client_email']
        client_state=request.POST['client_state']
        client_district=request.POST['client_district']
        client_zipcode=request.POST['client_zipcode']
        client_address=request.POST['client_address']
        client_bankholder=request.POST['client_bankholder']
        client_bankname=request.POST['client_bankname']
        client_ifsc=request.POST['client_ifsc']
        client_actnnumber=request.POST['client_actnnumber']
        client_contact_type=request.POST['client_contact_type']
        print(client_name)
        client_add=Client(client_name=client_name,client_gst_number=client_gst_number
        ,client_id=client_uid,client_phone=client_phone,client_email=client_email,
        client_state=client_state,client_district=client_district,client_zipcode=client_zipcode
        ,client_address=client_address,client_contact_type=client_contact_type,client_whsatpp=client_whsatpp,client_actnnumber=client_actnnumber, client_ifsc=client_ifsc, client_bankname=client_bankname, client_bankholder=client_bankholder )
        client_add.save()
        return redirect('/user/customer')
       
    return render(request,'addcustomer.html',context) 



def editcustomer(request,id):
    if request.method=='POST':
        client_name=request.POST['client_name']
        client_gst_number=request.POST['client_gst_number']
        client_whsatpp=request.POST['client_whsatpp']
        client_phone=request.POST['client_phone']
        client_email=request.POST['client_email']
        client_state=request.POST['client_state']
        client_district=request.POST['client_district']
        client_zipcode=request.POST['client_zipcode']
        client_address=request.POST['client_address']
        client_contact_type=request.POST['client_contact_type']
        Client.objects.filter(id=id).update(client_name=client_name,client_gst_number=client_gst_number
        ,client_phone=client_phone,client_email=client_email,
        client_state=client_state,client_district=client_district,client_zipcode=client_zipcode
        ,client_address=client_address,client_contact_type=client_contact_type,client_whsatpp=client_whsatpp)
        return render(request,'editcustomer.html',{'status':1})

    else:
        print(id)
        editcust=Client.objects.get(id=id)
    context={
        "is_customer":True,
        "editcust":editcust,
        'status':0
        }
    return render(request,'editcustomer.html',context)   


def viewcustomer(request,id):
    print(id)
    details=Client.objects.get(id=id)
    context={
        "is_custome":True,
        "details":details
        }
    return render(request,'viewcustomer.html',context)  


def deletecustomer(request,id):
    Client.objects.filter(id=id).update(client_status='InActive')
    return redirect ('/user/customer')


def viewemployee(requsest,id):
    print(id)
    details = Employee.objects.get(id=id)
    context={
        'details':details
    }
    return render(requsest,'viewemployee.html',context)         
        


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
        return redirect('/user/marketingstaff')
        
        
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

def deletestaff(request,id):
    Employee.objects.filter(id=id).update(employee_status='Inactive')   
    return redirect('/user/marketingstaff')  



def Estimate(request):
    context={"is_estimate":True}
    
    return render(request,'Estimate.html',context)   


def addestimate(req):
    
    cust = Client.objects.all()
    context={
        "is_estimate":True,
        'cust':cust
        }
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
        return redirect('/user/products')
        # msg = " product added"

    view_product = Product.objects.filter(food_status=True).all()  
    context={
        "is_product":True,
        'view_product': view_product
    }
    return render(request,'products.html',context) 

# @csrf_exempt
# def getproduct(request):
#     productID = request.POST.get('productID')

#     product=Product.objects.get(id=productID)

#     data={
#         "food_name":product.food_name,
#         "catagory":product.catagory,
#         "priceper_head":product.priceper_head,
#         "priceper_kg":product.priceper_kg,
#         "food_deatails":product.food_deatails

#     }
#     return JsonResponse({'product': data})  
@csrf_exempt     
def getproductGet(request,id):

    product=Product.objects.get(id=id)

    data={
        "food_name":product.food_name,
        "catagory":product.catagory,
        "priceper_head":product.priceper_head,
        "priceper_kg":product.priceper_kg,
        "food_deatails":product.food_deatails

    }
    # listone=[]
    # listone.append(data)
    # listone.append(data)
    return JsonResponse({'product': data})  
     


@csrf_exempt
def editProductdata(request,id):

    editproduct=Product.objects.get(id=id)
    # print(editproduct)
    
    data={
        "food_name":editproduct.food_name,
        "catagory":editproduct.catagory,
        "priceper_head":editproduct.priceper_head,
        "priceper_kg":editproduct.priceper_kg,
        "food_deatails":editproduct.food_deatails

    }
    return JsonResponse({'product': data})
          
@csrf_exempt
def updateproduct(request):
    id=request.POST['producId']
    food_name = request.POST['editfood']
    catagory = request.POST['editcat']
    priceper_head = request.POST['editperhead']
    priceper_kg = request.POST['editperkg']
    food_deatails = request.POST['editdecrption']
    Product.objects.filter(id=id).update(food_name=food_name, catagory=catagory, priceper_head=priceper_head ,priceper_kg=priceper_kg,food_deatails=food_deatails )
    return JsonResponse({'message': 'sucesses'})
    
 
def delete(request,id):
    Product.objects.filter(id=id).update(food_status=False)  
    return redirect('/user/products')    



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



    
        

      
