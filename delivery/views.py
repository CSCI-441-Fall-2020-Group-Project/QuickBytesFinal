from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView)
from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView
from django.db.models import Q
from decimal import Decimal

from tickets.models import Orderstable, Itemtable
from customer.models import Customer
from manager.models import Worker_Complaint                                                                        
from django.http import HttpResponse                                                                                                                                                        
from . forms import Worker_Complaint_Form

# Create your views here.
class addCustomer(CreateView):
    model = Customer
    fields = ['user_name', 'first_name', 'last_name', 'phone', 'email', 'street_address', 'city', 'country',]
    template_name = 'delivery/addCustomer.html'
    
    def get_success_url(self):
        return reverse('delivery:addcustomerorder')


class addCustomerOrder(CreateView):
    model = Orderstable
    fields =['customername', 'ordertype']
    template_name = 'delivery/orderstable_form.html'

    def get_success_url(self):
        return reverse('delivery:viewOrder', kwargs={'pk': self.object.pk}) 


class addItem(CreateView):
    model = Itemtable
    fields = ['ordernumber', 'menuitem', 'specialinstructions', 'allergies',] 
    template_name = 'delivery/itemtable_form.html'
    
    def get_success_url(self):
        return reverse('delivery:viewOrder', kwargs={'pk': self.object.ordernumber.id}) 

    def get_initial(self, **kwargs):
        initial = super(addItem, self).get_initial()
        initial['ordernumber'] = self.kwargs['pk']
        return initial

class dashboard(ListView):
    queryset = Orderstable.objects.filter(Q(ordertype='delivery') | Q(ordertype='carryout'))
    context_object_name = 'object'
    template_name = 'delivery/deliveryOrder.html'

class viewOrder(DetailView):
    model = Orderstable
    template_name = 'delivery/orderstable_detail.html'

    def get_success_url(self):
        return reverse('viewOrder', kwargs={'pk': self.object.pk})
'''
class viewOrder(UpdateView):
    model = Orderstable
    fields = ['message', 'status']

    def get_context_data(self, **kwargs):
        context = super(viewOrder, self).get_context_data(**kwargs)
        items = Orderstable.objects.get(id=self.object.id)
        context['items'] = items
        return context

    def get_success_url(self):
        return reverse('viewOrder', kwargs={'pk': self.object.pk})
'''

class editItem(UpdateView):
    model = Itemtable
    fields = ['ordernumber', 'menuitem', 'specialinstructions', 'allergies', 'server', 'ordertime', 'completiontime', 'status'] 
    template_name = 'delivery/itemtable_update_form.html'
    
    def get_success_url(self):
        return reverse('delivery:viewOrder', kwargs={'pk': self.object.ordernumber.id}) 

def sendToKitchen(request, pk):
    order = Orderstable.objects.get(id=pk)
    order.status = 'sentToKitchen'
    order.save()
    return redirect('delivery:dashboard')


def profile(request):
    context = {'text': 'Delivery Profile'}
    template = 'delivery/deliveryProfile.html'
    return render(request, template, context) 

# Creates anonymous complaints to the Manager
class create(CreateView):
    model=Worker_Complaint
    template_name='delivery/deliveryGrievance.html'
    form_class = Worker_Complaint_Form

    def get_success_url(self):
        return reverse('delivery:complaints')

def orders(request):
    context = {'text': 'Delivery Order Queue'}
    template = 'delivery/deliveryOrder.html'
    return render(request, template, context) 

