from django.forms import ModelForm, DateInput
from home.models import Reservation
from tickets.models import Orderstable, Itemtable
from .models import Complaint, Customer
from django import forms


class TimeInput(forms.TimeInput):
    input_type = "time"

class DateInput(forms.DateInput):
    input_type="date"

class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['table','guestCount','date','time']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time'].widget = TimeInput()
        self.fields['date'].widget = DateInput()

class OrderForm(ModelForm):
    class Meta:
        model = Orderstable
        fields = ['ordertype', 'tablenumber']


class ItemtableForm(ModelForm):
    class Meta:
        model = Itemtable
        fields = ['menuitem','quantity','specialinstructions','allergies']


class ComplaintForm(ModelForm):
    class Meta:
        model = Complaint
        fields = ['message', 'in_restaurant']

    message = forms.CharField(widget=forms.Textarea(attrs={"rows":5,"cols":20}))

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['user_name','first_name','email','last_name', 'street_address','city','country']



