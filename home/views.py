from django.template import loader
from django.shortcuts import render
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView)
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import Group
from .forms import registerForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse
from menu.models import Menu_Item
from customer.models import Customer

from .models import Reservation

# Create your views here.
def index(request):
    context = {'text': 'QUICKBYTES Homepage'}
    template = 'home/homepage.html'
    return render(request, template, context)

def faq(request):
    context = {'text': 'QUICKBYTES FAQ'}
    template = 'home/faq.html'
    return render(request, template, context)

def menu(request):
    menu = Menu_Item.objects.all()
    context = {'all_menu_items':menu}
    template = 'home/menu.html'
    return render(request, template, context)

class makeReservation(CreateView):
    model = Reservation
    fields = ['table', 'customer', 'guestCount', 'date']
    def get_success_url(self):
        return reverse("viewReservation", kwargs={'pk':self.object.pk})

    
class viewReservation(DetailView):
    model = Reservation
    def get_success_url(self):
        return reverse('viewReservation', kwargs={'pk': self.object.pk}) 

#Login request is handled and authenticated by django
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if (len(user.groups.all())>0):
                    group = str(user.groups.all()[0])
                    group = group.lower()
                else:
                    group=False
                if user is not None:
                    login(request, user)
                    #if the user is a customer, their id will be used to load their page
                    if(group == "customer"):
                        customer = Customer.objects.get(user_name=user.username)
                        return redirect('/customer/dashboard/' + str(customer.id))
                    if(group):
                        messages.info(request, f"You are now logged in as {username}")
                        return redirect(group + ':dashboard')
                    else:
                        return redirect('/home/')
            else:
                messages.error(request, "Invalid username or password.")
                return redirect('login')
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "home/login.html",{"form":form})

def about(request):
    context = {'text': 'QUICKBYTES About-us'}
    template = 'home/about-us.html'
    return render(request, template, context)

#Register function to create new users, this uses forms.py
def register(response):
    if response.method == "POST":
        form = registerForm(response.POST)
        if form.is_valid():
            #creates new user from the form data
            newUser = form.save()
            #adds the new user to the Customer group
            my_group = Group.objects.get(name="Customer")
            my_group.user_set.add(newUser)
            my_group.save()
            #creates a new customer object using the form data
            customer = Customer(first_name=newUser.first_name, last_name=newUser.last_name, user_name=newUser.username, 
            email=newUser.email)
            customer.save()
            messages.success(response, "Your account was created successfully. Please log in.")
            return redirect('login')
    else: 
        form = registerForm()
    
    context = {'form': form}
    return render(response, 'home/register.html', context)


def view_404(request):
    return render(request, 'home/view_404.html', {})