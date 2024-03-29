
from builtins import int, print
from multiprocessing import context
from tracemalloc import take_snapshot
from urllib import response
from django.shortcuts import render , redirect 
from . models import Employee, Items,Product,Client,AddBank,Category,EstimateProduct,Estimates,PaymentDetails,Expences, Stock,Terms,Income,Preview,StockCatagory,StockDetails
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.db.models import Avg, Count, Min, Sum
from django.db.models import Q
from datetime import datetime, timedelta, time
from decorator import admin_login_required
from django.conf import settings
from django.core.mail import send_mail
from random import randint
from django.conf.global_settings import EMAIL_HOST_USER
# Create your views here.


def master(request):    
    return render(request,'master.html')


@admin_login_required
def index(request):
    pending = Estimates.objects.filter(est_status ='Pending',est_active=True).all()
    billed = Estimates.objects.filter(est_status ='Billed',est_active=True).all()
    advanced = Estimates.objects.filter(est_status ='Advanced',est_active=True).all()
    paritialy = Estimates.objects.filter(est_status ='Partialy Paid',est_active=True).all()
    closed = Estimates.objects.filter(est_status ='Closed',est_active=True).all()
    bank = AddBank.objects.all()
    

    context={
        "is_index":True,
        'pending' : pending,
        'billed':billed,
        'advanced':advanced,
        'paritialy':paritialy,
        'closed':closed,
        'bank':bank
        }
    return render(request,'index.html',context) 



def indexbill(request,id):
    Estimates.objects.filter(id=id).update(est_status ='Billed')
    return redirect('/index')



def indexadvanced(request,id):
    Estimates.objects.filter(id=id).update(est_status ='Advanced')
    return redirect('/index')



def indexpartialy(request,id):
    Estimates.objects.filter(id=id).update(est_status ='Partialy Paid')
    return redirect('/index')

def indexclosed(request,id):
    Estimates.objects.filter(id=id).update(est_status ='Closed')
    return redirect('/index')            





@admin_login_required
def customer(req):
    # context={"is_customer":True}
    customerlist=Client.objects.all()
    context={
        "is_customer":True,
     "customerlist":customerlist
    }
    return render(req,'customer.html',context)



def addcustomer(request):


    if Client.objects.exists():
        est = Client.objects.last().id
        est_id = 'CLT'+str(1001+est)
    else:
        est=0
        est_id = 'VMINS'+str(1001+est)
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
        client_add=Client(client_name=client_name,client_gst_number=client_gst_number
        ,client_id=est_id,client_phone=client_phone,client_email=client_email,
        client_state=client_state,client_district=client_district,client_zipcode=client_zipcode
        ,client_address=client_address,client_contact_type=client_contact_type,client_whsatpp=client_whsatpp)
        client_add.save()
        return redirect('/customer')
    context={
        "is_customer":True,
       
        }   
    return render(request,'addcustomer.html',context) 


def savecustomer(request):
    if Client.objects.exists():
        est = Client.objects.last().id
        est_id = 'CLT'+str(1001+est)
    else:
        est=0
        est_id = 'CLT'+str(1001+est)
    
       
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
    client_add=Client(client_name=client_name,client_gst_number=client_gst_number
    ,client_id=est_id,client_phone=client_phone,client_email=client_email,
    client_state=client_state,client_district=client_district,client_zipcode=client_zipcode
    ,client_address=client_address,client_contact_type=client_contact_type,client_whsatpp=client_whsatpp)
    client_add.save()
    return JsonResponse({'message': 'sucesses'})


def estimatedata(request):
    if Client.objects.exists():
        est = Client.objects.last().id
        est_id = 'CLT'+str(1001+est)
    else:
        est=0
        est_id = 'CLT'+str(1001+est)
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
    client_add=Client(client_name=client_name,client_gst_number=client_gst_number
    ,client_id=est_id,client_phone=client_phone,client_email=client_email,
    client_state=client_state,client_district=client_district,client_zipcode=client_zipcode
    ,client_address=client_address,client_contact_type=client_contact_type,client_whsatpp=client_whsatpp)
    client_add.save()
    data={
        "client_phone":client_add.client_phone,
    }
    return JsonResponse({'client':data})




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
        editcust=Client.objects.get(id=id)
    context={
        "is_customer":True,
        "editcust":editcust,
        'status':0
        }
    return render(request,'editcustomer.html',context)   


def viewcustomer(request,id):
    details=Client.objects.get(id=id)
    context={
        "is_custome":True,
        "details":details
        }
    return render(request,'viewcustomer.html',context)  


def deletecustomer(request,id):
    Client.objects.filter(id=id).update(client_status='InActive')
    return redirect ('/customer')


def viewemployee(requsest,id):
    details = Employee.objects.get(id=id)
    context={
        'details':details
    }
    return render(requsest,'viewemployee.html',context)         
        

@admin_login_required
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
        emplyoeedetails=Employee(employee_name=employee_name, employee_username=employee_username, employee_password=employee_password, employee_phone=employee_phone, employee_email=employee_email, employee_state=employee_state, employee_district=employee_district, employee_zipcode=employee_zipcode, employee_address=employee_address, employee_status='Active')
        emplyoeedetails.save()
        return redirect('/marketingstaff')
        
        
    return render(request,'addmstaff.html',context)



def editstaff(request,staff_id):
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
        
    context={
        "is_marketingstaff":True,
        'staffdetails':staffdetails,
        'status':0
        }   
    return render(request,'editstaff.html',context)  


def deletestaff(request,id):
    Employee.objects.filter(id=id).update(employee_status='Inactive')   
    return redirect('/marketingstaff')  


@admin_login_required
def Estimate(request):
    if request.method=='POST':
        fromdate=request.POST['fromdate']
        todate=request.POST['todate']
        field=request.POST['field']
        
        srch_date=Estimates.objects.filter(Q(est_fromdate__icontains=fromdate) & Q(est_todate__icontains=todate) & Q(est_status__icontains=field))
        if srch_date.exists():
            context={
            "is_estimate":True,
            'srch_date':srch_date
            }
        else:
            estimates = Estimates.objects.filter(est_active=True).all()
            context={
            "is_estimate":True,
            'estimateList':estimates
            }
    else:
        estimates = Estimates.objects.filter(est_active=True).all()
        context={
            "is_estimate":True,
            'estimateList':estimates
            }


    
    return render(request,'Estimate.html',context)   

    # estimates = Estimates.objects.all()
    # class EstimateList:
    #     def __init__(self,estimate,total) :
    #         self.estimate = estimate
    #         self.total = total
    # estimatelist=[]
    # for estimate in estimates:
    #     products=EstimateProduct.objects.filter(estimateid=estimate)
    #     total=0
    #     if products.exists():
    #         for product in products:
    #             total+=int(product.est_qty)+product.est_price

    #     estimatelist.append(EstimateList(estimate,total))

    # context={
    #     "is_estimate":True,
    #     "estimate": estimatelist
    #     }


    
    # return render(request,'Estimate.html',context)   



