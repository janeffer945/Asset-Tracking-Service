from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200 )
    contact = models.CharField(max_length=100)
    def __str__(self):
        return self.name
 

class Employee(models.Model):

 name= models.ForeignKey(Company, on_delete=models.CASCADE )
 Username = models.CharField(max_length=100)
 full_name = models.CharField(max_length=200)
 Email = models.EmailField(null=True, blank=True)
 phone_number = models.IntegerField(null=True, blank=True)
  
 def __str__(self):
        return self.name

class Asset(models.Model):
 full_name = models.ForeignKey(Employee, on_delete=models.CASCADE)
 asset_type = models.CharField(max_length=100)
 asset_name = models.CharField(max_length=100) 
 asset_id = models.AutoField(primary_key=True)
 serial_number = models.IntegerField(null=True, blank=True)

 
