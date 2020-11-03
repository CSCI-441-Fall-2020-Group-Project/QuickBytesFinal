from manager.models import Worker_Complaint
from django.shortcuts import render, redirect                                                                             
from django.http import HttpResponse                                                                                                                                                        
from manager.models import Worker_Complaint
from home.models import Reservation
from django.urls import reverse
from customer.models import Customer
from tickets.models import Orderstable, Itemtable
from busser.models import Table_Status
from .forms import OrderForm, ItemtableForm, ReservationForm
from datetime import datetime
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView)


from django.views.generic.edit import CreateView

from . forms import Worker_Complaint_Form
from busser.forms import Table_Status_Form

#TODO 
#link up host profile to form
#hook up guest complaint to form
#make menu look good and usable on other pages


# Create your views here.
def dashboard(request):
    
    #reservations = Reservation.objects.filter(date__date=datetime.datetime.today())
    reservations = Reservation.objects.all()
    form = ReservationForm()
    context = {'text': 'Host Dashboard','form':form,'reservations':reservations}
    template = 'host/dashboard.html'
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, template, context) 

def cancelReservation(request, pk):
    reservation = Reservation.objects.get(id=pk)
    context = {'reservation':reservation}
    template = 'host/cancel_reservation.html'
    if request.method == 'POST':
        reservation.delete()
        return redirect('/host/dashboard/')

    return render(request, template, context)

def profile(request):
    context = {'text': 'Host Profile'}
    template = 'host/hostProfile.html'
    return render(request, template, context) 

def error(request):
    context = {'text': 'Host Error Page'}
    template = 'host/404.html'
    return render(request, template, context) 

class create(CreateView):
    model=Worker_Complaint
    template_name='host/hostGrievance.html'
    form_class = Worker_Complaint_Form

    def get_success_url(self):
        return reverse('host:complaints') 

def order(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid:
            order = form.save()
            return redirect('/host/additems/' + str(order.id) )
    recentOrders = Orderstable.objects.order_by("timeordered")[:10]
    #recentOrders = Orderstable.objects.all()
    context = {'text': 'Host Order', 'form':form, 'recentOrders':recentOrders}
    template = 'host/hostOrders.html'
    return render(request, template, context) 

def cancelOrder(request, pk):
    order = Orderstable.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/host/order/')
    context = {'order':order}
    return render(request, 'host/delete_order.html', context)

#stopped here - need to add delete/update functionality to orders 
def addItems(request, pk):
    order = Orderstable.objects.get(id=pk)
    items = Itemtable.objects.all()
    form = ItemtableForm()
    template = 'host/additems.html'
    context = {'order':order,'form':form,'order':order,'items':items}
    if request.method == 'POST':
        form = ItemtableForm(request.POST)
        if form.is_valid():
            item = form.save()
            item.ordernumber = order
            item.save()
            return redirect('/host/additems/' + str(order.id))
    return render(request, template, context)

def deleteItem(request, pk):
    item = Itemtable.objects.get(id=pk)
    order = item.ordernumber
    item.delete()
    return redirect('/host/additems/' + str(order.id))

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
    return redirect('/host/order/')



def information(request):
    context = {'text': 'Host Information'}
    template = 'host/hostInfo.html'
    return render(request, template, context) 

class tables(ListView):
    queryset = Table_Status.objects.filter(status='Available')
    context_object_name = 'object'
    template_name = 'host/tables.html'

# class addTable(CreateView):
#     model=Table_Status
#     template_name='busser/add_table.html'
#     form_class = Table_Status_Form

#     def get_success_url(self):
#         return reverse('host:dashboard')