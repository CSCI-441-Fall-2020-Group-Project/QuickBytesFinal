from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
'''
  // written by: Mark Norfolk & Patrick Carra
  // tested by: Mark Norfolk & Patrick Carra
  // debugged by: Mark Norfolk & Patrick Carra
  // etc.
'''
app_name = 'manager'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('restock/', views.restock.as_view(), name='restock'),
    path('error/', views.error, name='error'),
    path('employees/', views.employees.as_view(), name='employees'),
    path('discount/', views.discount.as_view(), name='discount'),
    path('income/', views.income.as_view(), name='income'),
    path('business/', views.business.as_view(), name='business'),
    path('complaints/', views.complaints, name='complaints'),
    path('requests/', views.requests.as_view(), name='requests'),
    path('completerequest/<int:pk>', views.completeRequest, name='completerequest'),
]
