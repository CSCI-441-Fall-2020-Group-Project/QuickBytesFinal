from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'server'
urlpatterns = [
  path('dashboard/', views.dashboard, name='dashboard'),
  path('profile/', views.profile, name='profile'),
  path('error/', views.error, name='error'),
  path('order/', views.order, name='order'),
  path('alerts/', views.alerts, name='alerts'),
  path('tableclean/', views.tableclean, name='tableclean'),
  path('delete_order/<int:pk>/', views.cancelOrder, name="cancel_order"),
  path('additems/<int:pk>/', views.addItems, name="additems"),
  path('delete_item/<int:pk>/', views.deleteItem, name="delete_item"),
  path('total/<int:pk>/', views.total, name="total"),
  path('tables/', views.tables.as_view(), name="tables"),
  path('setdirty/<int:pk>', views.setDirty, name="setdirty"),
]
