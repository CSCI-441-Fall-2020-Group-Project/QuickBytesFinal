from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView)
from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView
from django.db.models import Q
from decimal import Decimal

from tickets.models import Orderstable, Itemtable
from tickets.views import addItem, editOrder, editItem
from customer.models import Customer
from manager.models import Worker_Complaint                                                                        
from django.http import HttpResponse                                                                                                                                                        
from . forms import Worker_Complaint_Form, addOrderForm, editOrderForm

# Create your views here.
class addCustomer(CreateView):
    model = Customer
    fields = ['user_name', 'first_name', 'last_name', 'phone', 'email', 'street_address', 'city', 'country',]
    template_name = 'delivery/addCustomer.html'
    
    def get_success_url(self):
        return reverse('delivery:addcustomerorder')


class addCustomerOrderDelivery(CreateView):
    model = Orderstable
    #fields =['customername', 'ordertype', 'requestedtime']
    form_class = addOrderForm
    template_name = 'delivery/orderstable_form.html'

    def get_success_url(self):
        return reverse('delivery:viewOrder', kwargs={'pk': self.object.pk}) 


class addItemDelivery(addItem):
    fields = ['ordernumber', 'menuitem', 'specialinstructions', 'allergies',] 
    template_name = 'delivery/itemtable_form.html'
    
    def get_success_url(self):
        return reverse('delivery:viewOrder', kwargs={'pk': self.object.ordernumber.id}) 

    def get_initial(self, **kwargs):
        initial = super(addItem, self).get_initial()
        initial['ordernumber'] = self.kwargs['pk']
        return initial


class dashboard(ListView):
    queryset = Orderstable.objects.filter(Q(ordertype='delivery') | Q(ordertype='carryout')).order_by('requestedtime')
    context_object_name = 'object'
    template_name = 'delivery/deliveryOrder.html'


class viewOrderDelivery(DetailView):
    model = Orderstable
    template_name = 'delivery/orderstable_detail.html'

    def get_success_url(self):
        return reverse('delivery:viewOrderDelivery', kwargs={'pk': self.object.pk})


class editItemDelivery(UpdateView):
    model = Itemtable
    fields = ['ordernumber', 'menuitem', 'specialinstructions', 'allergies', 'server', 'ordertime', 'completiontime', 'status'] 
    template_name = 'delivery/itemtable_update_form.html'
    
    def get_success_url(self):
        return reverse('delivery:viewOrder', kwargs={'pk': self.object.ordernumber.id}) 


class editCustomerOrder(UpdateView):
    model = Orderstable
    form_class = editOrderForm
    template_name = 'delivery/orderstable_form_edit.html'

    def get_success_url(self):
        return reverse('delivery:vieworder', kwargs={'pk': self.object.pk}) 
    

def sendToKitchen(request, pk):
    order = Orderstable.objects.get(id=pk)
    order.status = 'sentToKitchen'
    order.save()
    return redirect('delivery:dashboard')

def delivered(request, pk):
    order = Orderstable.objects.get(id=pk)
    order.status = 'delivered'
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

