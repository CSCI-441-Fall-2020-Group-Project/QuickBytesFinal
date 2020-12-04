from django import forms
from django.forms import ModelForm, Textarea, DateTimeInput
from django.contrib.admin.widgets import AdminDateWidget

'''
  // written by: Patrick Carra
  // tested by: Patrick Carra
  // debugged by: Patrick Carra
  // etc.
'''

from manager.models import Worker_Complaint
from tickets.models import Orderstable


#Form to log a complaint
class Worker_Complaint_Form(ModelForm):
    class Meta:
        model = Worker_Complaint
        fields = ('complaint',)
        widgets = {'complaint': Textarea(attrs={'rows': 4}),}

#Form to add an order
class addOrderForm(ModelForm):
    class Meta:
        model = Orderstable
        fields = ('customername', 'ordertype', 'requestedtime')
        widgets = {'requetedtime': DateTimeInput(format='%m/%d/%y %H:%M', attrs={'type': 'datetime'}),}

#Form to edit an Order        
class editOrderForm(ModelForm):
    class Meta:
        model = Orderstable
        fields = ('customername', 'ordertype', 'requestedtime')
        widgets = {'requetedtime': DateTimeInput(format='%m/%d/%y %H:%M', attrs={'type': 'datetime'}),}
