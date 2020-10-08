#serializers.py 
from rest_framework import serializers 
from .models import Sunnyfive 


class SunnyfiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sunnyfive 
        fields = ['lat', 'lng', 'url', 'title', 'nation']
