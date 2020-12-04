from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
'''
  // written by: Mark Norfolk & Patrick Carra
  // tested by: Mark Norfolk & Patrick Carra
  // debugged by: Mark Norfolk & Patrick Carra
  // etc.
'''

urlpatterns = [
    path('', views.index, name='index'),
    path('faq/', views.faq, name='faq'),
    path('login/', views.login_request, name='login'),
    path('about-us/', views.about, name='about-us'),
    path('register/', views.register, name='register'),
    path('makereservation/', views.makeReservation.as_view(),name="makeReservation"),
    path('reservation/<int:pk>/', views.viewReservation.as_view(), name='viewReservation'),
    path('menu/', views.menu, name="menu" ),
    
    
]
