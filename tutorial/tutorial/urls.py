"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework import routers
from tutorial.quickstart import views
from django.conf.urls import url, include
from sunnyfive import views
from django.urls import path




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('sunnyfive/', views.address_list),
    path('sunnyfive/<int:pk>/', views.address),
    path('login/', views.login),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('sunnyfive2/', include('sunnyfive.urls')),
    path('mData/', include('sunnyfive.urls')), ]
