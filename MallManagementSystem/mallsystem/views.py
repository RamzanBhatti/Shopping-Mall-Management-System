

from django.shortcuts import render, redirect, get_object_or_404
from .models import Store
from .forms import StoreForm
from .models import Inventory,Sale,Customer,Product,Store
from .forms import InventoryForm, ProductForm, ReceiptForm,CustomerForm
from .forms import ProcessSaleForm,LoyaltyForm


def dashboard(request):
    return render(request, 'dashboard.html')

def store_management(request):
    stores = Store.objects.all()
    return render(request, 'Store/store_management.html', {'stores': stores})

def add_store(request):
    if request.method == "POST":
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store_management')
    else:
        form = StoreForm()
    return render(request, 'Store/add_store.html', {'form': form})

def update_store(request, store_id):
    store = Store.objects.get(pk=store_id)
    if request.method == "POST":
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect('store_management')
    else:
        form = StoreForm(instance=store)
    return render(request, 'Store/update_store.html', {'form': form})

def delete_store(request, store_id):
    store = Store.objects.get(pk=store_id)
    if request.method == "POST":
        store.delete()
        return redirect('store_management')
    return render(request, 'Store/delete_store.html', {'store': store})

def store_list(request):
    stores = Store.objects.all()
    return render(request, 'Store/store_list.html', {'stores': stores})


def inventory_interface(request):
    return render(request, 'Inventory\inventory_management.html')

def inventory_list(request):
    inventories = Inventory.objects.all()
    context = {
        'inventories': inventories
    }
    return render(request, 'Inventory/inventory_list.html', context)



def add_inventory(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        inventory_form = InventoryForm(request.POST)
        
        if product_form.is_valid() and inventory_form.is_valid():
            product = product_form.save()
            
            inventory = inventory_form.save(commit=False)
            inventory.product = product
            inventory.save()
            
            return redirect('inventory_list')
    else:
        product_form = ProductForm()
        inventory_form = InventoryForm()
        
    context = {
        'product_form': product_form,
        'inventory_form': inventory_form
    }
    return render(request, 'Inventory/add_inventory.html', context)




def update_inventory(request, inventory_id):
    inventory = get_object_or_404(Inventory, pk=inventory_id)
    product = inventory.product

    if request.method == 'POST':
        product_form = ProductForm(request.POST, instance=product)
        inventory_form = InventoryForm(request.POST, instance=inventory)
        
        if product_form.is_valid() and inventory_form.is_valid():
            product_form.save()
            inventory_form.save()
            return redirect('inventory_list')  # or whatever your list view's name/url is

    else:
        product_form = ProductForm(instance=product)
        inventory_form = InventoryForm(instance=inventory)

    context = {
        'product_form': product_form,
        'inventory_form': inventory_form
    }

    return render(request, 'Inventory/update_inventory.html', context)

def delete_inventory(request, inventory_id):
    inventory = get_object_or_404(Inventory, pk=inventory_id)

    if request.method == 'POST':
        inventory.delete()
        return redirect('inventory_list')  # or whatever your list view's name/url is

    return render(request, 'Inventory/delete_inventory.html')



def sales_interface(request):
    return render(request, 'Sales/sales_interface.html')


def process_sales(request):
    if request.method == 'POST':
        form = ProcessSaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.total_price = sale.product.price * sale.quantity
            sale.save()

            # Decrease inventory
            inventory = Inventory.objects.get(store=sale.store, product=sale.product)
            inventory.quantity -= sale.quantity
            inventory.save()

            return redirect('sales_interface')

    else:
        form = ProcessSaleForm()

    context = {
        'form': form
    }
    return render(request, 'Sales/process_sales.html', context)



def generate_receipt(request):
    if request.method == 'POST':
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(commit=False)
            total_amount = sum(sale.total_price for sale in form.cleaned_data['sales'])
            receipt.total_amount = total_amount
            receipt.save()
            form.save_m2m()  # Save many-to-many relationships
            return redirect('generate_receipt')  # You can redirect to any appropriate URL

    else:
        form = ReceiptForm()

    return render(request, 'Sales/generate_receipt.html', {'form': form})


def sales_history(request):
    sales = Sale.objects.all().order_by('-date')  # Orders the sales by date in descending order
    return render(request, 'Sales/sales_history.html', {'sales': sales})


def customer_management(request):
    return render(request, 'Customer/customer_management.html')

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_management')
    else:
        form = CustomerForm()

    context = {
        'form': form
    }

    return render(request, 'Customer/add_customer.html', context)

def view_customers(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers
    }
    return render(request, 'Customer/view_customer.html', context)

def loyalty_program(request):
    if request.method == 'POST':
        form = LoyaltyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_management')
    else:
        form = LoyaltyForm()
    
    context = {
        'form': form
    }
    return render(request, 'Customer/loyalty_program.html', context)

def customer_purchase_history(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    sales = Sale.objects.filter(customer=customer).order_by('-date')

    context = {
        'sales': sales
    }
    return render(request, 'Customer/customer_purchase_history.html', context)


