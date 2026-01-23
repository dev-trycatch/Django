from django.urls import path
from .views import StudentAPI

urlpatterns = [
    path('students/',StudentAPI.as_view()), # for get (all) & postand 
    path('students/<int:pk>',StudentAPI.as_view(),) # for Get (single),Put,Delete

]