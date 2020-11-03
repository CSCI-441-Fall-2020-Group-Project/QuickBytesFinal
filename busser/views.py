from manager.models import Worker_Complaint
from django.shortcuts import render, redirect                                                                             
from django.http import HttpResponse                                                                                                                                                        
from manager.models import Worker_Complaint
from busser.models import Busser_Supplies_Requests, Table_Status
from django.urls import reverse
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView)

from django.views.generic.edit import CreateView
from . forms import Worker_Complaint_Form, Busser_Supplies_Form, Table_Status_Form

# Create your views here.
def error(request):
    context = {'text': 'QUICKBYTES Error Page'}
    template = 'busser/404.html'
    return render(request, template, context)

def dashboard(request):
    context = {'text': 'QUICKBYTES Busser'}
    template = 'busser/busserIndex.html'
    return render(request, template, context)

def profile(request):
    context = {'text': 'QUICKBYTES Busser Profile'}
    template = 'busser/busserProfile.html'
    return render(request, template, context)

class create(CreateView):
    model=Worker_Complaint
    template_name='busser/busserGrievance.html'
    form_class = Worker_Complaint_Form

    def get_success_url(self):
        return reverse('busser:complaints')

class supplies(CreateView):
    model=Busser_Supplies_Requests
    template_name='busser/supplies.html'
    form_class = Busser_Supplies_Form

    def get_success_url(self):
        return reverse('busser:dashboard')

class addTable(CreateView):
    model=Table_Status
    template_name='busser/add_table.html'
    form_class = Table_Status_Form

    def get_success_url(self):
        return reverse('busser:dashboard')

class queue(ListView):
    queryset = Table_Status.objects.filter(status='Dirty')
    context_object_name = 'object'
    template_name = 'busser/queue.html'

def makeClean(request, pk):
    request = Table_Status.objects.get(id=pk)
    request.status = 'Available'
    request.save()
    return redirect('busser:queue')

