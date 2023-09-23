from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('store_management/', views.store_management, name='store_management'),
    path('add_store/', views.add_store, name='add_store'),
    path('update_store/<int:store_id>/', views.update_store, name='update_store'),
    path('delete_store/<int:store_id>/', views.delete_store, name='delete_store'),
    path('store_list/', views.store_list, name='store_list'),
    path('inventory_management/', views.inventory_interface, name='inventory_interface'),
    path('inventory/list/', views.inventory_list, name='inventory_list'),
    path('add_inventory/', views.add_inventory, name='add_inventory'),
    path('update_inventory/<int:inventory_id>/', views.update_inventory, name='update_inventory'),
    path('delete_inventory/<int:inventory_id>/', views.delete_inventory, name='delete_inventory'),
    path('sales_management/', views.sales_interface, name='sales_interface'),
    path('sales/process/', views.process_sales, name='process_sales'),
    path('generate_receipt/', views.generate_receipt, name='generate_receipt'),
    path('sales-history/', views.sales_history, name='sales_history'),
    path('customer_management/', views.customer_management, name='customer_management'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('view_customers/', views.view_customers, name='view_customers'),
    path('loyalty_program/', views.loyalty_program, name='loyalty_program'),
    path('customer_purchase_history/<int:customer_id>/', views.customer_purchase_history, name='customer_purchase_history'),
]
