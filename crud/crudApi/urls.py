from django.db.models import indexes
from django.urls import path
from .views import EmployeeAPIView, EmployeeDetail
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('api/Employee/', EmployeeAPIView.as_view()),
    path('api/Employee/<int:pk>', EmployeeDetail.as_view()),
    path('addnew',views.addnew, name='addnew'),  
    path('edit/<int:id>', views.edit, name='edit'),  
    path('update/<int:id>', views.update, name='update'),  
    path('delete/<int:id>', views.destroy, name='destroy'),  

]
