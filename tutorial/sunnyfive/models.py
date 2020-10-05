#models.py 
from django.db import models 
class Sunnyfive(models.Model): 
    name = models.CharField(max_length=10)
    location = models.CharField(max_length=13)
    address = models.TextField()
    id_name = models.CharField(max_length=10)
    channel = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    
class Meta: 
    ordering = ['created']

