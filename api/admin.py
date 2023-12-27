from django.contrib import admin
from api.models import company,Employee

# Register your models here.
class companyadmin(admin.ModelAdmin):
    list_display=('name','location','type')
    search_fields=('name',)


class Employeeadmin(admin.ModelAdmin):
    list_display=('name','email','address','phone')
    list_filter=('company',)

admin.site.register(company,companyadmin)
admin.site.register(Employee,Employeeadmin)
