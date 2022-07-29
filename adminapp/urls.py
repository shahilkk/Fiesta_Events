from django.urls import path
from . import views


app_name='userapp'

urlpatterns = [
    path('master',views.master,name="master"),
    path('index/',views.index,name="index"),
    path('customer/',views.customer,name="customer"),
    path('addcustomer/',views.addcustomer,name="addcustomer"),
    path('marketingstaff/',views.marketingstaff,name="marketingstaff"),
    path('estimate/',views.Estimate,name="estimate"),
    path('invoicegrid/',views.invoicegrid,name="invoicegrid"),
    path('invoiceList/',views.invoiceList,name="invoiceList"),
    path('editinvoice/',views.editinvoice,name="editinvoice"),
    path('addinvoice/',views.addinvoice,name="addinvoice"),
    path('invoicedetails/<str:id>/',views.invoicedetails,name="invoicedetails"),
    path('bank/',views.bank,name="bank"),
    path('products/',views.products,name="products"),
    path('editestimate/<str:id>',views.editestimate,name="editestimate"),
    path('payment/',views.payment,name="payment"),
    path('addpayment/<str:id>',views.addpayment,name="addpayment"),
    path('expenses/',views.expenses,name="expenses"),
    path('addexpenses/',views.addexpenses,name="addexpenses"),
    path('profit/',views.profit,name="profit"),
    path('addprofit/',views.addprofit,name="addprofit"),
    path('viewestimate/<str:id>',views.viewestimate,name="viewestimate"),
    path('editcustomer/<str:id>',views.editcustomer,name="editcustomer"),
    path('addestimate/',views.addestimate,name="addestimate"),
    path('filter/',views.filter,name="filter"),
    path('viewemployee/<str:id>',views.viewemployee,name="viewemployee"),
    path('viewcustomer/<str:id>',views.viewcustomer,name="viewcustomer"),
    path('addmstaff/',views.addmstaff,name="addmstaff"),
    path('editstaff/<str:staff_id>',views.editstaff,name="editstaff"),
    # path('getproduct/',views.getproduct,name="getproduct"),
    path('getproductGet/<int:id>',views.getproductGet,name="getproductGet"),
    path('profitandloss/',views.profitandloss,name="profitandloss"),
    path('netprofit/',views.netprofit,name="netprofit"),
    path('editProductdata/<int:id>/',views.editProductdata,name="editProductdata"),
    path('updateproduct/',views.updateproduct,name="updateproduct"),
    path('delete/<str:id>/',views.delete,name="delete"),
    path('deletestaff/<str:id>/',views.deletestaff,name="deletestaff"),
    path('deletecustomer/<str:id>/',views.deletecustomer,name="deletecustomer"),
    path('addcat',views.addcat,name="addcat"),
    path('bill',views.bill,name="bill"),
    path('billitem',views.billitem,name="billitem"),
    path('checkexist',views.checkexist,name="checkexist"),
    path('est_product',views.est_product,name="est_product"),
    path('est_productupdate',views.est_productupdate,name="est_productupdate"),
    path('deletedata',views.deletedata,name="deletedata"),
    path('createestimate/',views.createestimate,name="createestimate"),
    path('invoicebill/<str:id>/',views.invoicebill,name="invoicebill"),

    path('Delectestimate/<str:id>/',views.Delectestimate,name="Delectestimate"),


    path('indexbill/<str:id>/',views.indexbill,name="indexbill"),
    path('indexadvanced/<str:id>/',views.indexadvanced,name="indexadvanced"),
    path('indexpartialy/<str:id>/',views.indexpartialy,name="indexpartialy"),
    path('indexclosed/<str:id>/',views.indexclosed,name="indexclosed"),


    path('invoicegetdata',views.invoicegetdata,name="invoicegetdata"),
    path('clientnamegetdata',views.clientnamegetdata,name="clientnamegetdata"),

    path('savenote',views.savenote,name="savenote"),

    path('save/<str:id>/',views.save,name="save"),
    path('savenotenew/<str:id>/',views.savenotenew,name="savenotenew"),

    path('',views.login,name="login"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    # path('worker_logout',views.worker_logout,name="worker_logout"),
    path('forget/',views.forget,name="forget"),
    

    path('phoneexist',views.phoneexist,name="phoneexist"),
    path('rentoutlist/',views.rentoutlist,name="rentoutlist"),

    path('savecustomer/',views.savecustomer,name="savecustomer"),
    path('estimatedata/',views.estimatedata,name="estimatedata"),


    path('returningitems',views.returningitems,name="returningitems"),
    path('stockbill/<str:id>',views.stockbill,name="stockbill"),
    

    # path('printlist',views.printlist,name="printlist"),
    

    path('printlist/',views.printlist,name="printlist"),
    path('deleteprintlist/<str:id>',views.deleteprintlist,name="deleteprintlist"),
    path('stock/',views.stock,name="stock"),
    path('addstock/',views.addstock,name="addstock"),
    path('editstock/<str:id>',views.editstock,name="editstock"),

    path('addmaterial/<str:id>',views.addmaterial,name="addmaterial"),
    path('getQunatity/',views.getQunatity,name="getQunatity"),
    path('valuesave',views.valuesave,name="valuesave"),
    path('viewaddedmaterial/<str:id>',views.viewaddedmaterial,name="viewaddedmaterial"),
    path('stocktransfer',views.stocktransfer,name="stocktransfer"),

    path('damage',views.damage,name="damage"),

    path('viewpdf/<str:id>,<str:discount>,<str:previewno>',views.viewpdf,name="viewpdf"),
    path('billsaved/<str:id>',views.billsaved,name="billsaved"),
    
    # path('formesmimate',views.formesmimate,name="formesmimate"),
    # path('estimatedetailsadd',views.estimatedetailsadd,name="estimatedetailsadd"),


    

    path('demo',views.demo,name="demo"),


    path('estmatenew/<str:id>',views.estmatenew,name="estmatenew"),
    path('invoicebillnew/<str:id>',views.invoicebillnew,name="invoicebillnew"),
    
   
]