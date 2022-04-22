from django.urls import path
from . import views


urlpatterns = [
    path('master',views.master,name="master"),
    path('index',views.index,name="index"),
    path('customer',views.customer,name="customer"),
    path('addcustomer',views.addcustomer,name="addcustomer"),
    path('marketingstaff',views.marketingstaff,name="marketingstaff"),
    path('estimate',views.Estimate,name="estimate"),
    path('invoicegrid',views.invoicegrid,name="invoicegrid"),
    path('invoiceList',views.invoiceList,name="invoiceList"),
    path('editinvoice',views.editinvoice,name="editinvoice"),
    path('addinvoice',views.addinvoice,name="addinvoice"),
    path('invoicedetails',views.invoicedetails,name="invoicedetails"),
    path('bank',views.bank,name="bank"),
    path('products',views.products,name="products"),
    path('editestimate',views.editestimate,name="editestimate"),
    path('payment',views.payment,name="payment"),
    path('addpayment',views.addpayment,name="addpayment"),
    path('expenses',views.expenses,name="expenses"),
    path('addexpenses',views.addexpenses,name="addexpenses"),
    path('profit',views.profit,name="profit"),
    path('addprofit',views.addprofit,name="addprofit"),
    path('viewestimate',views.viewestimate,name="viewestimate"),
    path('editcustomer',views.editcustomer,name="editcustomer"),
    path('addestimate',views.addestimate,name="addestimate"),
    path('filter',views.filter,name="filter"),
    path('viewcustomer',views.viewcustomer,name="viewcustomer"),
    path('addmstaff',views.addmstaff,name="addmstaff"),
    path('editstaff',views.editstaff,name="editstaff"),
    

    path('demo',views.demo,name="demo"),


    
   
]