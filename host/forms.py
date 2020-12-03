'''
  // written by: Kegan Ronholt
  // tested by: Kegan Ronholt
  // debugged by: Kegan Ronholt
'''

from django.forms import ModelForm, Textarea
from tickets.models import Orderstable, Itemtable
from home.models import tableTable
from manager.models import Worker_Complaint
from home.models import Reservation
from .models import WaitList
from django import forms 




class WaitListForm(ModelForm):
    class Meta:
        model = WaitList
        fields = ('customer', 'guestCount')

        
class Worker_Complaint_Form(ModelForm):
    class Meta:
        model = Worker_Complaint
        fields = ('complaint',)
        widgets = {'complaint': Textarea(attrs={'rows': 4}),}


class TimeInput(forms.TimeInput):
    input_type = "time"

class DateInput(forms.DateInput):
    input_type="date"


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ('customer','table','guestCount','date','time')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time'].widget = TimeInput()
        self.fields['date'].widget = DateInput()

class OrderForm(ModelForm):
    class Meta:
        model = Orderstable
        fields = ['customername','ordertype','tablenumber']

class ItemtableForm(ModelForm):
    class Meta:
        model = Itemtable
        fields = ['menuitem','quantity','specialinstructions','allergies']