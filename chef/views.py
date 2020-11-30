from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from datetime import datetime
from decimal import Decimal
from re import sub

from tickets.models import Orderstable, Itemtable
from . forms import SendBackForm
from . models import SupplyOrder
from manager.models import Worker_Complaint                                                                         
from django.http import HttpResponse                                                                                                                                                        
from manager.models import Worker_Complaint
from django.urls import reverse
from . forms import Worker_Complaint_Form


# Create your views here.
def completeOrder(request, pk):
    order = Orderstable.objects.get(id=pk)
    order.status = 'orderCompleted'
    order.save()
    order.total = order.total 
    order.save()
    return redirect('chef:dashboard')


class dashboard(ListView):
    queryset = Orderstable.objects.filter(status='sentToKitchen')
    context_object_name = 'object'
    template_name= 'chef/chefIndex.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(dashboard, self).get_context_data(**kwargs)
        #Add additional context vars here
        now = datetime.now()
        context['time'] = now
        return context


class viewOrder(DetailView):
    model = Orderstable
    template_name = 'chef/orderstable_detail.html'

    def get_success_url(self):
        return reverse('chef:viewOrder', kwargs={'pk': self.object.pk})

   
class sendBack(UpdateView):
    model = Orderstable
    form_class = SendBackForm
    success_url = reverse_lazy('chef:listOrders')
    template_name = 'chef/orderstable_form.html'
    #fields = ['message']

    def form_valid(self, form):
        Orderstable = form.save(commit=False)
        Orderstable.status = 'sendBacktoServer'
        Orderstable.save()
        return redirect('chef:dashboard')

def profile(request):
    context = {'text': 'Chef Profile'}
    template = 'chef/chefProfile.html'
    return render(request, template, context) 

def returns(request):
    context = {'text': 'Chef Returns'}
    template = 'chef/chefReturns.html'
    return render(request, template, context) 

def error(request):
    context = {'text': 'Chef Error Page'}
    template = 'chef/404.html'
    return render(request, template, context) 

class create(CreateView):
    model=Worker_Complaint
    template_name='chef/chefGrievance.html'
    form_class = Worker_Complaint_Form

    def get_success_url(self):
        return reverse('chef:complaints')


class listSupply(ListView):
    model = SupplyOrder

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.exclude(status='Received')

    def get_success_url(self):
        return reverse('chef:dashboard')


class addSupply(CreateView):
    model = SupplyOrder
    fields = ['ingredient', 'order', 'status']

    def get_success_url(self):
        return reverse('chef:listsupply')


class editSupply(UpdateView):
    model = SupplyOrder
    fields = ['ingredient', 'order', 'status']

    def get_success_url(self):
        return reverse('chef:listsupply')

    
class deleteSupply(DeleteView):
    model = SupplyOrder
    #template_name = 'chef/deletesupply.html'

    def get_success_url(self):
        return reverse('chef:listsupply')



