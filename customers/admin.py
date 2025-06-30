from django.contrib import admin
from customers.models import Customer


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['name', 'cpf', 'phone', 'create_at']
    search_fields = ['name', 'cpf', 'phone']