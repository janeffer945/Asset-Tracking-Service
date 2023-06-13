from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CompaniesSerializer, EmployeesSerializers, DevicesSerializers, Device_logSerializers
from .models import Companies, Employees, Devices, Device_log
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.http import HttpResponse, HttpResponseRedirect

@receiver(post_save, sender=Employees)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# from django.contrib.auth.models import  
class CompaniesViewSet(viewsets.ModelViewSet):
    queryset =Companies.objects.all().order_by('name')
    serializer_class =CompaniesSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializers 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
class DevicesViewSet(viewsets.ModelViewSet):
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
class Device_logViewSet(viewsets.ModelViewSet):
    queryset = Device_log.objects.all()
    serializer_class = Device_logSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
