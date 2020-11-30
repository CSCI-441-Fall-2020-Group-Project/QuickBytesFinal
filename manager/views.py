from django.shortcuts import render
from . models import Customer_Complaint, Worker_Complaint, Budget_Table, Schedule_Table, Employee_Table, Restock_Table
from customer.models import Complaint, Discount
from busser.models import Busser_Supplies_Requests
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView)
from django.shortcuts import redirect
from django.urls import reverse
from . forms import Budget_Table_Form, Schedule_Table_Form, Discount_Form, Employee_Table_Form, Restock_Table_Form
from django.views.generic.edit import CreateView

# Create your views here.
def dashboard(request):
    context = {'text': 'Manager Dashboard'}
    template = 'manager/managerIndex.html'
    return render(request, template, context) 

#Displays the worker and customer complaints from the database
def complaints(request):
    customer_comp = Complaint.objects.all()
    worker_comp = Worker_Complaint.objects.all()
    context = {
        'customer_complaints' : customer_comp,
        'worker_complaints' : worker_comp,
    }

    if (request.GET.get('DeleteButton')):
        Complaint.objects.filter(id = request.GET.get('DeleteButton')).delete()
        return redirect(request.path)
    elif (request.GET.get('DeleteButton2')):
        Worker_Complaint.objects.filter(id = request.GET.get('DeleteButton2')).delete()
        return redirect(request.path)

    template = 'manager/complaints.html'
    return render(request, template, context)

# class create(CreateView):
#     budget = Budget_Table.objects.all()
#     model=Budget_Table
#     template_name='manager/income.html'
#     form_class = Budget_Table_Form

#     def get_success_url(self):
#         return reverse('manager:income')

# def income(request):
#     form = Budget_Table_Form(request.POST)
#     budget = Budget_Table.objects.all()
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#         else: 
#             form = Budget_Table_Form()
        
#         context = {
#             'form': form,
#             'budget_table' : budget,
#         }
#         return render(request, 'manager/income.html', context)
#     else:
#         context = {
#             'form': form,
#             'budget_table' : budget,
#         }
#         return render(request, 'manager/income.html', context)


class income(CreateView):
    model = Budget_Table
    #fields = ['item_Name', 'item_Category', 'item_Note', 'item_Date', 'item_Amount']
    form_class = Budget_Table_Form

    def get_context_data(self, **kwargs):
        context = super(income, self).get_context_data(**kwargs)
        budget = Budget_Table.objects.all()
        context['budget_table'] = budget
        return context
    
    def get_success_url(self):
        return reverse('manager:income')

class business(CreateView):
    model = Schedule_Table
    form_class = Schedule_Table_Form
    def get_context_data(self, **kwargs):
        context = super(business, self).get_context_data(**kwargs)
        schedule = Schedule_Table.objects.all()
        context['schedule_table'] = schedule
        return context
    
    def get_success_url(self):
        return reverse('manager:business')

class discount(CreateView):
    model = Discount
    form_class = Discount_Form
    def get_context_data(self, **kwargs):
        context = super(discount, self).get_context_data(**kwargs)
        d = Discount.objects.all()
        context['discount'] = d
        return context
    
    def get_success_url(self):
        return reverse('manager:discount')

class employees(CreateView):
    model = Employee_Table
    form_class = Employee_Table_Form
    def get_context_data(self, **kwargs):
        context = super(employees, self).get_context_data(**kwargs)
        e = Employee_Table.objects.all()
        context['employees'] = e
        return context
    
    def get_success_url(self):
        return reverse('manager:employees')

class restock(CreateView):
    model = Restock_Table
    form_class = Restock_Table_Form
    def get_context_data(self, **kwargs):
        context = super(restock, self).get_context_data(**kwargs)
        r = Restock_Table.objects.all()
        context['restock'] = r
        return context
    
    def get_success_url(self):
        return reverse('manager:restock')

# def employees(request):
#     context = {'text': 'Manager Employees'}
#     template = 'manager/employees.html'
#     return render(request, template, context) 

def profile(request):
    context = {'text': 'Manager Profile'}
    template = 'manager/managerProfile.html'
    return render(request, template, context) 

# def restock(request):
#     context = {'text': 'Manager Restock'}
#     template = 'manager/restock.html'
#     return render(request, template, context)

def error(request):
    context = {'text': 'Manager Error Page'}
    template = 'manager/error.html'
    return render(request, template, context) 

class requests(ListView):
    queryset = Busser_Supplies_Requests.objects.filter(request_complete=False)
    context_object_name = 'object'
    template_name = 'manager/busser_requests.html'

def completeRequest(request, pk):
    request = Busser_Supplies_Requests.objects.get(id=pk)
    request.request_complete = True
    request.save()
    return redirect('manager:requests')



