from crudApi.forms import EmployeeRegistration
from django.http.response import JsonResponse
from crudApi import models
from crudApi.models import Employee
from django.shortcuts import render ,redirect



def index(request):  
    employees = Employee.objects.all()  
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



