from django.forms import ModelForm, Textarea
from tickets.models import Orderstable, Itemtable, Alertstable
from django import forms 

class OrderForm(ModelForm):
    class Meta:
        model = Orderstable
        fields = ['customername','ordertype','tablenumber']

class ItemtableForm(ModelForm):
    class Meta:
        model = Itemtable
        fields = ['menuitem','quantity','specialinstructions','allergies']

class AlertstableForm(ModelForm):
    class Meta:
        model = Alertstable
        fields = ['sender', 'receiver', 'message', 'priority']