# def formesmimate(request):
    
#         # return reverse('addestimate', args(order_id))
#         # getid = Estimates.objects.get(clientd_id=clientid)
#         return redirect('addestimate/'+order_id)
       
#     else:
#         cust = Client.objects.all()
#         pro = Product.objects.all()
#         context={
#             "is_estimate":True,
#             'cust':cust,
#             'pro':pro
#             }
#     return render(request,'addestimate.html',locals())

@admin_login_required
def addestimate(request):
    cust = Client.objects.all()
    pro = Product.objects.all()
    if request.method=='POST':
        checkphone=request.POST['checkphone']
        if Client.objects.filter(client_phone=checkphone).exists():

            clientid = Client.objects.get(client_phone=checkphone)
            fromdate=request.POST['dataform']
            todate=request.POST['todate']
            est_id = Client.objects.get(id=clientid.id)

            
            esti=Estimates(clientd=est_id,est_fromdate=fromdate, est_todate=todate)
            esti.save()
            context={
            "is_estimate":True,
            'cust':cust,
            'pro':pro,
            "estimate":esti
            }
            order_id = esti.id
        else:
            return render(request,'addestimate.html',{'msg':'Customer Not Found Please Add'})   
        
        return render(request,'addestimate.html',context)

    # if Estimate.objects.exists():
    #     est = Estimate.objects.last().id
    #     est_id = 'EST'+int(10+est)
    # else:
    #     est=0
    #     est_id = 'EST'+int(10+est)

    
    context={
            "is_estimate":True,
            'cust':cust,
            'pro':pro
            }
    return render(request,'addestimate.html',context) 

@admin_login_required
def createestimate(request):
    cust = Client.objects.all()
    if request.method=='POST':
        clientid=request.POST['checkname']
        
        fromdate=request.POST['dataform']
        todate=request.POST['todate']
        est_id = Client.objects.get(id=clientid)
        estit=Estimates(clientd=est_id,est_fromdate=fromdate, est_todate=todate)
        estit.save() 
        context={
            "is_estimate":True,
            'cust':cust,
            "estimate":estit
            }
        return render(request,'createestimate.html',context)
          
    else:
        context={
                "is_estimate":True,
                'cust':cust,
                
                }
        return render(request,'createestimate.html',context)      


  


@csrf_exempt
def addcat(request):
    catagory_name=request.POST['catagory_name']
    obj= Category(category=catagory_name)
    obj.save()
    return JsonResponse({'category':obj.category})


   

def editestimate(request,id):
    pro = Product.objects.all()
    estimate = Estimates.objects.get(id=id)
    class ProductList:
        def __init__(self,index,item,priceper_head,priceper_kg) :
            self.index=index
            self.item = item
            self.priceper_head = priceper_head
            self.priceper_kg = priceper_kg
    estimateItemsList =[]  
    estimateItems=EstimateProduct.objects.filter(estimateid=estimate)
    i=1
    for estimateitem in estimateItems:
        propPricePerHead=estimateitem.productid.priceper_head
        propPricePerKG=estimateitem.productid.priceper_kg
        estimateItemsList.append(ProductList(i,estimateitem,propPricePerHead,propPricePerKG))
        i+=1

    details = EstimateProduct.objects.filter(estimateid=id)
    estimte= Estimates.objects.select_related('clientd').get(id=id)
    context={
        "is_estimate":True,
        "estimte":estimte,
        "details":details,
        "pro":pro,
        "estimateItemsList":estimateItemsList
        }
    return render(request,'editestimate.html',context)   


def viewestimate(request,id):
    clientdetails = Estimates.objects.select_related('clientd').get(id=id)
    details = EstimateProduct.objects.filter(estimateid=id)
    estid= EstimateProduct.objects.filter(estimateid=id)
    totalvalue=estid.aggregate(Sum('est_amount'))
    totalAmonut = totalvalue['est_amount__sum']
    gsttotal =totalAmonut*5/100
    total = totalAmonut + gsttotal

    context={
        "is_estimate":True,
        "clientdetails":clientdetails,
        "details":details,
        "totalAmonut":totalAmonut,
        "gsttotal":gsttotal,
        "total":total
        
        }
    return render(request,'viewestimate.html',context) 



def Delectestimate(request,id):
    delectestimate =  Estimates.objects.filter(id=id).update(est_active=False)
    return redirect('/index')


def invoicegrid(req):
    context={"is_invoice":True}
    return render(req,'invoicegrid.html',context)        
  
@admin_login_required
def invoiceList(req):
    alllist = Estimates.objects.filter(est_active=True).all()
    billed = Estimates.objects.filter(est_status ='Billed').all().count()
    totalbilled=Estimates.objects.filter(est_status ='Billed').aggregate(Sum('est_balance'))
    totalAmonutbilled = totalbilled['est_balance__sum']
    advanced = Estimates.objects.filter(est_status ='Advanced').all().count()
    totaladvanced=Estimates.objects.filter(est_status ='Advanced').aggregate(Sum('est_balance'))
    totalAmonutadvanced = totaladvanced['est_balance__sum']
    paritialy = Estimates.objects.filter(est_status ='Partialy Paid').all().count()
    totalparitialy=Estimates.objects.filter(est_status ='Partialy Paid').aggregate(Sum('est_balance'))
    totalAmonutparitialy = totalparitialy['est_balance__sum']
    closed = Estimates.objects.filter(est_status ='Closed').all().count()
    totalclosed=Estimates.objects.filter(est_status ='Closed').aggregate(Sum('est_balance'))
    totalAmonutclosed = totalclosed['est_balance__sum']

    context={
        "is_invoice":True,
        "alllist":alllist,
        "billed":billed,
        "advanced":advanced,
        "paritialy":paritialy,
        "closed":closed,
        "totalAmonutbilled":totalAmonutbilled,
        "totalAmonutadvanced":totalAmonutadvanced,
        "totalAmonutparitialy":totalAmonutparitialy,
        "totalAmonutclosed":totalAmonutclosed
       
        }
    return render(req,'invoiceList.html',context) 


