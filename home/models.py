'''
  // written by: Patrick Carra 
  // tested by: Patrick Carra 
  // debugged by: Patrick Carra 
'''

from django.db import models
from django import forms
from datetime import datetime
from customer.models import Customer



class Reservation(models.Model):
        table = models.ForeignKey('tableTable', on_delete=models.CASCADE)
        customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
        guestCount = models.IntegerField(default=1)
        #date = models.DateTimeField(default=datetime.now, blank=True)
        date = models.DateField(null=True, blank=True, auto_now=False)
        time = models.TimeField(null=True, blank=True, auto_now=False, auto_now_add=False)


        
        


# Create your models here.
class tableTable(models.Model):
    tableTypeChoices = [
            ('bar', 'bar'),
            ('booth', 'booth'),
            ('table', 'table'),
            ('hi-top', 'hi-top'),
            ('patio', 'patio'),
            ]

    statusChoices = [
            ('available', 'available'),
            ('occupied', 'occupied'),
            ('closed', 'closed'),
            ('reserved', 'reserved'),
            ]
    #primary key field
    
    tableName = models.CharField(max_length=10, default="A1" )
    seats = models.IntegerField()
    tableType = models.CharField(max_length=255, choices=tableTypeChoices)
    status = models.CharField(max_length=255, choices=statusChoices)
    server = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return '%s - %s - Seats: %s' % (self.tableName, self.tableType, self.seats )
