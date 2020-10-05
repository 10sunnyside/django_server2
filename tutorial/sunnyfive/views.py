#views.py 
from django.shortcuts import render 
from django.http import HttpResponse, JsonResponse 
from django.views.decorators.csrf import csrf_exempt 
from .models import Sunnyfive 
from .serializers import SunnyfiveSerializer 
from rest_framework.parsers import JSONParser
from rest_framework import viewsets

# Create your views here. 

class SunnyViewSet(viewsets.ModelViewSet): 
    queryset = Sunnyfive.objects.all() 
    serializer_class = SunnyfiveSerializer



@csrf_exempt
def address_list(request): 
    if request.method == 'GET': 
        query_set = Sunnyfive.objects.all() 
        serializer = SunnyfiveSerializer(query_set, many=True) 
        return JsonResponse(serializer.data, safe=False) 
        
    elif request.method == 'POST': 
        data = JSONParser().parse(request) 
        serializer = SunnyfiveSerializer(data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400) 
        
@csrf_exempt 
def address(request, pk):
    
    obj = Sunnyfive.objects.get(pk=pk) 
    
    if request.method == 'GET': 
        serializer = SunnyfiveSerializer(obj) 
        return JsonResponse(serializer.data, safe=False) 
        
    elif request.method == 'PUT': 
        data = JSONParser().parse(request) 
        serializer = SunnyfiveSerializer(obj, data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse(serializer.data, status=201) 
        return JsonResponse(serializer.errors, status=400) 
        
    elif request.method == 'DELETE': 
        obj.delete() 
        return HttpResponse(status=204) 
        
@csrf_exempt 
def login(request): 
    if request.method == 'POST': 
        data = JSONParser().parse(request) 
        search_channel = data['channel']
        obj = Sunnyfive.objects.get(channel=search_channel)
        
        if data['id_name'] == obj.id_name:
            return HttpResponse(status=200) 
        else: 
            return HttpResponse(status=400)


def map(request):
    """View function for home page of site."""
    # Render the HTML template index.html with the data in the context variable
    mData = Sunnyfive.objects.all()
    serializer = SunnyfiveSerializer(mData, many=True) 
    context = {'mData':mData}
    return render(request, 'map.html', context)

