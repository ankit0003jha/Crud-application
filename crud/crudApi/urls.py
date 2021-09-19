from django.db.models import indexes
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
<<<<<<< HEAD
    path('api/Employee/', EmployeeAPIView.as_view()),
    path('api/Employee/<int:pk>', EmployeeDetail.as_view()),
    path('api/save/', views.save, name='save'),
    path('api/delete/', views.delete_data, name='delete_data'),
    path('api/edit/', views.edit_data, name='edit_data'),
=======
    path('get/', views.get_data, name="get_data"),
    path('addnew',views.addnew, name='addnew'),  
    path('edit/<int:id>', views.edit, name='edit'),  
    path('update/<int:id>', views.update, name='update'),  
    path('delete/<int:id>', views.destroy, name='destroy'),  
>>>>>>> 58128533b0fef8faead8cfb03148f6da5c1b2288

]
