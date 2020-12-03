'''
  // written by: Kegan Ronholt
  // tested by: Kegan Ronholt
  // debugged by: Kegan Ronholt
'''

from django.db import models
from customer.models import Customer

# Create your models here.


class WaitList(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, to_field='id')
    timeadded = models.DateTimeField(auto_now=True)
    guestCount = models.IntegerField(default=1)
    