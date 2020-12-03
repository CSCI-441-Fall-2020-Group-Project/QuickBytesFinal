"""QUICKBYTES URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))


  // written by: Patrick Carra
  // tested by: Patrick Carra
  // debugged by: Patrick Carra
  // etc.

"""
from django.contrib import admin
from django.urls import path, include
from home import views as v #importing the home folder's view.py


urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('menu/', include('menu.urls')),
    path('home/', include('home.urls')),
    path('tickets/', include('tickets.urls')),
    path('delivery/', include('delivery.urls')),
    path('chef/', include('chef.urls')),
    path('busser/', include('busser.urls')),
    path('host/', include('host.urls')),
    path('customer/', include('customer.urls')),
    path('manager/', include('manager.urls')),
    path('server/', include('server.urls')),
    path('register/', v.register, name="register"),
]


