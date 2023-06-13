from django.db import models
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver




# model to create company 
class Companies(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.name 
    
#model to employee
class Employees(models.Model ):
 id = models.AutoField(primary_key=True)  
 company = models.ForeignKey(Companies, on_delete=models.CASCADE)
 username = models.CharField(max_length=100)
 full_name = models.CharField(max_length=200)
 email = models.EmailField(null=False, blank=False)
 phone_number = models.IntegerField(null=False, blank=False)
 date_created = models.DateTimeField(auto_now_add=True) 
 
 
 def __str__(self):
        return self.full_name

#model to create device
class Devices(models.Model):
 id = models.AutoField(primary_key=True)
 employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
 type = models.CharField(max_length=100)
 name = models.CharField(max_length=100) 
 mac_address = models.CharField(max_length=100, null=False, blank=False)
 date_created = models.DateTimeField(auto_now_add=True)
 def __str__(self):
        return self.name

#model to track devices
class Device_log(models.Model):
   id = models.AutoField(primary_key=True)
   device = models.ForeignKey(Devices, on_delete=models.CASCADE)
   description = models.TextField()
   issued_to = models.ForeignKey(Employees, on_delete=models.CASCADE)
   date_issued = models.DateTimeField(auto_now_add=True)
   date_returned = models.DateTimeField(auto_now_add=True)


 
