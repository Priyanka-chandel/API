from django.shortcuts import render
from rest_framework import viewsets
from api.models import company,Employee
from api.Serializers import companySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class companyviewsets(viewsets.ModelViewSet):
    queryset=company.objects.all()
    serializer_class=companySerializer
    
    #companies/{companyId}/employees
 

    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            company_instance = company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company_instance)
            emps_serializer = EmployeeSerializer(emps, many=True, context={'request': request})

            if not emps:
                return Response({'message': 'No employees found for this company.'}, status=status.HTTP_404_NOT_FOUND)

            return Response(emps_serializer.data)
        
        except Exception as e:
            pass
            


class Employeeviewsets(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer