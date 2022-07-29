from django.contrib import admin
from .models import *
# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_name', 'employee_phone', 'employee_district')
    search_fields=('employee_name',)
admin.site.register(Employee,EmployeeAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_id', 'client_phone')
    search_fields=('client_name',)
admin.site.register(Client,ClientAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('food_name',)
    search_fields=('food_name',)
admin.site.register(Product,ProductAdmin)


class AddBankAdmin(admin.ModelAdmin):
    list_display = ('bank_name',)
    search_fields=('bank_name',)
admin.site.register(AddBank,AddBankAdmin)



class EstimatesAdmin(admin.ModelAdmin):
    list_display = ('est_fromdate',)
    search_fields=('est_fromdate',)
admin.site.register(Estimates,EstimatesAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    search_fields=('category',)
admin.site.register(Category,CategoryAdmin)



class EstimateProductAdmin(admin.ModelAdmin):
    list_display = ('est_category',)
    search_fields=('est_category',)
admin.site.register(EstimateProduct,EstimateProductAdmin)





class PaymentDetailsAdmin(admin.ModelAdmin):
    list_display = ('paymentdate',)
    search_fields=('paymentdate',)
admin.site.register(PaymentDetails,PaymentDetailsAdmin)





class ExpencesAdmin(admin.ModelAdmin):
    list_display = ('expencesasamount',)
    search_fields=('expencesasamount',)
admin.site.register(Expences,ExpencesAdmin)






class TermsAdmin(admin.ModelAdmin):
    list_display = ('term',)
    search_fields=('term',)
admin.site.register(Terms,TermsAdmin)


class IncomeAdmin(admin.ModelAdmin):
    list_display = ('incomeamount',)
    search_fields=('incomeamount',)
admin.site.register(Income,IncomeAdmin)


class PreviewAdmin(admin.ModelAdmin):
    list_display = ('prviewnumber',)
    search_fields=('prviewnumber',)
admin.site.register(Preview,PreviewAdmin)




class StockAdmin(admin.ModelAdmin):
    list_display = ('stockname',)
    search_fields=('stockname',)
admin.site.register(Stock,StockAdmin)



class ItemsAdmin(admin.ModelAdmin):
    list_display = ('taken',)
    search_fields=('taken',)
admin.site.register(Items,ItemsAdmin)



class StockCatagoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name',)
    search_fields=('cat_name',)
admin.site.register(StockCatagory,StockCatagoryAdmin)



class StockDetailsAdmin(admin.ModelAdmin):
    list_display = ('estimate',)
    search_fields=('estimate',)
admin.site.register(StockDetails,StockDetailsAdmin)







