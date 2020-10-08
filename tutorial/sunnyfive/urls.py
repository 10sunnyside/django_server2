from django.urls import path
from sunnyfive import views
# Create your views here.
from django.conf.urls import url, include

urlpatterns = [
    #path('', views.map, name='map'),
    url(r'^$', views.mData_list.as_view(), name='mData_list'),
]
