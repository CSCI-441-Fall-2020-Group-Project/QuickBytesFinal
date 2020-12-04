'''
  // written by: Patrick Carra
  // tested by: Patrick Carra
  // debugged by: Patrick Carra
  // etc.
'''

from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name='tickets'
urlpatterns = [
    path('addticketsorder', views.addCustomerOrder.as_view(),),
    path('additem/<int:pk>', views.addItem.as_view(), name='addItem'),
    path('edititem/<int:pk>', views.editItem.as_view(), name='editItem'),
    path('listorders', views.listOrders.as_view(), name='listOrders'),
    path('editorder/<int:pk>', views.editOrder.as_view(), name='editOrder'),
    path('sendorder/<int:pk>', views.sendOrder.as_view(), name='sendOrder'),
]
