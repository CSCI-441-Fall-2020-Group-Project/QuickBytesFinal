from django.forms import ModelForm, Textarea
from django import forms

from .models import Budget_Table, Schedule_Table

class Budget_Table_Form(ModelForm):
    item_Note = forms.CharField(max_length=100, required=False)
    class Meta:
        model = Budget_Table 
        category = (
            ('Income', 'Income'),
            ('Expense', 'Expense'),
            ('Other', 'Other'),
        )
        select = forms.ChoiceField(required=True, choices=category)
        fields = ['item_Name', 'item_Category', 'item_Note', 'item_Date', 'item_Amount']
        widgets = {
            'item_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'item_Category': forms.Select(choices=category),
            'item_Note': forms.TextInput(attrs={'class': 'form-control'}),
            'item_Date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'item_Amount': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class Schedule_Table_Form(ModelForm):
    class Meta:
        model = Schedule_Table
        position = {
            ('Chef', 'Chef'),
            ('Server', 'Server'),
            ('Busser', 'Busser'),
            ('Manager', 'Manager'),
            ('Host', 'Host'),
            ('Delivery', 'Delivery'),
        }
        select = forms.ChoiceField(required=True, choices=position)
        fields = ['worker_Name', 'worker_Position', 'worker_Start', 'worker_End','worker_Date', 'worker_Break']
        widgets = {
            'worker_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'worker_Position': forms.Select(choices=position),
            'worker_Start': forms.TimeInput(),
            'worker_End': forms.TimeInput(),
            'worker_Date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'worker_Break': forms.TextInput(attrs={'class': 'form-control'}),
        }