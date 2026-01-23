from django.urls import path
from .views import *

urlpatterns = [
    path('students/',get_students,name='get_students'),
    path('students/add/',add_students,name='add_students'),
    path('students/update/<int:pk>',update_student,name='update_student'),
    path('students/delete/<int:pk>',delete_student,name='delete_student'),
]