def addinvoice(request):

    context={
        "is_invoice":True,
    }
    return render(request,'addinvoice.html',context)



def invoicedetails(request,id):
    discount=request.GET['discount']
    
    details = EstimateProduct.objects.filter(estimateid=id)
    eid= Estimates.objects.get(id=id)
    billing = PaymentDetails.objects.select_related('clientid','bankid','estimateId').filter(estimateId=eid).last()
    termandnote =Terms.objects.filter(estimateid=id).last()

    estid= EstimateProduct.objects.filter(estimateid=id)
    totalvalue=estid.aggregate(Sum('est_amount'))
    totalAmonut = totalvalue['est_amount__sum']
    gsttotal =totalAmonut*5/100
    # sgst = (totalAmonut*5/100)/2
    total = totalAmonut + gsttotal
    grandtotal = total-int(discount)


    # preview = Preview.objects.get(estimateId=id)
    context={
        "is_invoice":True,
        'billing':billing,
        "details":details,
        "totalAmonut":totalAmonut,
        "gsttotal":gsttotal,
        "discount":discount,
        "grandtotal":grandtotal,
        "termandnote":termandnote,
        # "preview":preview,
        "eid":eid
        }
    return render(request,'invoicedetails.html',context) 


def editinvoice(req):
    context={"is_invoice":True}
    return render(req,'editinvoice.html',context) 



@admin_login_required
def bank(request):
    if request.method == 'POST':
        bank_name = request.POST['bank_name']
        bank_holdername = request.POST['bank_holdername']
        bank_accountname = request.POST['bank_accountname']
        bank_ifsc = request.POST['bank_ifsc']
        bank_branch = request.POST['bank_branch']
        addbank = AddBank(bank_name=bank_name, bank_holdername=bank_holdername, bank_accountname=bank_accountname, bank_ifsc=bank_ifsc, bank_branch=bank_branch, bank_balance=0)
        addbank.save()
        return render(request,'addbank.html',{'status':1,})
    else:
        context={
        "is_bank":True,
        'status':0,
        }
    return render(request,'addbank.html',context)
        
 
