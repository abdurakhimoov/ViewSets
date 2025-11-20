from django.contrib import admin
from .models import Company, Employee

@admin.register(Company)
class AdminCompany(admin.ModelAdmin):
    list_display = ['name', 'location']
    search_fields = ['name']


@admin.register(Employee)
class AdminEmployee(admin.ModelAdmin):
    list_display = ['name', 'company', 'email']
    search_fields = ['name', 'email']