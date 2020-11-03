from django.test import TestCase, Client
from tickets.models import Orderstable
from customer.models import Customer
from . views import sendToKitchen, addCustomerOrder

# Create your tests here
class listTest(TestCase):
    def test_list(self):
        client = Client()
        response = client.get('/delivery/dashboard')
        self.assertEqual(response.status_code, 200)

class sendToKitchen(TestCase):    
    def setup(self):
        customer=Customer.objects.create(user_name='Test')
        Orderstable.objects.create(customername=customer, ordertype='dine-in')

    def test_stk(self):
        order = Orderstable.objects.get(customername__Customer__user_name=='Test')
        order = order.sendToKitchen(order.id)
        order.assertEqual(order.status, 'sentToKitchen')
