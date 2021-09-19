from django import forms
from django.forms import widgets
from .models import Employee

class EmployeeRegistration(forms.ModelForm):
    class Meta:
        model = Employee
<<<<<<< HEAD
        fields = ['id', 'name', 'email', 'task']
=======
        fields = ['name', 'email', 'task', 'designation']
>>>>>>> 58128533b0fef8faead8cfb03148f6da5c1b2288
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'id':'txtName'}),
             'email':forms.EmailInput(attrs={'class':'form-control', 'id':'txtEmailid'}),
              'task':forms.TextInput(attrs={'class':'form-control', 'id':'txtTask'}),
               'designation':forms.TextInput(attrs={'class':'form-control', 'id':'txtDesignation'}),

        }