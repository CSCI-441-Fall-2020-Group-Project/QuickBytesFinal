'''
  // written by: Patrick Carra, Clint Ryan
  // tested by: Patrick Carra
  // debugged by: Patrick Carra
  // etc.
'''

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView)
from datetime import datetime

from . models import Orderstable, Itemtable, Alertstable

# Create your views here.
#Create new order
class addCustomerOrder(CreateView):
    model = Orderstable
    fields = ['customername', 'ordertype']

    #Redirect to viewOrder screen
    def get_success_url(self):
        return reverse('tickets:viewOrder', kwargs={'pk': self.object.pk})    

#Display Orders in list form
class listOrders(ListView):
    model = Orderstable

#Send order to kitchen
class sendOrder(UpdateView):
    model = Orderstable
    fields = ['tablenumber']
    template_name = 'tickets/sendorder.html'

    #Redirect to view Order
    def get_success_url(self):
        return reverse('tickets:viewOrder', kwargs={'pk': self.object.pk})

    #Used to change status without user input
    def form_valid(self, form):
        Orderstable = form.save(commit=False)
        Orderstable.status = 'sentToKitchen'
        Orderstable.save()
        Orderstable.timeordered = datetime.now().time()
        Orderstable.save()
        return HttpResponseRedirect(self.get_success_url())


#Add Item to Order
class addItem(CreateView):
    model = Itemtable
    fields = ['ordernumber', 'menuitem', 'specialinstructions', 'allergies', 'server', 'ordertime', 'completiontime', 'status'] 

    #Redirect to View Order
    def get_success_url(self):
        return reverse('tickets:viewOrder', kwargs={'pk': self.object.ordernumber.id})    
    
    #Populate initial values of form
    def get_initial(self, **kwargs):
        initial = super(CreateView, self).get_initial()
        initial['ordernumber'] = self.kwargs['pk']
        return initial
    

#edit the Item selected
class editItem(UpdateView):
    model = Itemtable
    fields = ['ordernumber', 'menuitem', 'specialinstructions', 'allergies', 'server', 'ordertime', 'completiontime', 'status']

    #Redirect to View Order
    def get_success_url(self):
        return reverse('tickets:viewOrder', kwargs={'pk': self.object.pk})  


#Edit the selected Order
class editOrder(UpdateView):
    model = Orderstable
    fields = ['customername', 'ordertype', 'status', 'timeordered', 'timecompleted', 'tablenumber', 'total', 'message']

    #Redirect to view Order
    def get_success_url(self):
        return reverse('tickets:viewOrder', kwargs={'pk': self.object.pk})

#Add an alert
class addAlert(CreateView):
    model = Alertstable
    fields = [ 'sender', 'receiver', 'message', 'priority']

    #Redirect to viewAlert
    def get_success_url(self):
        return reverse('tickets:viewAlert', kwargs={'pk': self.object.pk})

#view all alerts
class listAlerts(ListView):
    model = Alertstable


#View an individual alert
class viewAlert(DetailView):
    model = Alertstable

    #Redirect to view Alert
    def get_success_url(self):
        return reverse('tickets:viewAlert', kwargs={'pk': self.object.pk})  