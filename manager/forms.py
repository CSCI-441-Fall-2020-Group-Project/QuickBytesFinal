from django.forms import ModelForm, Textarea
from django import forms 
from .models import Budget_Table, Schedule_Table, Employee_Table, Restock_Table
from customer.models import Customer, Discount
'''
  // written by: Mark Norfolk
  // tested by: Mark Norfolk
  // debugged by: Mark Norfolk
  // etc.
'''
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
    worker_Name = forms.ModelChoiceField(queryset=Employee_Table.objects.all().values_list('employee_Name', flat=True), to_field_name='employee_Name', required=False)
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
            # 'worker_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'worker_Position': forms.Select(choices=position),
            'worker_Start': forms.TimeInput(),
            'worker_End': forms.TimeInput(),
            'worker_Date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'worker_Break': forms.TextInput(attrs={'class': 'form-control'}),
        }

class Discount_Form(ModelForm):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), required=True)
    discount_percentage = forms.IntegerField(required=True)
    reason = forms.CharField(max_length = 250, required=False)
    class Meta:
        model = Discount
        fields = ['customer', 'discount_percentage', 'reason']

class Employee_Table_Form(ModelForm):
    class Meta:
        model = Employee_Table
        position = {
            ('Chef', 'Chef'),
            ('Server', 'Server'),
            ('Busser', 'Busser'),
            ('Manager', 'Manager'),
            ('Host', 'Host'),
            ('Delivery', 'Delivery'),
        }

        performance = {
            ('Great', 'Great'),
            ('Good', 'Good'),
            ('Average', 'Average'),
            ('Poor', 'Poor'),
            ('Abysmal', 'Abysmal'),
        }
        select1 = forms.ChoiceField(required=True, choices=position)
        select2 = forms.ChoiceField(required=True, choices=performance)
        fields = ['employee_Name', 'employee_Start', 'employee_Position', 'employee_Salary','employee_Performance', 'employee_Comment']
        widgets = {
            'employee_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'employee_Start': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'employee_Position': forms.Select(choices=position),
            'employee_Salary' : forms.TextInput(attrs={'class': 'form-control'}), 
            'employee_Performance': forms.Select(choices=performance),
            'employee_Comment': forms.Textarea(),
        }

class Restock_Table_Form(ModelForm):
    class Meta:
        model = Restock_Table
        restock = {
            ('Utensils', 'Utensils'),
            ('Ingredients', 'Ingredients'),
            ('Equipment', 'Equipment'),
        }
        select3 = forms.ChoiceField(required=True, choices=restock)
        fields = ['restock_option', 'restock_date']
        widgets = {
            'restock_option': forms.Select(choices=restock),
            'restock_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }