'''
  // written by: Patrick Carra, Clint Ryan
  // tested by: Patrick Carra
  // debugged by: Patrick Carra
  // etc.
'''

from django.db import models
from django.urls import reverse

from menu.models import Menu_Item
from home.models import tableTable
from customer.models import Customer

# Create your models here.
class Orderstable(models.Model):
    order_type = [
            ('dine-in', 'dine-in'),
            ('carryout', 'carryout'),
            ('delivery', 'delivery'),
            ]   
    status = [
            ('needDrinks', 'Needs Drinks'),
            ('needToOrder', 'Needs to Order'),
            ('orderTaken', 'Order Taken'),
            ('sentToKitchen', 'Sent To Kitchen'),
            ('sentBacktoServer', 'Sent to Server'),
            ('orderCompleted', 'Order Completed'),
            ('delivered', 'Delivered'),
            ]
    #customername = models.CharField(max_length=255)
    BOOL_CHOICES = ((True, 'Paid'),(False,'Not_Paid'))

    customername = models.ForeignKey(Customer, on_delete=models.CASCADE, to_field='id', db_column='customername')
    ordertype = models.CharField(max_length=10, choices=order_type, default='dine-in')
    status = models.CharField(null=True, blank=True, max_length=255, choices=status, default='orderTaken')
    timeordered = models.DateTimeField(auto_now=True, null=True, blank=True)
    timecompleted = models.DateTimeField(auto_now=False, null=True, blank=True)
    tablenumber = models.ForeignKey(tableTable, on_delete=models.CASCADE, to_field='id', db_column='tablenumber', null=True, blank=True)
    total = models.DecimalField(max_digits = 7, decimal_places=2, default=0.0,null=True, blank=True)
    message = models.CharField(max_length=255, null=True, blank=True)
    paid = models.BooleanField(choices=BOOL_CHOICES, default=False)
    requestedtime = models.DateTimeField(auto_now=False, null=True, blank=True)



    def __str__(self):
        return str(self.id) + " - " + self.ordertype 



class Itemtable(models.Model):
    menuItem = [
            ('',''),
            ]
    status = [
            ('waiting', 'waiting'),
            ('preparing', 'preparing'),
            ('completed', 'completed'),
            ('delivered', 'delivered'),
            ]
    
    ordernumber = models.ForeignKey(Orderstable, on_delete=models.CASCADE, to_field='id', db_column='ordernumber')
    menuitem = models.ForeignKey(Menu_Item, on_delete=models.CASCADE, to_field='id', db_column='menuitem', default=1)
    specialinstructions = models.CharField(max_length=255, blank=True, null=True)
    allergies = models.CharField(max_length=255, blank=True, null=True)
    server = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, choices=status, blank=True, null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.ordernumber) + " - " + str(self.menuitem)

class Alertstable(models.Model):
        sender = models.CharField(max_length=10)
        receiver = models.CharField(max_length=10)
        message = models.CharField(max_length=50)
        time = models.TimeField(auto_now_add=True)
        priority = models.BooleanField(default=False)

        def __str__(self):
                return str(self.message) + " : " + str(self.sender) + " " + str(self.time)