'''
  // written by: Kegan Ronholt
  // tested by: Kegan Ronholt
  // debugged by: Kegan Ronholt
'''

from django.contrib import admin
from . models import tableTable, Reservation

# Register your models here
admin.site.register(tableTable)
admin.site.register(Reservation)

