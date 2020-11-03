from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'manager'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('restock/', views.restock, name='restock'),
    path('error/', views.error, name='error'),
    path('employees/', views.employees, name='employees'),
    # path('business/', views.business, name='business'),
    path('income/', views.income.as_view(), name='income'),
    path('business/', views.business.as_view(), name='business'),
    path('complaints/', views.complaints, name='complaints'),
    path('requests/', views.requests.as_view(), name='requests'),
    path('completerequest/<int:pk>', views.completeRequest, name='completerequest'),
]
