from django.db.models import indexes
from django.urls import path
from .views import EmployeeAPIView, EmployeeDetail
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('api/Employee/', EmployeeAPIView.as_view()),
    path('api/Employee/<int:pk>', EmployeeDetail.as_view()),
    path('api/save/', views.save, name='save'),
    path('api/delete/', views.delete_data, name='delete_data'),
    path('api/edit/', views.edit_data, name='edit_data'),

]
