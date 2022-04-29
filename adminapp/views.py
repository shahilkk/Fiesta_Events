
from http import client
from django.shortcuts import render , redirect 
from . models import Employee,Product,Client,AddBank,Category,EstimateProduct,Estimates,PaymentDetails
import random
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.db.models import Avg, Count, Min, Sum
# Create your views here.


def master(req):
    return render(req,'master.html')

def index(req):
    pending = Estimates.objects.filter(est_status ='Pending').all()
    billed = Estimates.objects.filter(est_status ='Billed').all()
    advanced = Estimates.objects.filter(est_status ='Advanced').all()
    paritialy = Estimates.objects.filter(est_status ='Partialy Paid').all()
    closed = Estimates.objects.filter(est_status ='Closed').all()
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
    return render(req,'index.html',context) 



def indexbill(request,id):
    Estimates.objects.filter(id=id).update(est_status ='Billed')
    return redirect('/user/index')

def indexadvanced(request,id):
    Estimates.objects.filter(id=id).update(est_status ='Advanced')
    return redirect('/user/index')

def indexpartialy(request,id):
    Estimates.objects.filter(id=id).update(est_status ='Partialy Paid')
    return redirect('/user/index')

def indexclosed(request,id):
    Estimates.objects.filter(id=id).update(est_status ='Closed')
    return redirect('/user/index')            






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
    # if Estimate.objects.exists():
    #     est = Estimate.objects.last().id
    #     est_id = 'EST'+int(10+est)
    # else:
    #     est=0
    #     est_id = 'EST'+int(10+est)
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
    estimates = Estimates.objects.all()
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
#         # print(getid)
#         return redirect('/user/addestimate/'+order_id)
       
#     else:
#         cust = Client.objects.all()
#         pro = Product.objects.all()
#         context={
#             "is_estimate":True,
#             'cust':cust,
#             'pro':pro
#             }
#     return render(request,'addestimate.html',locals())


def addestimate(request):
    
    cust = Client.objects.all()
    pro = Product.objects.all()

    if request.method=='POST':
        clientid=request.POST['checkname']
        print(clientid)
        
        fromdate=request.POST['dataform']
        todate=request.POST['todate']
        est_id = Client.objects.get(id=clientid)
        print(est_id)
        esti=Estimates(clientd=est_id,est_fromdate=fromdate, est_todate=todate)
        esti.save()
        order_id = esti.id
        context={
            "is_estimate":True,
            'cust':cust,
            'pro':pro,
            "estimate":esti
            }
        return render(request,'addestimate.html',context)
    # print(order_id)

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


def createestimate(request):
    cust = Client.objects.all()
    if request.method=='POST':
        clientid=request.POST['checkname']
        print(clientid)
        
        fromdate=request.POST['dataform']
        todate=request.POST['todate']
        est_id = Client.objects.get(id=clientid)
        print(est_id)
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


  



def addcat(request):
    if request.method=='POST':
        catagory_name=request.POST['catagory_name']
        obj= Category(category=catagory_name)
        obj.save()
        return redirect ('/user/products')


   

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


def addinvoice(request):

    context={
        "is_invoice":True,
    }
    return render(request,'addinvoice.html',context)


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
        addbank = AddBank(bank_name=bank_name, bank_holdername=bank_holdername, bank_accountname=bank_accountname, bank_ifsc=bank_ifsc, bank_branch=bank_branch, bank_balance=0)
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
        paymentclientbank = request.POST['paymentclientbank']
        paymentamount = request.POST['paymentamount']
        paymentestimateid = request.POST['paymentestimateid']
        paymentcompanybank = request.POST['paymentcompanybank']
        paymentclientid = request.POST['paymentclientid']
        
        # print(paymentcompanybank,paymentclientid,paymentestimateid,paymentdate,paymentclientname,paymentclientbank,paymentamount)
        clientID= Client.objects.get(id=paymentclientid)  
        bank=AddBank.objects.get(id=paymentcompanybank)
        estimate = Estimates.objects.get(id=paymentestimateid)
        payment = PaymentDetails(clientid=clientID,bankid=bank,estimateId=estimate,paymentdate=paymentdate,paymentamount=paymentamount,clientbank=paymentclientbank)
        payment.save()
        qunless =Estimates.objects.get(id=paymentestimateid)
        qunless.est_balance = qunless.est_balance-int(paymentamount)
        print(qunless.est_balance)
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
    alllist = Estimates.objects.all()
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
      


