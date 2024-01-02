from django.contrib import admin
from django.urls import path,include
from api.views import companyviewsets,Employeeviewsets
from rest_framework import routers
from .views import YourViewSetClass


router=routers.DefaultRouter()
router.register(r'companies',companyviewsets)
router.register(r'employees',Employeeviewsets)
router.register(r'your-endpoint', YourViewSetClass,)


urlpatterns = [
    path('',include(router.urls))
]