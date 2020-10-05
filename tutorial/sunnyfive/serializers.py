#serializers.py 
from rest_framework import serializers 
from .models import Sunnyfive 


class SunnyfiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sunnyfive 
        fields = ['name', 'location', 'address', 'id_name', 'channel']
