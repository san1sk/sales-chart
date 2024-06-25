from django.contrib import admin
from .models import salesData
# Register your models here.

@admin.register(salesData)
class SalesDataAdmin(admin.ModelAdmin):
    list_display = ('saleDate', 'amount')
    list_filter = ('saleDate',)
    search_fields = ('saleDate', 'amount')
