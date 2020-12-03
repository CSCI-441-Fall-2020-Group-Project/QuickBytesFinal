'''
  // written by: Kegan Ronholt
  // tested by: Kegan Ronholt
  // debugged by: Kegan Ronholt
'''

from django.shortcuts import loader
from django.http import HttpResponse 
from django.shortcuts import render, get_object_or_404
from .models import  Menu_Item
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView



# Create your views here.


def index(request):
    all_menu_items = Menu_Item.objects.all() 
    #all_drink_items = Menu_Drink_Item.objects.all()
    context = {
        'all_menu_items': all_menu_items
    }

    return render(request, 'menu/menu.html', context)

# def item_detail(request, menu_item_id):
#     menu_item = get_object_or_404(Menu_Item, pk=menu_item_id)
#     return render(request, 'menu/item_detail.html', {'menu_item':menu_item})



    

class createItem(CreateView):
     model = Menu_Item
     fields = ['name', 'description', 'price', 'item_type']

class editItem(UpdateView):
    model = Menu_Item
    fields = ['name', 'description', 'price', 'item_type']

class listItem(ListView):
    model = Menu_Item
    fields = ['name', 'description', 'price', 'item_type']




