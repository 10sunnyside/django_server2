# models.py
from django.db import models


class Sunnyfive(models.Model):
    lat = models.DecimalField(max_digits=10, decimal_places=6, null=True,default='')
    lng = models.DecimalField(max_digits=10, decimal_places=6, null=True,default='')
    url = models.CharField(max_length=100, null=True,default='')
    title = models.CharField(max_length=70, null=True,default='')
    nation = models.CharField(max_length=30, null=True,default='')
    # location = models.CharField(max_length=13)
    # address = models.TextField()
    # id_name = models.CharField(max_length=10)
    # channel = models.CharField(max_length=10)
    # created = models.DateTimeField(auto_now_add=True)


class Meta:
    ordering = ['created']

