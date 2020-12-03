'''
  // written by: Patrick Carra
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
class addCustomerOrder(CreateView):
    model = Orderstable
    fields = ['customername', 'ordertype']

    def get_success_url(self):
        return reverse('tickets:viewOrder', kwargs={'pk': self.object.pk})    


class listOrders(ListView):
    model = Orderstable


class sendOrder(UpdateView):
    model = Orderstable
    fields = ['tablenumber']
    template_name = 'tickets/sendorder.html'

    def get_success_url(self):
        return reverse('tickets:viewOrder', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        Orderstable = form.save(commit=False)
        Orderstable.status = 'sentToKitchen'
        Orderstable.save()
        Orderstable.timeordered = datetime.now().time()
        Orderstable.save()
        return HttpResponseRedirect(self.get_success_url())


class addItem(CreateView):
    model = Itemtable
    fields = ['ordernumber', 'menuitem', 'specialinstructions', 'allergies', 'server', 'ordertime', 'completiontime', 'status'] 

    def get_success_url(self):
        return reverse('tickets:viewOrder', kwargs={'pk': self.object.ordernumber.id})    
    
    def get_initial(self, **kwargs):
        initial = super(CreateView, self).get_initial()
        initial['ordernumber'] = self.kwargs['pk']
        return initial
    

class editItem(UpdateView):
    model = Itemtable
    fields = ['ordernumber', 'menuitem', 'specialinstructions', 'allergies', 'server', 'ordertime', 'completiontime', 'status']

    def get_success_url(self):
        return reverse('tickets:viewOrder', kwargs={'pk': self.object.pk})  


class editOrder(UpdateView):
    model = Orderstable
    fields = ['customername', 'ordertype', 'status', 'timeordered', 'timecompleted', 'tablenumber', 'total', 'message']

    def get_success_url(self):
        return reverse('tickets:viewOrder', kwargs={'pk': self.object.pk})

class addAlert(CreateView):
    model = Alertstable
    fields = [ 'sender', 'receiver', 'message', 'priority']

    def get_success_url(self):
        return reverse('tickets:viewAlert', kwargs={'pk': self.object.pk})

class listAlerts(ListView):
    model = Alertstable


class viewAlert(DetailView):
    model = Alertstable

    def get_success_url(self):
        return reverse('tickets:viewAlert', kwargs={'pk': self.object.pk})  