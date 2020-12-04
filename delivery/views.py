'''
  // written by: Patrick Carra
  // tested by: Patrick Carra
  // debugged by: Patrick Carra
  // etc.
'''

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
#Add a new customer
class addCustomer(CreateView):
    model = Customer
    fields = ['user_name', 'first_name', 'last_name', 'phone', 'email', 'street_address', 'city', 'country',]
    template_name = 'delivery/addCustomer.html'
    
    #Redirect to add new order
    def get_success_url(self):
        return reverse('delivery:addcustomerorder')

#Add a new order
class addCustomerOrderDelivery(CreateView):
    model = Orderstable
    #fields =['customername', 'ordertype', 'requestedtime']
    form_class = addOrderForm
    template_name = 'delivery/orderstable_form.html'

    #redirect to view Order
    def get_success_url(self):
        return reverse('delivery:viewOrder', kwargs={'pk': self.object.pk}) 


#Add a new Item to an order
class addItemDelivery(addItem):
    fields = ['ordernumber', 'menuitem', 'specialinstructions', 'allergies',] 
    template_name = 'delivery/itemtable_form.html'
    
    #Redirect to view Order
    def get_success_url(self):
        return reverse('delivery:viewOrder', kwargs={'pk': self.object.ordernumber.id}) 

    #Set initial Ordernumber value for item
    def get_initial(self, **kwargs):
        initial = super(addItem, self).get_initial()
        initial['ordernumber'] = self.kwargs['pk']
        return initial


#View the Dashboard for the delivery liaison
class dashboard(ListView):
    queryset = Orderstable.objects.filter(Q(ordertype='delivery') | Q(ordertype='carryout')).order_by('requestedtime')
    context_object_name = 'object'
    template_name = 'delivery/deliveryOrder.html'


#View a delivery order
class viewOrderDelivery(DetailView):
    model = Orderstable
    template_name = 'delivery/orderstable_detail.html'

    #Redirect to View the Order
    def get_success_url(self):
        return reverse('delivery:viewOrderDelivery', kwargs={'pk': self.object.pk})

#Edit an item
class editItemDelivery(UpdateView):
    model = Itemtable
    fields = ['ordernumber', 'menuitem', 'specialinstructions', 'allergies', 'server', 'ordertime', 'completiontime', 'status'] 
    template_name = 'delivery/itemtable_update_form.html'
    
    #Redirect to View the order
    def get_success_url(self):
        return reverse('delivery:viewOrder', kwargs={'pk': self.object.ordernumber.id}) 


#edit a customer order
class editCustomerOrder(UpdateView):
    model = Orderstable
    form_class = editOrderForm
    template_name = 'delivery/orderstable_form_edit.html'

    #Redirect to view the Order
    def get_success_url(self):
        return reverse('delivery:vieworder', kwargs={'pk': self.object.pk}) 
    

#Custom function to change status when sending to Kitchen for prep
def sendToKitchen(request, pk):
    order = Orderstable.objects.get(id=pk)
    order.status = 'sentToKitchen'
    order.save()
    return redirect('delivery:dashboard')

#Custom function to change the status to delivered when completed
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