@admin_login_required
def products(request):
   
    # msg = ''
    if request.method == 'POST':
        food_name = request.POST['food_name']
        catagory = request.POST['catagory']
        priceper_head = request.POST['priceper_head']
        priceper_kg = request.POST['priceper_kg']
        food_deatails = request.POST['food_deatails']
        catname=Category.objects.get(category=catagory)
        food_exist = Product(food_name = food_name,catagory = catname,priceper_head = priceper_head,priceper_kg = priceper_kg,food_deatails = food_deatails)
        food_exist.save()
        return redirect('/products')
        # msg = " product added"

    else:
        view_product = Product.objects.filter(food_status=True).all() 
        view_cat = Category.objects.all() 
        context={
            "is_product":True,
            'view_product': view_product,
            'view_cat':view_cat
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
        "catagory":product.catagory.category,
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
    
    data={
        "food_name":editproduct.food_name,
        "catagory":editproduct.catagory.category,
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
    return redirect('/products')    


@admin_login_required
def payment(request):
    paymentlist = PaymentDetails.objects.all()
    context={
        "is_payment":True,
        'paymentlist':paymentlist
        }
    return render(request,'payment.html',context)  


def addpayment(request,id):
    companybank = AddBank.objects.all()
    cusmoterdetails = Estimates.objects.select_related('clientd').get(id=id)
    if request.method == 'POST':
        paymentdate = request.POST['paymentdate']
        paymentclientname = request.POST['paymentclientname']
        paymentamount = request.POST['paymentamount']
        paymentestimateid = request.POST['paymentestimateid']
        paymentcompanybank = request.POST['paymentcompanybank']
        paymentclientid = request.POST['paymentclientid']
        
        clientID= Client.objects.get(id=paymentclientid)  
        bank=AddBank.objects.get(id=paymentcompanybank)
        estimate = Estimates.objects.get(id=paymentestimateid)
        payment = PaymentDetails(clientid=clientID,bankid=bank,estimateId=estimate,paymentdate=paymentdate,paymentamount=paymentamount)
        payment.save()
        qunless =Estimates.objects.get(id=paymentestimateid)
        qunless.est_balance = qunless.est_balance-int(paymentamount)
        qunless.save()
        addamount =AddBank.objects.get(id=paymentcompanybank)
        addamount.bank_balance=addamount.bank_balance + int(paymentamount)
        addamount.save()
        context={
        "is_payment":True,
        "cusmoterdetails":cusmoterdetails,
        "companybank":companybank,
        "payment":payment
        }
        return render(request,'addpayment.html',context) 
    context={
        "is_payment":True,
        "cusmoterdetails":cusmoterdetails,
        "companybank":companybank
        }
    return render(request,'addpayment.html',context)   



@admin_login_required
def expenses(request):
   
    if request.method=='POST':
        profitandlossdate=request.POST['profitandlossdate']
        # print(profitandlossdate)
        srch_date= Expences.objects.filter(Q(expencesdate__icontains=profitandlossdate))
        if srch_date.exists():
            context={
                "is_expenses":True,
                'srch_date':srch_date

            }
        else:
            expenselist = Expences.objects.filter(expencestatus='Expences').all()

            context={
            "is_expenses":True,
            "expenselist":expenselist
            }
    else:
        expenselist = Expences.objects.filter(expencestatus='Expences').all()

        context={
            "is_expenses":True,
            "expenselist":expenselist
            }

   
    return render(request,'expenses.html',context) 

# def expenses(request):
#     expenselist = ProfitsandLoss.objects.filter(profitandlosstatus='Expences').all()
#     context={
#         "is_expenses":True,
#         "expenselist":expenselist
#     }
#     return render(request,'expenses.html',context)          



def addexpenses(request):

    if request.method=='POST':
        category=request.POST['category']
        note=request.POST['note']
        
        amount=request.POST['amount']
       
        
        expencevalue =Expences( expencescategory=category,expencesnote=note,  expencesasamount=amount ,expencestatus='Expences')
        expencevalue.save()
        return redirect('/expenses')

    context={
        "is_expenses":True,
    }
    return render(request,'addexpence.html',context)


@admin_login_required
def profit(request):
    if request.method=='POST':
        date=request.POST['date']
        srch_date= Income.objects.filter(Q(date__icontains=date))

        if srch_date.exists():
            context={
                "is_profit":True,
                'srch_date':srch_date
            }
        else:
            profitlist = Income.objects.select_related('estimateId').all()

            context={
            "is_profit":True,
            "profitlist":profitlist
            }
    else:
        profitlist = Income.objects.select_related('estimateId').all()

        context={
         "is_profit":True,
         "profitlist":profitlist
         }
    return render(request,'profit.html',context)  
    


    # profitlist = Income.objects.select_related('estimateId').all()

    # context={
    #     "is_profit":True,
    #     "profitlist":profitlist
    #     }
    # return render(request,'profit.html',context)          



def addprofit(request):
    if request.method=='POST':
        category=request.POST['category']
        note=request.POST['note']
        date=request.POST['date']
        phone=request.POST['phone']
        amount=request.POST['amount']
        clientid= Client.objects.get(client_phone=phone)
        profitvalue = Expences(clientid=clientid, expencescategory=category,expencesnote=note, expencesdate=date, expencesasamount=amount ,expencestatus='Expences')
        profitvalue.save()
        return redirect('/profit')
    context={
        "is_profit":True,
        }


    return render(request,'addprofit.html',context)



@admin_login_required
def filter(req):
    alllist = Estimates.objects.filter(est_active=True).all()
    billed = Estimates.objects.filter(est_status ='Billed').all()
    advanced = Estimates.objects.filter(est_status ='Advanced').all()
    paritialy = Estimates.objects.filter(est_status ='Partialy Paid').all()
    closed = Estimates.objects.filter(est_status ='Closed').all()

    context={
        "is_filter":True,
        'alllist' : alllist,
        'billed':billed,
        'advanced':advanced,
        'paritialy':paritialy,
        'closed':closed
        }
    return render(req,'filter.html',context) 
      

@admin_login_required
def profitandloss(request):
    context={

        "is_profitandloss":True,

        }
    return render(request,'profit&loss.html',context)



def netprofit(request):
    today = datetime.now().date()
    today_start = datetime.combine(today, time())
    data = []
    recent_expenses=Expences.objects.filter(expencesdate__gte=today_start).values('id','expencesasamount','expencestatus','expencesdate','expencescategory')
    recent_income=Income.objects.filter(date__gte=today_start).values('id','incomeamount','date','incomestatus')
    queryset = list(recent_income)+list(recent_expenses)
    return JsonResponse({'data':queryset})
        



   
def demo(request):
    return render(request,'demo/index.html')



   
def createestimate(request):
    cust = Client.objects.all()
    if request.method=='POST':
        clientid=request.POST['checkname']
        
        fromdate=request.POST['dataform']
        todate=request.POST['todate']
        est_id = Client.objects.get(id=clientid)
        esti=Estimates(clientd=est_id,est_fromdate=fromdate, est_todate=todate)
        esti.save() 
        return redirect('/createestimate') 


    context={
            "is_estimate":True,
            'cust':cust,
            
            }
    return render(request,'createestimate.html',context)


@csrf_exempt
def bill(request):
    productname = request.POST['productname']
    # viewpro = Product.objects.filter(food_name=productname).count()
    # product_cat = viewpro.catagory.category
    # estimateid = request.POST['estimateid']
    # product_count = 0
    # product_count = Product.objects.filter(food_name=productname).count()
    # if product_count > 1 :
    #     viewproduct = Product.objects.filter(food_name=productname).last()
    # else :
    viewproduct = Product.objects.filter(food_name=productname).last()
    # catagoryname = viewpro.catagory.category
    # estid=Estimates.objects.get(id=estimateid)
    # product_data = viewproduct.food_name
    if viewproduct.catagory.category is not None:
        product_category = viewproduct.catagory.category
    else :
        product_category = viewproduct.catagory
    data={
        # "fdata":product_data,
        # "food_name":viewpro.food_name,
        # "estimateid":estid.id,
        "id":viewproduct.id,
        "catagory":product_category,
        "priceper_head":viewproduct.priceper_head,
        "priceper_kg":viewproduct.priceper_kg,
        "food_deatails":viewproduct.food_deatails
    }

    # data = {
    #     "catagory":viewpro,
    # }
    return JsonResponse(data)

@csrf_exempt
def billitem(request):
    productname = request.POST['productname']
    # estimateid = request.POST['estimateid']
    viewpro=Product.objects.get(food_name=productname)
    # estid=Estimates.objects.get(id=estimateid)
    data={
        
        # "food_name":viewpro.food_name,
        # "estimateid":estid.id,
        "id":viewpro.id,
        "catagory":viewpro.catagory.category,
        "priceper_head":viewpro.priceper_head,
        "priceper_kg":viewpro.priceper_kg,
        "food_deatails":viewpro.food_deatails
    }
    return JsonResponse({'product': data})


@csrf_exempt
def checkexist(request):
    check_name = request.POST['checkname']
    object = Product.objects.filter(food_name=check_name).exists()
    return JsonResponse({'IsExist':object})


# @csrf_exempt
# def create_estimate(request):
#     productId = request.POST['productId']
#     est_category = request.POST['est_category']
#     est_price = request.POST['est_price']
#     est_amount = request.POST[''est_amount']
#     est_qty = request.POST['est_qty']
#     var =Estimate.objects.filter().id
#     est_id='EST'+10+var
#     addest = EstimateProduct(estimate_id__id=productId,est_category=est_category, est_price=est_price, est_amount=est_amount, est_qty=est_qty)
#     addest.save()
#     return JsonResponse({'message': 'sucesses'})

@csrf_exempt
def est_product(request):
    estimateid = request.POST['estimateid']
    productId = request.POST['productId']
    est_category = request.POST['est_category']
    est_price = request.POST['est_price']
    est_amount = request.POST['est_amount']    
    est_qty = request.POST['est_qty']

    additionalchargeid = request.POST['additionalchargeid']
    gtotal = request.POST['grandtotal']

    pr=Product.objects.get(id=productId)
    estim=Estimates.objects.get(id=estimateid)
    addest = EstimateProduct(estimateid=estim,productid=pr,est_category=est_category, est_price=est_price, est_amount=est_amount, est_qty=est_qty)
    addest.save()
    estid= EstimateProduct.objects.filter(estimateid=estimateid)
    estTotal=estid.aggregate(Sum('est_amount'))
    totall = estTotal['est_amount__sum']
    # totalvalue=estid.aggregate(Sum('est_amount'))
    
    # totalAmonut = totalvalue['est_amount__sum']
    


    grandtotal = 0
    totalAmonut = int(gtotal)
    # print(totalAmonut,"#"*20)
    if totall == 0:
        gsttotal = 0
    else:
        gsttotal =totalAmonut*5/100
    grandtotal= totalAmonut+gsttotal
    extraamount=int(grandtotal)+int(additionalchargeid)

    total=Estimates.objects.filter(id=estimateid).update(est_balance=extraamount,totalsum=extraamount)
    return JsonResponse({'msg':'data inserted sucess'})



@csrf_exempt
def est_productupdate(request):
    estimateid = request.POST['estimateid']
    productId = request.POST['productId']
    est_category = request.POST['est_category']
    est_price = request.POST['est_price']
    est_amount = request.POST['est_amount']    
    est_qty = request.POST['est_qty']
    prodid=Product.objects.get(id=productId)
    estiid=Estimates.objects.get(id=estimateid)
    if EstimateProduct.objects.filter(estimateid=estiid, productid=prodid ).exists():
        updateproduct = EstimateProduct.objects.get(estimateid=estiid, productid=prodid )
        updateproduct.est_category=est_category
        updateproduct.est_price=est_price
        updateproduct.est_amount=est_amount
        updateproduct.est_qty=est_qty
        updateproduct.save()
        print('*'*20)

    else:
        EstimateProduct.objects.create(estimateid=estiid,productid=prodid,est_category=est_category, est_price=est_price, est_amount=est_amount, est_qty=est_qty)
    
    estid= EstimateProduct.objects.filter(estimateid=estimateid)
    totalvalue=estid.aggregate(Sum('est_amount'))
    totalAmonut = totalvalue['est_amount__sum']
    gsttotal =totalAmonut*5/100
    grandtotal= totalAmonut+gsttotal
    total=Estimates.objects.filter(id=estimateid).update(est_balance=grandtotal)
    data={
        
        
        "totalAmonut":totalAmonut,
        "gsttotal":gsttotal,
        "grandtotal":grandtotal

        
        
    }
    return JsonResponse({'msg':'data inserted sucess','details': data})



@csrf_exempt
def deletedata(request):
    product = request.POST['product']
    estimateid = request.POST['estimateid']
    estmate=Estimates.objects.get(id=estimateid)
    EstimateProduct.objects.get(productid=product,estimateid=estmate).delete()
    estid= EstimateProduct.objects.filter(estimateid=estimateid)
    totalvalue=estid.aggregate(Sum('est_amount'))
    totalAmonut = totalvalue['est_amount__sum']
    gsttotal = int(totalAmonut)*5/100
    grandtotal= totalAmonut+gsttotal
    total=Estimates.objects.filter(id=estimateid).update(est_balance=grandtotal)
    return JsonResponse({'msg':'data Delected sucess'})


@csrf_exempt
def invoicegetdata(request):
    data = {}
    clientphone = request.POST['clientphone']
    if Client.objects.filter(client_phone=clientphone).exists():

        viewpro=Client.objects.get(client_phone=clientphone)
        estimatelist=[]
        if Estimates.objects.filter(clientd=viewpro.id).exists():
            estID = Estimates.objects.filter(clientd=viewpro.id)
            for value in estID:
                clientdata={
                    "id":value.clientd.id,
                    "client_name":value.clientd.client_name
                }
                estdata={
                    "id":value.id,
                    "clientd":clientdata,
                    "est_fromdate":value.est_fromdate,
                    "est_todate":value.est_todate,
                    "est_balance":value.est_balance,
                    "est_status":value.est_status,
                }
                estimatelist.append(estdata)
                data={
            
                'msg':True,
                "id":viewpro.id,
                "gst":viewpro.client_gst_number,
                "email":viewpro.client_email,
                "state":viewpro.client_state,
                "district":viewpro.client_district,
                "zipcode":viewpro.client_zipcode,
                "address":viewpro.client_address,
                "estimatelist":estimatelist
                
            }
    else:
        data={
            'msg':False
        }

    
    return JsonResponse({'details': data})   





@csrf_exempt
def clientnamegetdata(request):
    clientname = request.POST['clientname']
    data = {}
    if Client.objects.filter(client_name=clientname).exists():
        viewpro=Client.objects.get(client_name=clientname)
        estimatelist=[]
        if Estimates.objects.filter(clientd=viewpro.id).exists():
            estID = Estimates.objects.filter(clientd=viewpro.id)
            for value in estID:
                clientdata={
                    "id":value.clientd.id,
                    "client_name":value.clientd.client_name
                }
                estdata={
                    "id":value.id,
                    "clientd":clientdata,
                    "est_fromdate":value.est_fromdate,
                    "est_todate":value.est_todate,
                    "est_balance":value.est_balance,
                    "est_status":value.est_status,
                }
                estimatelist.append(estdata)
                data={
            
                'msg':True,
                "id":viewpro.id,
                "gst":viewpro.client_gst_number,
                "email":viewpro.client_email,
                "state":viewpro.client_state,
                "district":viewpro.client_district,
                "zipcode":viewpro.client_zipcode,
                "address":viewpro.client_address,
                "estimatelist":estimatelist
                
            }
    else:
        data={
            'msg':False
        }

    
    return JsonResponse({'details': data}) 
    


def invoicebill(request,id):

   
    # payment = PaymentDetails.objects.filter(estimateId_id=id)    
    details = EstimateProduct.objects.filter(estimateid=id)
    estime = Estimates.objects.get(id=id)
    estid= EstimateProduct.objects.filter(estimateid=id)
    totalvalue=estid.aggregate(Sum('est_amount'))
    subtotal = totalvalue['est_amount__sum']
    if subtotal == 0:
        totalAmonut = int(estime.totalsum)
        gsttotal = 0
        sgst = 0
    else :
        totalAmonut = int(subtotal)
        gsttotal =totalAmonut*5/100
        sgst = (totalAmonut*5/100)/2
    grandtotal = totalAmonut + gsttotal
    print(grandtotal,"#"*20)
    context={
            "is_estimate":True,
            "details":details,
            # "payment":payment,
            "estime":estime,
            "totalAmonut":totalAmonut,
            "gsttotal":gsttotal,
            "grandtotal":grandtotal,
            "sgst":sgst
            
            
            }
    return render(request,'invoicebill.html',context)



@csrf_exempt
def savenote(request):
    addterms = request.POST['addterms']
    addnote = request.POST['addnote']
    estimateid = request.POST['estimateid']
    estid = Estimates.objects.get(id=estimateid)
    add = Terms(estimateid=estid,term=addterms,note=addnote)
    add.save()
    return JsonResponse({'msg':'Note Added'})



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            if username == "fiesta_2022" and password == 'fiesta_2022':
                userDetails = {
                    'is_admin':True
                }
                request.session['permission']=userDetails
                return redirect('/index') 
            else:
                login_data=Employee.objects.filter(employee_username=username,employee_password=password).exists()
                if login_data:
                    data=Employee.objects.get(employee_username=username,employee_password=password)
                    if data.employee_status=='Active':
                        userDetails = {
                            'is_admin':False
                        }
                        request.session['permission']=userDetails
                        return redirect('/index')
                    else:
                        return render(request,'login.html',{'status':2})
                else:
                    return render(request,'login.html',{'status':1})        
        except:
            return render(request,'login.html',{'status':0})
 
       
    return render(request,'login.html') 



def admin_logout(request):
    del request.session['permission']
    return redirect('userapp:login')   


def forget(request):
    otp=randint(10000,9999999)
    if request.method=='POST':
        forgetmail=request.POST['forgetmail']
        send_mail(
            "OTP for reseting password in Fiesta",
            str(otp),
            EMAIL_HOST_USER,
            [forgetmail],
            fail_silently=False,
            )
        employeedetails=Employee.objects.filter(employee_email=forgetmail).update(employee_password=str(otp))
    return render(request,'forgetpassword.html')    



def printlist(request):
    listview = Preview.objects.all()
    context={
            "is_print":True, 
            "listview":listview       
            }
    return render(request,'printlist.html',context) 
      

def deleteprintlist(request,id):
    Preview.objects.get(id=id).delete()
    return redirect('/printlist')
      

def viewpdf(request,id,discount,previewno):
    details = EstimateProduct.objects.filter(estimateid=id)
    eid= Estimates.objects.get(id=id)
    billing = PaymentDetails.objects.select_related('clientid','bankid','estimateId').filter(estimateId=eid).last()
    termandnote =Terms.objects.filter(estimateid=id).last()

    estid= EstimateProduct.objects.filter(estimateid=id)
    totalvalue=estid.aggregate(Sum('est_amount'))
    totalAmonut = totalvalue['est_amount__sum']
    gsttotal =totalAmonut*5/100
    # sgst = (totalAmonut*5/100)/2
    total = totalAmonut + gsttotal
    grandtotal = total-int(discount)


    preview = Preview.objects.get(prviewnumber=previewno)
    context={
        "is_invoice":True,
        'billing':billing,
        "details":details,
        "totalAmonut":totalAmonut,
        "gsttotal":gsttotal,
        "discount":discount,
        "grandtotal":grandtotal,
        "termandnote":termandnote,
        "preview":preview,
        "eid":eid
        }
    return render(request,'viewpdf.html',context) 
    


def save(request,id):
    discount=request.GET['discount']  
    eid= Estimates.objects.get(id=id)
    if Preview.objects.exists():
        est = Preview.objects.last().id
        est_id = 'INV'+str(1001+est)
    else:
        est=0
        est_id = 'INV'+str(1001+est)
    preview =Preview(estimateId=eid, discount=discount,prviewnumber=est_id)
    preview.save()
    details = EstimateProduct.objects.filter(estimateid=id)
    eid= Estimates.objects.get(id=id)
    billing = PaymentDetails.objects.select_related('clientid','bankid','estimateId').filter(estimateId=eid).last()
    termandnote =Terms.objects.filter(estimateid=id).last()

    estid= EstimateProduct.objects.filter(estimateid=id)
    totalvalue=estid.aggregate(Sum('est_amount'))
    totalAmonut = totalvalue['est_amount__sum']
    gsttotal =totalAmonut*5/100
    # sgst = (totalAmonut*5/100)/2
    total = totalAmonut + gsttotal
    grandtotal = total-int(discount)
    addincome = Income(estimateId=eid,incomestatus='Income',incomeamount=grandtotal)
    addincome.save()
    
    preview = Preview.objects.filter(estimateId=eid).last()
    
    context={
        "is_invoice":True,
        'billing':billing,
        "details":details,
        "totalAmonut":totalAmonut,
        "gsttotal":gsttotal,
        "discount":discount,
        "grandtotal":grandtotal,
        "termandnote":termandnote,
        "eid":eid,
        "preview":preview
        }
    return render(request,'invoicedetails.html',context) 



def stock(request):
    stock = Stock.objects.all()
    context={
        "is_stock":True,
        "stock":stock
        }
    return render(request,'stock.html',context)        


def addstock(request):
    allcatagory = StockCatagory.objects.all()
    
    if request.method=='POST':
        stockname=request.POST['stockname']
        quantity=request.POST['quantity']
        missingPrice = request.POST['missing_price']
        # sqft_price = request.POST['sqft_price']
        damagePrice = request.POST['damage_price']
        price = request.POST['price']
        category = request.POST['catagories']

        category_exist=StockCatagory.objects.filter(cat_name=category).exists()
        if not category_exist:
            new_category=StockCatagory(cat_name=category)
            new_category.save()
            addStock = Stock(stockname=stockname , quantity=quantity, missing_price= missingPrice, damage_price=damagePrice, price=price,category=new_category)
            addStock.save()
            context = {
            "is_stock":True,
            "allcatagory":allcatagory,
            "status":1
            }
            return render(request, 'addstock.html',context)
        else:
            catagory = StockCatagory.objects.get(cat_name=category)
            addStock = Stock(stockname=stockname , quantity=quantity, missing_price= missingPrice, damage_price=damagePrice, price=price,category=catagory)
            addStock.save()
            context = {
            "is_stock":True,
            "allcatagory":allcatagory,
            "status":1
            }
            return render(request, 'addstock.html',context)


    context={
        "is_stock":True,
        "allcatagory":allcatagory
        }
    return render(request,'addstock.html',context)        
  

def editstock(request,id):
    stock=Stock.objects.get(id=id)
    if request.method=='POST':
        stockname=request.POST['stockname']
        quantity=request.POST['quantity']
        price=request.POST['price']
        damageprice=request.POST['damageprice']
        missprice=request.POST['missprice']
        sqftprice=request.POST['sqftprice']
        Stock.objects.filter(id=id).update(stockname=stockname , quantity=quantity, price=price, damage_price=damageprice,missing_price=missprice)
        return redirect('/stock')
    context={
        "is_stock":True,
        "stock":stock
        }
    return render(request,'editstock.html',context)        
  


def addmaterial(request,id):
    stock= Stock.objects.all()
    context={
        "is_stock":True,
        "stock":stock,
        "id":id
        }
    return render(request,'addmaterial.html',context)        
  

def getQunatity(request):
    stockname = request.GET['name']
    stocklist = Stock.objects.get(stockname=stockname)
    data={
        "quantiy":stocklist.quantity,
        "id":stocklist.id,
    }
    return JsonResponse({'stock':data,})


@csrf_exempt
def valuesave(request):
    estimateid = request.POST['estimateid']
    productId = request.POST['productId']
    stock = request.POST['stock']
    qty = request.POST['qty']
    needed = request.POST['needed']  
    # stockid=Stock.objects.get(id=productId)
    stc=Stock.objects.get(stockname=stock)
    estimate=Estimates.objects.get(id=estimateid)
    details = Items(estimate=estimate, stock=stc, taken=needed)
    details.save()
    added_qty = Stock.objects.get(stockname=stock)
    added_qty.quantity = added_qty.quantity -int(needed)
    added_qty.save()
    return JsonResponse({'msg':'data inserted sucess'})

    
def viewaddedmaterial(request,id):
    estimates = Estimates.objects.get(id=id)
    view = Items.objects.filter(estimate=estimates,status="not returned")
    context={
        "is_stock":True,
        "view":view,
        "estimates":estimates
        }
    return render(request,'viewaddedmaterial.html',context)        
  


def stocktransfer(request):
    returnQty = request.POST['returnQty']
    id = request.POST['id']
    status = "Rejected"
    transfer_obj = Items.objects.get(id=id)
    transfer_obj.stock.quantity = transfer_obj.stock.quantity + int(returnQty)
    transfer_obj.stock.save()
    transfer_obj.taken = transfer_obj.taken -int(returnQty)
    transfer_obj.save()
    return JsonResponse({'msg':'Staff Transfer Success'})




@csrf_exempt
def phoneexist(request):
    client_phone = request.POST['client_phone']
    object = Client.objects.filter(client_phone=client_phone).exists()
    return JsonResponse({'IsExist':object})



    
@admin_login_required
def rentoutlist(request):
    takenlist = Items.objects.filter(taken__gt=0 , status="not returned")
    context={
        "is_rent":True,
        "takenlist":takenlist
        }
    return render(request,'rentoutlist.html',context)    







@csrf_exempt
def returningitems(request):
    returnQty = request.POST['returnQty']
    Estimateid = request.POST['Estimateid']
    StockId = request.POST['StockId']
    damage_qty = request.POST['damage_qty']
    missed_qty = request.POST['missed_qty']
    ItemId = request.POST['ItemId']


    # print(returnQty, damage_qty, missed_qty,Estimateid,StockId)
    estimate = Estimates.objects.get(id=Estimateid)
    stock = Stock.objects.get(id=StockId)
    # print(estimate,stock)

    price = stock.price
    print(price)
    damage_amount = stock.damage_price
    missing_amount = stock.missing_price
    
    item = Items.objects.get(id=ItemId)
    qty_taken = item.taken
    # print(qty_taken,missing_amount,damage_amount)
   
    
   
    

    #damage

    if damage_qty == '' :

        damage_qty = 0
        damage_qty_amt = 0

         
    else :
        
        damage_qty_amt = int(damage_amount) * int(damage_qty)


        # print (damage_qty_amt)  

    
    # missings 
    
    if missed_qty == '' :
        print(returnQty,damage_qty)   
        missed_qty = int(returnQty) + int(damage_qty)
        print(missed_qty, 'hiiiiiii')

        missing_quantity = qty_taken - missed_qty 
        print(missing_quantity, 'hello')

        missing_qty_amt = missing_quantity * int(missing_amount)

        print(missing_qty_amt)

      

    else:
 
        missing_qty_amt = int(missing_amount) * int(missed_qty)
        print(missing_qty_amt, 'heeeeeee')


   
    totalrentamount = int(returnQty) * int(price)
    print(totalrentamount)


    
    total_amount =  damage_qty_amt + missing_qty_amt + totalrentamount
    print(total_amount, 'sum')

    
    transfer_obj = Items.objects.get(id=ItemId)
    transfer_obj.stock.quantity = transfer_obj.stock.quantity + int(returnQty)
    transfer_obj.stock.save()
    transfer_obj.taken = transfer_obj.taken -int(returnQty)
    transfer_obj.save()
    estimateid = Estimates.objects.get(id=Estimateid)
    stockid = Stock.objects.get(id=StockId)
    damaged_item = StockDetails(estimate=estimateid, stock=stockid, damagedstock=damage_qty, missingstock=missed_qty,returnstock=returnQty,grandtotal=total_amount)
    damaged_item.save()
    itemstatus = Items.objects.filter(id=ItemId).update(status='Returned')

    data = {
        'total':total_amount,
        'status':"returned",
    }

    return JsonResponse(data)




def damage(request):
    damagelist = StockDetails.objects.all()
    context={
        "is_stock":True,
        "damagelist":damagelist
        }
    return render(request,'damage.html',context)



# estimate
def estmatenew(request,id):
    clientdetails = Estimates.objects.select_related('clientd').get(id=id)
    # details = EstimateProduct.objects.filter(estimateid=id)
    products = EstimateProduct.objects.select_related('productid').filter(estimateid=id).values('productid__catagory__category','productid__food_name').order_by('productid__catagory__category')
    # products = EstimateProduct.objects.filter(estimateid=id).order_by('productid__catagory__category')

    totalsumval= clientdetails.totalsum

    estid= EstimateProduct.objects.filter(estimateid=id)
    note = Terms.objects.filter(estimateid=id).last()
    totalvalue=estid.aggregate(Sum('est_amount'))
    totalAmonut = totalvalue['est_amount__sum']


    gsttotal =totalAmonut*5/100
    cgst = gsttotal/2
    total = totalAmonut + gsttotal

    
    addedamount=totalsumval-total 
  
    context={
        "is_estimate":True,
        "clientdetails":clientdetails,
        # "details":details,
        # "details":details,
        "products":products,
        "totalAmonut":totalAmonut,
        "gsttotal":gsttotal,
        "total":total,
        "cgst":cgst,
        "note":note,
        "addedamount":addedamount,
        "totalsumval":clientdetails.totalsum
        
        }

    return render(request,'quatation.html',context)


# invoicebill

def invoicebillnew(request,id):
    
    clientdetails = Estimates.objects.select_related('clientd').get(id=id)
    details = EstimateProduct.objects.filter(estimateid=id)
    estid= EstimateProduct.objects.filter(estimateid=id)
    note = Terms.objects.filter(estimateid=id).last()
    totalvalue=estid.aggregate(Sum('est_amount'))
    # totalAmonut = totalvalue['est_amount__sum']
    # print(totalAmonut,"#"*10)
    # totalAmonut = 0
    totalAmonut_value = totalvalue['est_amount__sum']
    # print(totalAmonut,"#"*10)
    if totalAmonut_value == 0:
        totalAmonut = clientdetails.totalsum
        gsttotal = 0
        cgst = 0
    else :
        totalAmonut = totalAmonut_value
        gsttotal =totalAmonut*5/100
        cgst = gsttotal/2
    total = totalAmonut + gsttotal

    context={
        "is_estimate":True,
        "clientdetails":clientdetails,
        "details":details,
        "totalAmonut":totalAmonut,
        "gsttotal":gsttotal,
        "total":total,
        "cgst":cgst,
        "note":note
        
        }

    return render(request,'viewinvoicebill.html',context)


def savenotenew(request,id):
    discount=request.GET['discount']  
    eid= Estimates.objects.get(id=id)
    if Preview.objects.exists():
        est = Preview.objects.last().id
        est_id = 'INV'+str(1001+est)
    else:
        est=0
        est_id = 'INV'+str(1001+est)

    clientdetails = Estimates.objects.select_related('clientd').get(id=id)    
    preview =Preview(estimateId=eid, discount=discount,prviewnumber=est_id)
    preview.save()
    details = EstimateProduct.objects.filter(estimateid=id)
    eid= Estimates.objects.get(id=id)
    billing = PaymentDetails.objects.select_related('clientid','bankid','estimateId').filter(estimateId=eid).last()
    termandnote =Terms.objects.filter(estimateid=id).last()

    estid= EstimateProduct.objects.filter(estimateid=id)
    totalvalue=estid.aggregate(Sum('est_amount'))
    totalAmonut = totalvalue['est_amount__sum']
    if totalAmonut == 0:
        gsttotal = 0
        total = int(eid.totalsum)
    else :
        gsttotal =totalAmonut*5/100
        # sgst = (totalAmonut*5/100)/2
        total = totalAmonut + gsttotal
    grandtotal = total-int(discount)
    addincome = Income(estimateId=eid,incomestatus='Income',incomeamount=grandtotal)
    addincome.save()
    
    preview = Preview.objects.filter(estimateId=eid).last()
    cgst =gsttotal/2
    context={
        "is_invoice":True,
        'billing':billing,
        "details":details,
        "totalAmonut":totalAmonut,
        "gsttotal":gsttotal,
        "discount":discount,
        "grandtotal":grandtotal,
        "termandnote":termandnote,
        "eid":eid,
        "preview":preview,
        "cgst":cgst,
        "clientdetails":clientdetails
        }
    return render(request,'savenotenew.html',context)



def stockbill(request,id):
    estid = Estimates.objects.get(id=id)
    stockdetails=StockDetails.objects.filter(estimate=estid)
    clientdetails = Estimates.objects.select_related('clientd').get(id=id)
    totalvalue=stockdetails.aggregate(Sum('grandtotal'))
    totalAmonut = totalvalue['grandtotal__sum']
    context={
        "stockdetails":stockdetails,
        "totalAmonut":totalAmonut,
        "clientdetails":clientdetails
        }

    return render (request,'stockbill.html',context)    

def billsaved(request,id):
    estid = Estimates.objects.get(id=id)
    previewlist = Preview.objects.filter(estimateId=estid).last()
    print(previewlist.discount)
    clientdetails = Estimates.objects.select_related('clientd').get(id=id)
    details = EstimateProduct.objects.filter(estimateid=id)
    estid= EstimateProduct.objects.filter(estimateid=id)
    note = Terms.objects.filter(estimateid=id).last()
    totalvalue=estid.aggregate(Sum('est_amount'))
    totalAmonut = totalvalue['est_amount__sum']
    gsttotal =totalAmonut*5/100
    cgst = gsttotal/2
    discount = previewlist.discount
    subtotal = totalAmonut + gsttotal
    total =subtotal - discount
    

    print(previewlist)
    context={
       "previewlist":previewlist,
       "clientdetails":clientdetails,
        "details":details,
        "totalAmonut":totalAmonut,
        "gsttotal":gsttotal,
        "total":total,
        "cgst":cgst,
        "discount":discount
        }

    return render (request,'billsaved.html',context)  





def itemsearch(request):
    item = request.GET['itemname']
    item_ex = Stock.objects.filter(stockname = item).exists()
    if item_ex:
        item_details = Stock.objects.get(stockname = item)
        # date = datetime.now()
        print(type(item_details.price))
        print(type(item_details.quantity))
        data = {
            'item':item_details.category.cat_name,
            'rentalprice':item_details.price,
            'max_qty':item_details.quantity,          
        }
     
        return JsonResponse(data)    




@csrf_exempt
def bill_adding(request):
    invid = request.POST['estimateid']
    item = request.POST['item']
    qty = request.POST['qty']
    print(invid,item,qty)

    inv_obj = Estimates.objects.get(id=invid)
    print(inv_obj)
      
    itemname = Stock.objects.get(stockname=item)
    print(itemname)
    
    taken = Items(estimate=inv_obj, stock=itemname, taken=qty,status="not returned")
    taken.save()
    added_qty = Stock.objects.get(stockname=item)
    added_qty.quantity = added_qty.quantity -int(qty)
    added_qty.save()
    return JsonResponse({'msg':'Genegrated'})        