from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import serializers
from .models import *
from .serializers import publisherserializer
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(['GET'])
def apioverview(req):
    api_urls={
        'getallpublisher':'/all/',
        'createpublisher':'create/',
    }
    return Response(api_urls)

@api_view(['POST'])
def add_publisher(request):
    publisher=publisherserializer(data=request.data)
    if(Publisher.objects.filter(**request.data)):
        serializers.ValidationError('data send before')
    else:
        if(publisher.is_valid()):
            publisher.save()
            return Response(publisher.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def list(request):
    Publishers=Publisher.objects.all()
    Publisherserialized=publisherserializer(Publishers,many=True)
    return Response(Publisherserialized.data)

@api_view(['POST'])
def searchbyname(request):
    inputdata=publisherserializer(request.data)
    objts=Publisher.objects.filter(name=inputdata.data['name'])
    print(objts)
    return Response(status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_publisher(request,pk):
    obj=get_object_or_404(Publisher,id=pk)
    obj.delete()
    return Response(status.HTTP_202_ACCEPTED)

@api_view(['PUT'])
def update_publisher(request,pk):
    obj=Publisher.objects.get(id=pk)
    data=publisherserializer(instance=obj,data=request.data)
    if(data.is_valid()):
        data.save()
        return Response(data.data)
    else:
        return Response(status.HTTP_404_NOT_FOUND)