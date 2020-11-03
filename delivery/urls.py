from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name='delivery'

urlpatterns = [
    path('addcustomerorder', views.addCustomerOrder.as_view(), name='addcustomerorder'),
    path('additem/<int:pk>', views.addItem.as_view(), name='addItem'),
    path('<int:pk>/', views.viewOrder.as_view(), name='viewOrder'),
    path('profile/', views.profile, name='profile'),
    path('complaints/', views.create.as_view(), name='complaints'),
    path('dashboard', views.dashboard.as_view(), name='dashboard'),
    path('vieworder/<int:pk>', views.viewOrder.as_view(), name='vieworder'),
    path('edititem/<int:pk>', views.editItem.as_view(), name='edititem'),
    path('sendtokitchen/<int:pk>', views.sendToKitchen, name='sendtokitchen'),
    path('addcustomer/', views.addCustomer.as_view(), name='addcustomer'),
    ]
