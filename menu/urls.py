from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'menu'

urlpatterns = [
    
    # /menu/
    url(r'^$', views.index, name="index"),
    #url(r'^(?P<menu_item_id>[0-9]+)$', views.item_detail, name="item_detail"),
    path('additem', views.createItem.as_view()),
    #path('edititem', views.editItem.as_view()),
]


