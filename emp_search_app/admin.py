from django.contrib import admin
from .models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['fname','lname','age','address','photo']

admin.site.register(Employee,EmployeeAdmin)