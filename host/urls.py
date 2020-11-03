from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'host'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cancel_reservation/<int:pk>/',views.cancelReservation, name="cancel_reservation"),
    path('profile/', views.profile, name='profile'),
    path('error/', views.error, name='error'),
    path('order/', views.order, name='order'),
    path('delete_order/<int:pk>/', views.cancelOrder, name="cancel_order"),
    path('additems/<int:pk>/', views.addItems, name="additems"),
    path('delete_item/<int:pk>/', views.deleteItem, name="delete_item"),
    path('total/<int:pk>/', views.total, name="total"),
    path('complaints/', views.create.as_view(), name='complaints'),
    path('information/', views.information, name='information'),
    path('tables/', views.tables.as_view(), name='tables'),
    # path('add-table/', views.addTable.as_view(), name='add-table'),
]