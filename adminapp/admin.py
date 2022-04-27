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






