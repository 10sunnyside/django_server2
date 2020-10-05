from django.urls import path
from sunnyfive import views
# Create your views here.


urlpatterns = [
    path('', views.map, name='map'),
]
