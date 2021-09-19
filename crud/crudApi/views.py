from crudApi.forms import EmployeeRegistration
from django.http.response import JsonResponse
from crudApi import models
from crudApi.models import Employee
from django.shortcuts import render ,redirect
<<<<<<< HEAD
from rest_framework import generics
from .serializers import EmployeeSerializer
from crudApi.forms import EmployeeRegistration
from rest_framework.decorators import (api_view, authentication_classes, permission_classes)
=======

>>>>>>> 58128533b0fef8faead8cfb03148f6da5c1b2288


def index(request):  
    employees = Employee.objects.all()  
<<<<<<< HEAD
    form = EmployeeRegistration()
    return render(request,"index.html",{'employees':employees, 'form':form})

@api_view(["POST"])
def save(request):
    if request.method == "POST":
        form = EmployeeRegistration(request.POST)
        if form.is_valid():
            id = request.POST['id']
            name = request.POST['name']
            email = request.POST['email']
            task = request.POST['task']
            if id == "":
                usr = Employee(name = name, email=email, task=task)
            else:
                usr = Employee(id = id, name = name, email=email, task=task)
            usr.save()
            emp = Employee.objects.values()
            # print(emp)
            Employee_data = list(emp)
            return JsonResponse({'status':'Save', 'employee_data':Employee_data})
        else:
            return JsonResponse({'status':'Not Save'})


@api_view(["POST"])
def delete_data(request):
    if request.method == "POST":
        id = request.POST.get('id')
        print(id)
        pi = Employee.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})


@api_view(["POST"])
def edit_data(request):
    if request.method == "POST":
        id = request.POST.get('id')
        print(id)
        em = Employee.objects.get(pk=id)
        em_data = {"id":em.id, "name":em.name, "email":em.email,
        "task":em.task}
        return JsonResponse(em_data)
    else:
        return JsonResponse({'status':0})
=======
    return render(request,"index.html",{'employees':employees})

def get_data(request):  
    employees = Employee.objects.values()
    emp = list(employees)
    return JsonResponse({'status':"ok", 'emp':emp})


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
>>>>>>> 58128533b0fef8faead8cfb03148f6da5c1b2288



