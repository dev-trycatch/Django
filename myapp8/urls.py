from django.urls import path
from .views import *
urlpatterns = [

    path('set-session',set_session,name = 'set_session'),
    path('get-session',get_session,name = 'get_session'),
    path('delete-session',delete_session,name = 'delete_session'),

    # path('set-cookie',set_cookie,name = 'set_cookie'),
    # path('get-cookie',get_cookie,name = 'get_cookie'),
    # path('delete-cookie',delete_cookie,name = 'delete_cookie'),    
]