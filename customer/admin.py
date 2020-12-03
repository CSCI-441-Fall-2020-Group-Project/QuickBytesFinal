'''
  // written by: Kegan Ronholt
  // tested by: Kegan Ronholt
  // debugged by: Kegan Ronholt
'''

from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Complaint)
admin.site.register(Discount)