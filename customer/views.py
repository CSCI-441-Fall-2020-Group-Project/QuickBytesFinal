'''
  // written by: Kegan Ronholt
  // tested by: Kegan Ronholt
  // debugged by: Kegan Ronholt
'''

from django.shortcuts import render, redirect
from .models import Customer, Complaint, Discount, Payment
from home.models import Reservation, tableTable
from .forms import ReservationForm, OrderForm, ItemtableForm, ComplaintForm, CustomerForm, PaymentForm
from django.contrib import messages
from menu.models import Menu_Item
from tickets.models import Orderstable, Itemtable, Alertstable
from django.db.models import Sum
from decimal import Decimal


# Create your views here.
def dashboard(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = Orderstable.objects.all()
    context = {'text': 'Customer Dashboard', 'customer':customer, 'orders':orders}
    template = 'customer/dashboard.html'
    return render(request, template, context) 

#This function allows the customer to request service from the server. This proccesses the button click and sends the alert to the server
def serviceRequested(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = Customer.orderstable_set.all()
    alert = Alertstable(sender="Customer", receiver="Server", message=customer.first_name + " " + customer.last_name + " is requesting service")
    alert.save()
    messages.success(request, "Service request placed. Staff will be with you shortly")
    context = {"customer": customer}
    template = 'customer/dashboard.html'
    return render(request,template,context)

#This function allows the customer to select the Low Contact Enable:Disable button on their dashboard
def lowContact(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.low_contact = not customer.low_contact
    customer.save()
    return redirect('/customer/dashboard/' + str(pk))

#received the order id after customer has added items on the additem.html page
#Customer is directed to add payment method and pay for food
def payment(request, pk):
    order = Orderstable.objects.get(id=pk)
    customer = order.customername
    form = PaymentForm()
    context = {'order':order, 'customer':customer, 'form':form}
    template = 'customer/payment.html'
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid:
            form.save()
            order.paid = True
            order.save()
            return redirect('/customer/order/' + str(customer.id))
    return render(request, template, context)


#this loads the customer profile - this displays an editable form with the customers current information and the ability to change fields 
def profile(request, pk):
    customer = Customer.objects.get(id=pk)
    #using the instance=customer preloads the form with the customer's information
    form = CustomerForm(instance=customer)
    #the submit button will update any changed fields and keep the rest the same
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()

    context = {'text': 'Customer Profile', 'customer':customer, 'form':form}
    template = 'customer/customerProfile.html'
    return render(request, template, context) 


#general load of the orderhistory.html page
def history(request, pk):
    customer = Customer.objects.get(id=pk)
    context = {'text': 'Customer Order History', 'customer':customer}
    template = 'customer/customerOrderHistory.html'
    return render(request, template, context) 

#general load of the error page
def error(request, pk):
    customer = Customer.objects.get(id=pk)
    context = {'text': 'Customer Error Page', 'customer':customer}
    template = 'customer/404.html'
    return render(request, template, context) 

#allows customer to cancel their reservations
def cancelReservation(request, pk):
    reservation = Reservation.objects.get(id=pk)
    customer = reservation.customer
    if request.method == "POST":
        reservation.delete()
        return redirect('/customer/reservation/' + str(customer.id))
    context = {'customer':customer, 'reservation':reservation}
    return render(request, 'customer/delete_reservation.html', context)

#view for creating a new reservation
def reservation(request, pk):
    customer = Customer.objects.get(id=pk)
    form = ReservationForm()
    context = {'text': 'Customer Reservations', 'customer':customer, 'form':form}
    template = 'customer/customerReservations.html'
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            #saves the form as a new reservation and returns the new object to reservation variable
            #form.cleaned_date['date'] gives the date data in the form given by the customer
            #I filtered all of the reservation objects by the date, time, and table that match the attempted customer reservation
            #if there is any object in r3, this means that there is a table with the same time/date. Reservation will not be saved 
            r1 = Reservation.objects.filter(date=form.cleaned_data['date'])
            r2 = r1.filter(time=form.cleaned_data['time'])
            r3 = r2.filter(table=form.cleaned_data['table'])
            #there is no previous reservation
            if not r3:
                reservation =  form.save()
                reservation.customer = customer
                reservation.save()
            else:
                messages.error(request, "That Table is already reserved for that time/date")
            #assigns the reservation to the customer object and saves reservation
            return redirect('/customer/reservation/' + str(pk))
    return render(request, template, context) 

#handles the complaint form submitted by customer
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

#retracts a user complaint when they click the "Withdraw Complaint" button on customerComplaints.html
def deleteComplaint(request, pk):
    complaint = Complaint.objects.get(id=pk)
    customer = complaint.customer
    complaint.delete()
    return redirect('/customer/complaints/' + str(customer.id))

#loads the discounts that belong to the customer
def discounts(request, pk):
    customer = Customer.objects.get(id=pk)
    #discount_set.all() returns all of the discounts belonging to this customer
    discounts = customer.discount_set.all()
    context = {'text': 'Customer Discounts', 'customer':customer, 'discounts':discounts}
    template = 'customer/customerDiscounts.html'
    return render(request, template, context) 

#handles the order submission of a customer
def order(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = Orderstable.objects.all()
    form = OrderForm()
    tables = tableTable.objects.all()
    template = 'customer/customerOrder.html'
    context = {'customer':customer, 'form':form, 'orders':orders, 'tables':tables}
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            #saves the form as a new reservation and returns the new object to reservation variable
            order = form.save()
            order.customername = customer
            #if the ordertype is dine-in we need to prevent them from selecting currently occupied tables
            if order.ordertype == "dine-in":
                #if the table is not available, the order attempt is deleted and message is sent to customer
                if order.tablenumber.status != "available":
                    order.delete()
                    messages.error(request, "Table is currently occupied")
                else:
                    order.tablenumber.status = "occupied"
                    order.tablenumber.save()
                    order.save()
                    return redirect('/customer/additems/' + str(order.id))
            else:
                order.tablenumber = None
                order.save()
                return redirect('/customer/additems/' + str(order.id))

            #assigns the reservation to the customer object and saves reservation
    return render(request, template, context) 

#allows customer to cancel one of their orders
def cancelOrder(request, pk):
    order = Orderstable.objects.get(id=pk)
    customer = order.customername
    if request.method == "POST":
        #if the ordertype is dine-in we will need to set the status back to available
        if order.ordertype == "dine-in":
            #this checks for null value in the order table - although this shouldn't occur with the way the system is currently set up.
            if order.tablenumber is not None:
                order.tablenumber.status = "available"
                order.tablenumber.save()
        order.delete()
        return redirect('/customer/order/' + str(customer.id))
    context = {'customer':customer, 'order':order}
    return render(request, 'customer/delete_order.html', context)  
        
#this view is called after order is created - customer adds menu items to their order
def addItems(request, pk):
    order = Orderstable.objects.get(id=pk)
    menu = Menu_Item.objects.all()
    customer = order.customername
    items = Itemtable.objects.all()
    form = ItemtableForm()
    template = 'customer/additems.html'
   
    context = {'order':order, 'form':form, 'customer':customer, 'items':items, 'all_menu_items':menu}
    if request.method == 'POST':
        form = ItemtableForm(request.POST)
        if form.is_valid():
            item = form.save()
            item.ordernumber = order
            item.save()
            return redirect('/customer/additems/' + str(order.id))

    return render(request, template, context)

#this method is called when the items are all added to order and the order is submitted, it totals the cost of the menu items and updates order.total
def total(request, pk):
    order = Orderstable.objects.get(id=pk)
    customer = order.customername
    order.total = 0
    for item in order.itemtable_set.all():
        quantity = item.quantity
        if quantity is not None:
            order.total += (quantity * item.menuitem.price)
        else:
            order.total += order.total +  item.menuitem.price
    order.save()
    return redirect('/customer/payment/' + str(order.id))

#alows customer to remove an item from their order
def deleteItem(request, pk):
    item = Itemtable.objects.get(id=pk)
    order = item.ordernumber
    item.delete()
    return redirect('/customer/additems/' + str(order.id))