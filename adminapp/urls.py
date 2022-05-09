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
    path('invoicedetails/<str:id>/',views.invoicedetails,name="invoicedetails"),
    path('bank',views.bank,name="bank"),
    path('products',views.products,name="products"),
    path('editestimate/<str:id>',views.editestimate,name="editestimate"),
    path('payment',views.payment,name="payment"),
    path('addpayment/<str:id>',views.addpayment,name="addpayment"),
    path('expenses',views.expenses,name="expenses"),
    path('addexpenses',views.addexpenses,name="addexpenses"),
    path('profit',views.profit,name="profit"),
    path('addprofit',views.addprofit,name="addprofit"),
    path('viewestimate/<str:id>',views.viewestimate,name="viewestimate"),
    path('editcustomer/<str:id>',views.editcustomer,name="editcustomer"),
    path('addestimate',views.addestimate,name="addestimate"),
    path('filter',views.filter,name="filter"),
    path('viewemployee/<str:id>',views.viewemployee,name="viewemployee"),
    path('viewcustomer/<str:id>',views.viewcustomer,name="viewcustomer"),
    path('addmstaff',views.addmstaff,name="addmstaff"),
    path('editstaff/<str:staff_id>',views.editstaff,name="editstaff"),
    # path('getproduct/',views.getproduct,name="getproduct"),
    path('getproductGet/<int:id>',views.getproductGet,name="getproductGet"),
    path('profitandloss',views.profitandloss,name="profitandloss"),
    path('netprofit/',views.netprofit,name="netprofit"),
    path('editProductdata/<int:id>',views.editProductdata,name="editProductdata"),
    path('updateproduct/',views.updateproduct,name="updateproduct"),
    path('delete/<str:id>',views.delete,name="delete"),
    path('deletestaff/<str:id>',views.deletestaff,name="deletestaff"),
    path('deletecustomer/<str:id>',views.deletecustomer,name="deletecustomer"),
    path('addcat',views.addcat,name="addcat"),
    path('bill',views.bill,name="bill"),
    path('checkexist',views.checkexist,name="checkexist"),
    path('est_product',views.est_product,name="est_product"),
    path('est_productupdate',views.est_productupdate,name="est_productupdate"),
    path('createestimate',views.createestimate,name="createestimate"),
    path('invoicebill/<str:id>',views.invoicebill,name="invoicebill"),

    path('Delectestimate/<str:id>',views.Delectestimate,name="Delectestimate"),


    path('indexbill/<str:id>',views.indexbill,name="indexbill"),
    path('indexadvanced/<str:id>',views.indexadvanced,name="indexadvanced"),
    path('indexpartialy/<str:id>',views.indexpartialy,name="indexpartialy"),
    path('indexclosed/<str:id>',views.indexclosed,name="indexclosed"),


    path('invoicegetdata',views.invoicegetdata,name="invoicegetdata"),

    path('savenote',views.savenote,name="savenote"),

    path('login',views.login,name="login"),
    path('admin_logout',views.admin_logout,name="admin_logout"),
    # path('worker_logout',views.worker_logout,name="worker_logout"),
    path('forget',views.forget,name="forget"),
    

    path('printlist',views.printlist,name="printlist"),
    
    path('viewpdf/<str:id>,<str:discount>',views.viewpdf,name="viewpdf"),
    
    # path('formesmimate',views.formesmimate,name="formesmimate"),
    # path('estimatedetailsadd',views.estimatedetailsadd,name="estimatedetailsadd"),


    

    path('demo',views.demo,name="demo"),


    
   
]