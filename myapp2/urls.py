from django.urls import path
from .views import *

urlpatterns = [
    path('add/',student_create,name = 'student_create'),
    path('',student_list,name = 'student_list'),
    path('detail/<int:pk>',student_detail,name = 'student_detail'),
    path('edit/<int:pk>',student_edit,name = 'student_edit'),
    path('delete/<int:pk>',student_delete,name = 'student_delete'),
    
]
