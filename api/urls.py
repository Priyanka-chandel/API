from django.contrib import admin
from django.urls import path,include
from api.views import companyviewsets,Employeeviewsets
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'companies',companyviewsets)
router.register(r'employees',Employeeviewsets)


urlpatterns = [
    path('',include(router.urls))
]