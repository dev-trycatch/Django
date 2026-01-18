from django.urls import path
from .views import *

urlpatterns = [
    path('students/',get_students,name='get_students'),
    path('students/add/',add_students,name='add_students'),
]