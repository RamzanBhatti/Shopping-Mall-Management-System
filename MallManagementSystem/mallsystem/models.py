from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    contact_details = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Inventory(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="inventories")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="inventory_records")
    quantity = models.PositiveIntegerField()
    restock_threshold = models.PositiveIntegerField()  # When the stock reaches this number, it's time to restock

class Customer(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    LOYALTY_CHOICES = [
        ('silver', 'Silver'),
        ('gold', 'Gold'),
        ('platinum', 'Platinum'),
        ('none', 'None'),
    ]
    loyalty_status = models.CharField(max_length=10, choices=LOYALTY_CHOICES, default='none')

class Sale(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="sales")
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name="purchases")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sales")
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

class Receipt(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    sales = models.ManyToManyField(Sale)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
