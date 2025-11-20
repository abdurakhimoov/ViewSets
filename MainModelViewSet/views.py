from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import CompanySerializer, EmployeeSerializer
from .models import Company, Employee


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True, methods=['GET'])
    def employees(self, request, pk=None):
        company = self.get_object()
        employees = company.employees.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET'])
    def company_high_salary(self, request, pk=None):
        company = self.get_object()
        employees = company.employees.filter(salary__gte=400)
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def count_employees(self, request, pk=None):
        company = self.get_object()
        employee_count = company.employees.count()
        return Response({'company_id': pk, 'employee_count': employee_count}, status=status.HTTP_200_OK)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @action(detail=False, methods=['GET'])
    def high_salary(self, request):
        high_salary = Employee.objects.filter(salary__gte=1000)
        ser = EmployeeSerializer(high_salary, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['GET'])
    def employees_count(self, request):
        employees_count = Employee.objects.count()
        return Response({'employees_count': employees_count}, status=status.HTTP_200_OK)