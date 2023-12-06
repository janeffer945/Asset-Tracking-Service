from . import views
from django.urls import include, path
from rest_framework import routers
from . import views
# from django.conf.urls import path


router = routers.DefaultRouter()
router.register(r'Companies',  views.CompaniesViewSet)
router.register(r'Employees',  views.EmployeesViewSet)
router.register(r'Devices', views.DevicesViewSet )
router.register(r'Device_log', views.Device_logViewSet )



urlpatterns = [
   
    path('', include(router.urls)),
    
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login', view='login', name= 'login')
]