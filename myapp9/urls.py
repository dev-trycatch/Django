# from django.urls import path
# from . import views

# urlpatterns = [
#     path('bulk-email/',views.send_bulk_email,name='bulk-email'),

   
# ]

from django.urls import path
from .views import register, success

urlpatterns = [
    path('register/', register, name='register'),
    path('success/', success, name='success'),
]
