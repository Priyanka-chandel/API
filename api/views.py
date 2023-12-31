from django.shortcuts import render
from rest_framework import viewsets
from api.models import company,Employee
from api.Serializers import companySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Create your views here.

class companyviewsets(viewsets.ModelViewSet):
    queryset=company.objects.all()
    serializer_class=companySerializer
    
    #companies/{companyId}/employees
 

    # @action(detail=True, methods=['get'])
    # def employees(self, request, pk=None):
    #     try:
    #         company_instance = company.objects.get(pk=pk)
    #         emps = Employee.objects.filter(company=company_instance)
    #         emps_serializer = EmployeeSerializer(emps, many=True, context={'request': request})

    #         if not emps:
    #             return Response({'message': 'No employees found for this company.'}, status=status.HTTP_404_NOT_FOUND)

    #         return Response(emps_serializer.data)
        
    #     except Exception as e:
    #         pass

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        success_message = 'Company created successfully.'
        headers = self.get_success_headers(serializer.data)
        return Response({'message': success_message, 'data': serializer.data}, status=status.HTTP_201_CREATED, headers=headers)

    


class YourViewSetClass(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @action(detail=True, methods=['post'])
    def employees(self, request, pk=None):
        try:
            company_instance = company.objects.get(pk=pk)
            employee_data = request.data
            employee_data['company'] = company_instance.id

            new_employee = Employee.objects.create(**employee_data)
            new_employee_serializer = EmployeeSerializer(new_employee, context={'request': request})
            
            return Response(new_employee_serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            pass


class Employeeviewsets(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
