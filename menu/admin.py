from django.contrib import admin

# Register your models here.
from .models import Menu_Item
#from .models import Menu_Drink_Item

admin.site.register(Menu_Item)
