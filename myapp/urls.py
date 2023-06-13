from . import views
from django.urls import include, path
from rest_framework import routers
from . import views
# from django.conf.urls import path
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Corporate App Track APIs')


router = routers.DefaultRouter()
router.register(r'Companies',  views.CompaniesViewSet)
router.register(r'Employees',  views.EmployeesViewSet)
router.register(r'Devices', views.DevicesViewSet )
router.register(r'Device_log', views.Device_logViewSet )

schema_view = get_swagger_view(title='Corporate App Track APIs')
urlpatterns = [
   
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]