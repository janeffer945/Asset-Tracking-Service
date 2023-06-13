from django.contrib import admin
from .models import Companies, Employees, Devices, Device_log
# Register your models here.
admin.site.register(Companies)
admin.site.register(Employees)
admin.site.register(Devices)
admin.site.register(Device_log)
