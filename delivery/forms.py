from django.forms import ModelForm, Textarea

from manager.models import Worker_Complaint

class Worker_Complaint_Form(ModelForm):
    class Meta:
        model = Worker_Complaint
        fields = ('complaint',)
        widgets = {'complaint': Textarea(attrs={'rows': 4}),}
