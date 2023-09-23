from django import forms
from .models import Store, Customer, Product, Inventory, Sale, Receipt

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'location', 'contact_details']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['store', 'quantity', 'restock_threshold']



class ProcessSaleForm(forms.ModelForm):
    store = forms.ModelChoiceField(queryset=Store.objects.all())
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    quantity = forms.IntegerField(min_value=1)

    class Meta:
        model = Sale
        fields = ['store', 'customer', 'product', 'quantity']

    def clean(self):
        cleaned_data = super().clean()
        store = cleaned_data.get('store')
        product = cleaned_data.get('product')
        quantity = cleaned_data.get('quantity')

        inventory = Inventory.objects.get(store=store, product=product)
        if inventory.quantity < quantity:
            raise forms.ValidationError(f'Not enough stock available in {store.name}. Only {inventory.quantity} left.')

        return cleaned_data
    


class ReceiptForm(forms.ModelForm):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), required=False)
    sales = forms.ModelMultipleChoiceField(queryset=Sale.objects.all())

    class Meta:
        model = Receipt
        fields = ['customer', 'sales']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'contact', 'loyalty_status']

class LoyaltyForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'loyalty_status']

        


