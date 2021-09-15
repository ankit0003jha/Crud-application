from django.http.response import JsonResponse
from crudApi import models
from crudApi.models import Employee
from django.shortcuts import render ,redirect
from rest_framework import generics
from .serializers import EmployeeSerializer
from crudApi.forms import EmployeeRegistration


def index(request):  
    employees = Employee.objects.all()  
    return render(request,"index.html",{'employees':employees})


def addnew(request):  
    if request.method == "POST":  
        form = EmployeeRegistration(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass 
    else:  
        form = EmployeeRegistration()  
    return render(request,'add.html',{'form':form})  

def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  


def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeRegistration(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect('/')  
    return render(request, 'edit.html', {'employee': employee})  


def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/")  


class EmployeeAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

