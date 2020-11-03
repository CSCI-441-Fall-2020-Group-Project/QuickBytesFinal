from django.test import TestCase
from . models import Orderstable, Itemtable
from customer.models import Customer

# Create your tests here.
class Order(TestCase):
    def setup(self):
        customer=Customer.objects.create(user_name='Test')
        Orderstable.objects.create(customername=customer, ordertype='dine-in')

    def test_order_created(self):
        testOrder = Orderstable.objects.get(customername=1)
        self.assertEqual(testOrder.customername, customer)

class Item(TestCase):
    def setup(self):
        Itemtable.objects.create(ordernumber=1, menuitem='Burger')

    def test_item_created(self):
        testItem = Itemtable.objects.get(ordernumber=1, menuitem='Burger')
        self.assertEqual(testItem.menuitem.name, 'Burger')
