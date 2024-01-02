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

@csrf_exempt  # Only use this decorator if you want to disable CSRF protection for this view
@require_POST
def login_view(request):
    # Assuming successful user login
    success_message = 'User Successfully Logged In'

    # Create a dictionary with the desired structure
    response_data = {
        'status': True,
        'message': success_message,
        'code': 200
    }

    # Convert the dictionary to a JSON response
    return JsonResponse(response_data, status=200)
class Employeeviewsets(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
