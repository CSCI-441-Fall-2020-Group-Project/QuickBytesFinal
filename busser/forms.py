'''
  // written by: Mila Hose
  // tested by: Mila Hose
  // debugged by: Mila Hose
  // etc.
'''

from django.forms import ModelForm, Textarea
from manager.models import Worker_Complaint
from busser.models import Busser_Supplies_Requests, Table_Status

class Worker_Complaint_Form(ModelForm):
    class Meta:
        model = Worker_Complaint
        fields = ('complaint',)
        widgets = {'complaint': Textarea(attrs={'rows': 4}),}

class Busser_Supplies_Form(ModelForm):
    class Meta:
        model = Busser_Supplies_Requests
        fields = ['name', 'spray_bottle', 'sanitizing_cloth', 'carrying_tray']

class Table_Status_Form(ModelForm):
    class Meta:
        model = Table_Status
        fields = ['server', 'table', 'section', 'seats', 'status']
