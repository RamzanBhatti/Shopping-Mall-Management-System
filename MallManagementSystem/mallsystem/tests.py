
# Create your tests here.
from django.test import TestCase
from .models import Product

class ProductTestCase(TestCase):
    def test_product_creation(self):
        product = Product.objects.create(name="Test Product", description="This is a test product.", price=10.00)
        self.assertIsInstance(product, Product)
        self.assertEqual(product.name, "Test Product")



from django.test import TestCase
from .models import Product, Sale, Customer, Store

class SaleTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Test Product", description="This is a test product.", price=10.00)
        self.customer = Customer.objects.create(name="John Doe", contact="1234567890")
        self.store = Store.objects.create(name="Test Store", location="Test Location", contact_details="1234567890")

    def test_sale_creation(self):
        sale = Sale.objects.create(store=self.store, customer=self.customer, product=self.product, quantity=1, total_price=10.00)
        self.assertIsInstance(sale, Sale)
        self.assertEqual(sale.total_price, 10.00)

from django.test import TestCase
from .models import Product, Inventory, Store

class InventoryIntegrationTestCase(TestCase):
    def setUp(self):
        self.store = Store.objects.create(name="Test Store", location="Test Location", contact_details="1234567890")
        self.product = Product.objects.create(name="Test Product", description="This is a test product.", price=10.00)
    
    def test_product_addition_and_stock_update(self):
        # Add product to inventory
        inventory = Inventory.objects.create(store=self.store, product=self.product, quantity=10, restock_threshold=5)
        self.assertEqual(inventory.quantity, 10)

        # Update stock
        inventory.quantity -= 2
        inventory.save()
        self.assertEqual(inventory.quantity, 8)

class CustomerLoyaltyIntegrationTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name="John Doe", contact="1234567890", loyalty_status='none')
    
    def test_loyalty_program_assignment(self):
        self.customer.loyalty_status = 'silver'
        self.customer.save()
        self.assertEqual(self.customer.loyalty_status, 'silver')

from django.urls import reverse
from django.test import Client

class DashboardTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_dashboard_access(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
