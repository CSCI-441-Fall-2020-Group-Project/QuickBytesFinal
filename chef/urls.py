from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'chef'
urlpatterns = [
    path('<int:pk>/', views.viewOrder.as_view(), name='viewOrder'),
    path('sendback/<int:pk>/', views.sendBack.as_view(), name='sendBack'),
    path('dashboard/', views.dashboard.as_view(), name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('complaints/', views.create.as_view(), name='complaints'),
    path('returns/', views.returns, name='returns'),
    path('error/', views.error, name='error'),
    path('completeOrder/<int:pk>/', views.completeOrder, name='completeOrder'),
    ]
