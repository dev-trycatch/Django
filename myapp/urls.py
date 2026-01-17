from django.urls import path
from .views import *

urlpatterns = [
    path('receipe/',receipe,name = 'receipe'),
    path('login/',login_page,name = 'login_page'),
    path('logout/',logout_page,name = 'logout_page'),
    path('register/',register,name = 'register'),
    path('receipe/',receipe,name = 'receipe'),
    path('delete-receipe/<id>',delete_recipe,name = 'delete_recipe'),
    path('update-receipe/<id>',update_recipe,name = 'update_recipe'),
]
