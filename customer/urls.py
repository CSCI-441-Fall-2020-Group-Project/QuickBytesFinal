'''
  // written by: Kegan Ronholt
  // tested by: Kegan Ronholt
  // debugged by: Kegan Ronholt
'''

from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'customer'
urlpatterns = [
    path('dashboard/<int:pk>/', views.dashboard, name='dashboard'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('history/<int:pk>/', views.history, name='history'),
    path('error/<int:pk>/', views.error, name='error'),
    path('order/<int:pk>/', views.order, name='order'),
    path('cancel_order/<int:pk>', views.cancelOrder, name="cancel_order"),
    path('reservation/<int:pk>/', views.reservation, name='reservation'),
    path('complaints/<int:pk>/', views.complaints, name='complaints'),
    path('delete_complaint/<int:pk>', views.deleteComplaint, name="delete_complaint"),
    path('discounts/<int:pk>/', views.discounts, name='discounts'),
    path('delete_reservation/<int:pk>/', views.cancelReservation, name="cancel_reservation"),
    path('additems/<int:pk>/', views.addItems, name="add_items"),
    path('total/<int:pk>/', views.total, name="total"),
    path('delete_item/<int:pk>/', views.deleteItem, name="delete_item"),
    path('payment/<int:pk>/', views.payment, name="payment"),
    path('contactswitch/<int:pk>', views.lowContact, name="low_contact"),
    path('service_request/<int:pk>', views.serviceRequested, name="service_request"),
    
    ]
