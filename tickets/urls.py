from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name='tickets'
urlpatterns = [
    path('addcustomerorder', views.addCustomerOrder.as_view(),),
    path('<int:pk>/', views.viewOrder.as_view(), name='viewOrder'),
    path('additem/<int:pk>', views.addItem.as_view(), name='addItem'),
    path('edititem/<int:pk>', views.editItem.as_view(), name='editItem'),
    path('listorders', views.listOrders.as_view(), name='listOrders'),
    path('editorder/<int:pk>', views.editOrder.as_view(), name='editOrder'),
    path('sendorder/<int:pk>', views.sendOrder.as_view(), name='sendOrder'),
]
