from django.shortcuts import render, redirect
from .models import Customer, Complaint, Discount
from home.models import Reservation, tableTable
from .forms import ReservationForm, OrderForm, ItemtableForm, ComplaintForm, CustomerForm
from django.contrib import messages
from menu.models import Menu_Item
from tickets.models import Orderstable, Itemtable
from django.db.models import Sum
from decimal import Decimal


#TODO in customer
# Allow for updating through profile section
# Hook up dashboard to correct templates

# Create your views here.
def dashboard(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = Orderstable.objects.all()
    context = {'text': 'Customer Dashboard', 'customer':customer, 'orders':orders}
    template = 'customer/dashboard.html'
    return render(request, template, context) 

def profile(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()

    context = {'text': 'Customer Profile', 'customer':customer, 'form':form}
    template = 'customer/customerProfile.html'
    return render(request, template, context) 





def history(request, pk):
    customer = Customer.objects.get(id=pk)
    context = {'text': 'Customer Order History', 'customer':customer}
    template = 'customer/customerOrderHistory.html'
    return render(request, template, context) 

def error(request, pk):
    customer = Customer.objects.get(id=pk)
    context = {'text': 'Customer Error Page', 'customer':customer}
    template = 'customer/404.html'
    return render(request, template, context) 

def cancelReservation(request, pk):
    reservation = Reservation.objects.get(id=pk)
    customer = reservation.customer
    if request.method == "POST":
        reservation.delete()
        return redirect('/customer/reservation/' + str(customer.id))
    context = {'customer':customer, 'reservation':reservation}
    return render(request, 'customer/delete_reservation.html', context)

def reservation(request, pk):
    customer = Customer.objects.get(id=pk)
    form = ReservationForm()
    context = {'text': 'Customer Reservations', 'customer':customer, 'form':form}
    template = 'customer/customerReservations.html'
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            #saves the form as a new reservation and returns the new object to reservation variable
            reservation = form.save()
            #assigns the reservation to the customer object and saves reservation
            reservation.customer = customer
            reservation.save()

            
            return redirect('/customer/reservation/' + str(pk))
    return render(request, template, context) 

def complaints(request, pk):
    customer = Customer.objects.get(id=pk)
    form = ComplaintForm()
    context = {'text': 'Customer Complaints', 'customer':customer, 'form':form}
    template = 'customer/customerComplaints.html'
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save()
            complaint.customer = customer
            complaint.save()
            return redirect('/customer/complaints/' + str(customer.id))
    
    return render(request, template, context) 

def deleteComplaint(request, pk):
    complaint = Complaint.objects.get(id=pk)
    customer = complaint.customer
    complaint.delete()
    return redirect('/customer/complaints/' + str(customer.id))

def discounts(request, pk):
    customer = Customer.objects.get(id=pk)
    discounts = customer.discount_set.all()
    context = {'text': 'Customer Discounts', 'customer':customer, 'discounts':discounts}
    template = 'customer/customerDiscounts.html'
    return render(request, template, context) 

def order(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = Orderstable.objects.all()
    form = OrderForm()
    template = 'customer/customerOrder.html'
            
    context = {'customer':customer, 'form':form, 'orders':orders}
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            #saves the form as a new reservation and returns the new object to reservation variable
            order = form.save()
            if order.ordertype == "carryout" or order.ordertype == "delivery":
                blanktable = tableTable.objects.get(id=13)
                order.tablenumber = blanktable
            order.customername = customer
            order.save()
            #assigns the reservation to the customer object and saves reservation
            return redirect('/customer/additems/' + str(order.id))
    return render(request, template, context) 

def cancelOrder(request, pk):
    order = Orderstable.objects.get(id=pk)
    customer = order.customername
    if request.method == "POST":
        order.delete()
        return redirect('/customer/order/' + str(customer.id))
    context = {'customer':customer, 'order':order}
    return render(request, 'customer/delete_order.html', context)  
        

def addItems(request, pk):
    order = Orderstable.objects.get(id=pk)
    customer = order.customername
    items = Itemtable.objects.all()
    form = ItemtableForm()
    template = 'customer/additems.html'
   
    context = {'order':order, 'form':form, 'customer':customer, 'items':items}
    if request.method == 'POST':
        form = ItemtableForm(request.POST)
        if form.is_valid():
            item = form.save()
            item.ordernumber = order
            item.save()
            return redirect('/customer/additems/' + str(order.id))

    return render(request, template, context)

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
    return redirect('/customer/order/' + str(order.customername.id))

def deleteItem(request, pk):
    item = Itemtable.objects.get(id=pk)
    order = item.ordernumber
    item.delete()
    return redirect('/customer/additems/' + str(order.id))