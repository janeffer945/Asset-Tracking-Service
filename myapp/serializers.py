from rest_framework import serializers
from .models import Companies, Employees, Devices, Device_log 

#serializes data from companies model 
class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = ['id', 'name', 'email', 'date_created']


#serializes data from employees model
class EmployeesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['id', 'company', 'username', 'full_name', 'email', 'phone_number', 'date_created']


#serializes data from devices model
class DevicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = ['id', 'employee', 'type', 'name', 'mac_address', 'date_created']        


#serializes data from device log model
class Device_logSerializers(serializers.ModelSerializer):
    class Meta:
        model = Device_log
        fields = ['id', 'device', 'issued_to', 'date_returned', 'date_issued', 'description']