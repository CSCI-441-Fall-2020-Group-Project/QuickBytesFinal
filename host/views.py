'''
  // written by: Kegan Ronholt
  // tested by: Kegan Ronholt
  // debugged by: Kegan Ronholt
'''

from manager.models import Worker_Complaint
from django.shortcuts import render, redirect                                                                             
from django.http import HttpResponse       
from .models import WaitList                                                                                                                                                 
from manager.models import Worker_Complaint
from home.models import Reservation
from django.urls import reverse
from customer.models import Customer
from home.models import tableTable
from django.contrib import messages
from tickets.models import Orderstable, Itemtable
from customer.forms import OrderForm as TableAssignForm
from busser.models import Table_Status
from .forms import OrderForm, ItemtableForm, ReservationForm, WaitListForm
from datetime import datetime
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView)
from django.views.generic.edit import CreateView
from . forms import Worker_Complaint_Form
from busser.forms import Table_Status_Form

#TODO - allow hosts to create new or temporary customers - this may have to be future feature


#the host dashboard allows hosts to place and manage reservations
def dashboard(request):
    
    #reservations = Reservation.objects.filter(date__date=datetime.datetime.today())
    reservations = Reservation.objects.all()
    form = ReservationForm()
    tables = tableTable.objects.all()
    context = {'text': 'Host Dashboard','form':form,'reservations':reservations, 'tables':tables}
    template = 'host/dashboard.html'
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            #saves the form as a new reservation and returns the new object to reservation variable
            #filters the reservation lists looking for duplicate date/time/table
            #if this is found, the table is already booked
            r1 = Reservation.objects.filter(date=form.cleaned_data['date'])
            r2 = r1.filter(time=form.cleaned_data['time'])
            r3 = r2.filter(table=form.cleaned_data['table'])
            if not r3:
                form.save()
            else:
                messages.error(request, "That Table is already reserved for that time/date")
                
    return render(request, template, context) 


    
#allows host to cancel reservation of guests
def cancelReservation(request, pk):
    reservation = Reservation.objects.get(id=pk)
    context = {'reservation':reservation}
    template = 'host/cancel_reservation.html'
    if request.method == 'POST':
        reservation.delete()
        return redirect('/host/dashboard/')

    return render(request, template, context)

#host profile
def profile(request):
    context = {'text': 'Host Profile'}
    template = 'host/hostProfile.html'
    return render(request, template, context) 

#general error page
def error(request):
    context = {'text': 'Host Error Page'}
    template = 'host/404.html'
    return render(request, template, context) 

#page to create complaints
class create(CreateView):
    model=Worker_Complaint
    template_name='host/hostGrievance.html'
    form_class = Worker_Complaint_Form

    def get_success_url(self):
        return reverse('host:complaints') 

#this method is called after the Host takes a customer off the waitlist and creates an order for them
def assignTable(request, pk):
    customer = Customer.objects.get(id=pk)
    form = TableAssignForm()
    customer.waitlist_set.all().delete()
    tables = tableTable.objects.all()
    template = 'host/assign_table.html'   
    context = {'customer':customer, 'form':form, 'tables':tables}
    if request.method == 'POST':
        form = TableAssignForm(request.POST)
        if form.is_valid():
            #saves the form as a new reservation and returns the new object to reservation variable
            order = form.save()
            #if the ordertype is dine-in we need to make sure an occupied table is not selected
            if order.ordertype == "dine-in":
                if order.tablenumber.status != "available":
                    order.delete()
                    messages.error(request, "Table is currently occupied")
                else:
                    order.tablenumber.status = "occupied"
                    order.tablenumber.save()
                    order.customername = customer
                    order.save()
                    return redirect('/host/additems/' + str(order.id))

            else:
                order.tablenumber = None
                order.customername = customer
                order.save()
                return redirect('/host/additems/' + str(order.id))
    return render(request, template, context) 


#allows the host to place orders for other customers
def order(request):
    form = OrderForm()
    #if a POST request was sent from the host/orders screen
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid:
            order = form.save()
            #if the order is type dine-in we need to prevent occupied or closed tables from being selected
            if order.ordertype == "dine-in":
                if order.tablenumber.status != "available":
                    order.delete()
                    messages.error(request, "Table is currently occupied")
                else:
                    order.tablenumber.status = "occupied"
                    order.tablenumber.save()
                    return redirect('/host/additems/' + str(order.id))
            #if the order is not dine-in it doesn't matter what table they select, it will be deleted anyway
            else:
                order.tablenumber = None
                order.save()
                return redirect('/host/additems/' + str(order.id))
    tables = tableTable.objects.all()
    recentOrders = Orderstable.objects.order_by("timeordered")[:10]
    #recentOrders = Orderstable.objects.all()
    context = {'text': 'Host Order', 'form':form, 'recentOrders':recentOrders, 'tables':tables}
    template = 'host/hostOrders.html'
    return render(request, template, context) 

#allows the host to cancel customer orders
def cancelOrder(request, pk):
    order = Orderstable.objects.get(id=pk)
    if request.method == 'POST':
        if order.ordertype == "dine-in":
            if order.tablenumber is not None:
                order.tablenumber.status = "available"
                order.tablenumber.save()
        order.delete()
        return redirect('/host/order/')
    context = {'order':order}
    return render(request, 'host/delete_order.html', context)

#directed here after order creation, allows host to add items to the guest order
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

#allows customer to click button to delete a menu item from order
def deleteItem(request, pk):
    item = Itemtable.objects.get(id=pk)
    order = item.ordernumber
    item.delete()
    return redirect('/host/additems/' + str(order.id))

#called after menu items have been added and order is complete - totals the menu item cost and adds to order.total
def total(request, pk):
    order = Orderstable.objects.get(id=pk)
    order.total = 0
    #iterates through the items in the order and adds their quantity * price to order.total
    for item in order.itemtable_set.all():
        quantity = item.quantity
        
        if quantity is not None:
            order.total += (quantity * item.menuitem.price)
        else:
            order.total += order.total +  item.menuitem.price
    order.save()
    return redirect('/host/order/')

#allows host to add customers to the waiting list
def waitList(request):
    form = WaitListForm()
    tables = tableTable.objects.all()
    entries = WaitList.objects.all()
    if request.method == 'POST':
        form = WaitListForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form, 'entries':entries, 'tables':tables}
    template = 'host/waitlist.html'
    return render(request, template, context)

#allows host to remove customers from waiting list
def cancelWaitList(request, pk):
    entry = WaitList.objects.get(id=pk)
    entry.delete()
    return redirect('/host/waitlist/')

#displays basic restaurant information
def information(request):
    context = {'text': 'Host Information'}
    template = 'host/hostInfo.html'
    return render(request, template, context) 

#displays the tables in the restaurant
class tables(ListView):
    queryset = Table_Status.objects.filter(status='Available')
    context_object_name = 'object'
    template_name = 'host/tables.html'




class newTable(CreateView):
    model=Table_Status
    template_name='host/add_table.html'
    form_class = Table_Status_Form

    def get_success_url(self):
        return reverse('host:tables')

