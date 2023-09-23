from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Store, Product, Inventory, Customer, Sale, Receipt

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'contact_details']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['store', 'product', 'quantity', 'restock_threshold']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact', 'loyalty_status']

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['store', 'customer', 'product', 'quantity', 'total_price', 'date']

@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_amount', 'date']

