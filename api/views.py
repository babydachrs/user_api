from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import UserSerializer
from .models import User

# Create your views here.
"""@api_view(['GET'])
def apiOverview(request):
    api_urls = {
    'List': '/user-list/',
    'Detail View': '/user-detail/<int:id>',
    'Create': '/user-create/',
    'Update': '/user-update/',
    'Delete': '/user-delete/',
    }

    return Response(api_urls):
"""
@api_view(['GET'])
def ShowAll(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)  

@api_view(['GET'])
def ViewUser(request,pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)       

@api_view(['POST'])
def CreateUser(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)  

@api_view(['POST'])
def UpdateUser(request):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)         


@api_view(['GET'])
def DeleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return Response('Items delete successfully')   