from django.shortcuts import render, redirect
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView)
from django.urls import reverse_lazy, reverse
from datetime import datetime
from .forms import OrderForm, ItemtableForm, AlertstableForm
from tickets.models import Orderstable, Itemtable, Alertstable
from tickets.views import addCustomerOrder
from django.http import HttpResponse 
from busser.models import Table_Status

# Create your views here.
def profile(request):
    context = {'text': 'Server Profile Page'}
    template = 'server/serverProfile.html'
    return render(request, template, context)

def error(request):
    context = {'text': 'Server Error Page'}
    template = 'server/404.html'
    return render(request, template, context)

def dashboard(request):
    context = {'text': 'Server Dashboard'}
    template = 'server/dashboard.html'
    return render(request, template, context) 

def alerts(request):
    form = AlertstableForm()
    if request.method == 'POST':
        form = AlertstableForm(request.POST)
        if form.is_valid:
            alert = form.save()
            return redirect('/server/serverAlerts/')
    orders = Orderstable.objects.all()
    recentAlerts = Alertstable.objects.all()
    context = {'text': 'Server Alerts','recentAlerts':recentAlerts, "orders":orders}
    template = 'server/serverAlerts.html'
    return render(request, template, context)

def tableclean(request):
    context = {'text': 'Send Tables to Busser'}
    template = 'server/tableClean.html'
    return render(request, template, context)

class serverOrder(addCustomerOrder):
        def get_success_url(self):
            return reverse('server:viewOrder', kwargs={'pk': self.object.pk}) 

class viewOrder(DetailView):
    model = Orderstable

    def get_success_url(self):
        return reverse('server:viewOrder', kwargs={'pk': self.object.pk})

class listOrders(ListView):
    model = Orderstable

def order(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid:
            order = form.save()
            return redirect('/server/additems/' + str(order.id) )
    recentOrders = Orderstable.objects.order_by("timeordered")[:10]
    #recentOrders = Orderstable.objects.all()
    context = {'text': 'Server Order', 'form':form, 'recentOrders':recentOrders}
    template = 'server/serverOrders.html'
    return render(request, template, context) 

def cancelOrder(request, pk):
    order = Orderstable.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/server/order/')
    context = {'order':order}
    return render(request, 'server/delete_order.html', context)

#stopped here - need to add delete/update functionality to orders 
def addItems(request, pk):
    order = Orderstable.objects.get(id=pk)
    items = Itemtable.objects.all()
    form = ItemtableForm()
    template = 'server/additems.html'
    context = {'order':order,'form':form,'order':order,'items':items}
    if request.method == 'POST':
        form = ItemtableForm(request.POST)
        if form.is_valid():
            item = form.save()
            item.ordernumber = order
            item.save()
            return redirect('/server/additems/' + str(order.id))
    return render(request, template, context)

def deleteItem(request, pk):
    item = Itemtable.objects.get(id=pk)
    order = item.ordernumber
    item.delete()
    return redirect('/server/additems/' + str(order.id))

def total(request, pk):
    order = Orderstable.objects.get(id=pk)
    order.total = 0
    for item in order.itemtable_set.all():
        quantity = item.quantity
        
        if quantity is not None:
            order.total += (quantity * item.menuitem.price)
        else:
            order.total += order.total +  item.menuitem.price
    order.save()
    return redirect('/server/order/')

class tables(ListView):
    queryset = Table_Status.objects.filter(status='Occupied')
    context_object_name = 'object'
    template_name = 'server/tables.html'

def setDirty(request, pk):
    request = Table_Status.objects.get(id=pk)
    request.status = 'Dirty'
    request.save()
    return redirect('server:tables')

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

def alert(request):
    # form = AlertstableForm()
    # if request.method == 'POST':
    #     form = AlertstableForm(request.POST)
    #     if form.is_valid:
    #         alert = form.save()
    #         return redirect('/server/serverAlerts/')
    orders = Orderstable.objects.all()
    recentAlerts = Alertstable.objects.all()
    context = {'text': 'Server Alerts','recentAlerts':recentAlerts, "orders":orders}
    template = 'server/serverAlerts.html'
    return render(request, template, context) 