'''
  // written by: Patrick Carra
  // tested by: Patrick Carra
  // debugged by: Patrick Carra
  // etc.
'''

from django.db import models
from django.urls import reverse

# Create your models here.

class Ingredients(models.Model):
    ingredient = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.ingredient)

class SupplyOrder(models.Model):
    status_choice = [
        ('On Order', 'On Order'),
        ('Ordered', 'Ordered'),
        ('Received', 'Received'),
    ]
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE, to_field='id', db_column='ingredient')
    order = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=status_choice, default='On Order')

    def __str__(self):
        return str(self.ingredient)
