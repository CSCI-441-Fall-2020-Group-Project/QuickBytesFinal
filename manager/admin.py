from django.contrib import admin
from . models import Worker_Complaint, Customer_Complaint,  Budget_Table, Schedule_Table

# Register your models here.
admin.site.register(Worker_Complaint)
admin.site.register(Customer_Complaint)
admin.site.register(Budget_Table) 
admin.site.register(Schedule_Table) 