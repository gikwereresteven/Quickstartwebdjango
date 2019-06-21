from django.shortcuts import render
from quickstart import views
from django.contrib.auth.models import User, Group
from .models import Registration
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer, RegistrationSerializer

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from quickstart.serializers import RegistrationSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class RegistrationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

@csrf_exempt
def registration_list(request):
     """
     List all code quickstart, or create a new quickstart.
     """
     if request.method == 'GET':
         quickstart = Registration.objects.all()
         serializer = RegistrationSerializer(quickstart, many=True)
         return JsonResponse(serializer.data, safe=False)
         
     elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RegistrationSerializer(data=data)
     
        if  serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def registration_detail(request, pk):
    """
    Retrieve, update or delete a code registration.
    """
    try:
        quickstart = Registration.objects.get(pk=pk)
    except Registration.DoesNotExist:
        return HttpResponse(status=404)
    
    
    if request.method == 'GET':
            serializer = RegistrationSerializer(quickstart)
            return JsonResponse(serializer.data)

    elif request.method == 'PUT':
            data = JSONParser.parse(request)
            serializer = RegistrationSerializer(Registration,data=data)
    if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
                return JsonResponse(serializer.errors, satatus=400)
            
    elif request.method == 'DELETE':
            Registration.delete()
            return HttpResponse(status=202)


def homepage(request):
    return render(request,'quickstart/home.html',{})


