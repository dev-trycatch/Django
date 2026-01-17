from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home,name = 'home'),
    # path('clear_data/',clear_data,name = 'clear_data'),
    path('show_data/',show_data,name = 'show_data'),
    path('data/<id>',data,name = 'data'),
]
