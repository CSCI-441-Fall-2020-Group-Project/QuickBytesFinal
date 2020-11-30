from django import forms
from django.forms import ModelForm, Textarea, DateTimeInput
from django.contrib.admin.widgets import AdminDateWidget

from manager.models import Worker_Complaint
from tickets.models import Orderstable



class Worker_Complaint_Form(ModelForm):
    class Meta:
        model = Worker_Complaint
        fields = ('complaint',)
        widgets = {'complaint': Textarea(attrs={'rows': 4}),}

class addOrderForm(ModelForm):
    class Meta:
        model = Orderstable
        fields = ('customername', 'ordertype', 'requestedtime')
        widgets = {'requetedtime': DateTimeInput(format='%m/%d/%y %H:%M', attrs={'type': 'datetime'}),}
        
class editOrderForm(ModelForm):
    class Meta:
        model = Orderstable
        fields = ('customername', 'ordertype', 'requestedtime')
        widgets = {'requetedtime': DateTimeInput(format='%m/%d/%y %H:%M', attrs={'type': 'datetime'}),}
