from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'busser'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('complaints/', views.create.as_view(), name='complaints'),
    path('error/', views.error, name='error'),
    path('supplies/', views.supplies.as_view(), name='supplies'),
    path('queue/', views.queue.as_view(), name='queue'),
    path('makeclean/<int:pk>', views.makeClean, name='makeclean'),
    # path('add-table/', views.addTable.as_view(), name='add-table'),
]
