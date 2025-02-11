from django.contrib import admin
from .models import Customer

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'address') 
    search_fields = ('name', 'phone') 
    list_filter = ('id', 'name') 