def profitandloss(req):
    context={
        "is_profitandloss":True
        }
    return render(req,'profit&loss.html',context)



   
def demo(request):
    return render(request,'demo/index.html')



   
def createestimate(request):
    cust = Client.objects.all()
    if request.method=='POST':
        clientid=request.POST['checkname']
        print(clientid)
        
        fromdate=request.POST['dataform']
        todate=request.POST['todate']
        est_id = Client.objects.get(id=clientid)
        print(est_id)
        esti=Estimates(clientd=est_id,est_fromdate=fromdate, est_todate=todate)
        esti.save() 
        return redirect('/user/createestimate') 


    context={
            "is_estimate":True,
            'cust':cust,
            
            }
    return render(request,'createestimate.html',context)    


@csrf_exempt
def bill (request):
    productname = request.POST['productname']
    # estimateid = request.POST['estimateid']
    print(productname)
    viewpro=Product.objects.get(food_name=productname)
    # estid=Estimates.objects.get(id=estimateid)
    data={
        
        # "food_name":viewpro.food_name,
        # "estimateid":estid.id,
        "id":viewpro.id,
        "catagory":viewpro.catagory,
        "priceper_head":viewpro.priceper_head,
        "priceper_kg":viewpro.priceper_kg,
        "food_deatails":viewpro.food_deatails
    }
    return JsonResponse({'product': data})


@csrf_exempt
def checkexist(request):
    print('worked')
    check_name = request.POST['checkname']
    object = Product.objects.filter(food_name=check_name).exists()
    print(object)
    print(check_name)
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
    print(estimateid)
    productId = request.POST['productId']
    est_category = request.POST['est_category']
    est_price = request.POST['est_price']
    est_amount = request.POST['est_amount']    
    est_qty = request.POST['est_qty']
    pr=Product.objects.get(id=productId)
    estim=Estimates.objects.get(id=estimateid)
    addest = EstimateProduct(estimateid=estim,productid=pr,est_category=est_category, est_price=est_price, est_amount=est_amount, est_qty=est_qty)
    addest.save()
    estid= EstimateProduct.objects.filter(estimateid=estimateid)
    totalvalue=estid.aggregate(Sum('est_amount'))
    totalAmonut = totalvalue['est_amount__sum']
    print(totalvalue)
    total=Estimates.objects.filter(id=estimateid).update(est_balance=totalAmonut)
    return JsonResponse({'msg':'data inserted sucess'})


@csrf_exempt
def invoicegetdata(request):
    clientphone = request.POST['clientphone']
    viewpro=Client.objects.get(client_phone=clientphone)
    estimatelist=[]
    print(viewpro.id)
    estID = Estimates.objects.filter(clientd=viewpro.id)
    print(estID)

    if estID.exists():
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
            print(value)



    # viewProduct = EstimateProduct.objects.filter(estimateid_id=estID.id).last()
    # print(viewProduct)
    # for i in viewProduct:
    #     print(i)
    data={
        
        
        "id":viewpro.id,
        "gst":viewpro.client_gst_number,
        "email":viewpro.client_email,
        "state":viewpro.client_state,
        "district":viewpro.client_district,
        "zipcode":viewpro.client_zipcode,
        "address":viewpro.client_address,
        "estimatelist":estimatelist
        
    }
    return JsonResponse({'details': data})   



def invoicebill(request,id):

    details = EstimateProduct.objects.filter(estimateid=id)
    print(details)
    context={
            "is_estimate":True,
            "details":details
            
            }
    return render(request,'invoicebill.html',context)