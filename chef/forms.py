'''
  // written by: Patrick Carra
  // tested by: Patrick Carra
  // debugged by: Patrick Carra
  // etc.
'''

from django.forms import ModelForm, Textarea
from manager.models import Worker_Complaint
from tickets.models import Orderstable

class SendBackForm(ModelForm):
    class Meta:
        model = Orderstable
        fields = ('message',)
        widgets = {'message': Textarea(attrs={'rows': 4}),}

class Worker_Complaint_Form(ModelForm):
    class Meta:
        model = Worker_Complaint
        fields = ('complaint',)
        widgets = {'complaint': Textarea(attrs={'rows': 4}),}
