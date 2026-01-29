from django.urls import path
from .views import *

# urlpatterns = [
#     path('public/',public_view,name='public_view'),
#     path('private/',private_view,name='private_view'),

# ]
# urlpatterns = [
#     path('blogs/',blog_list,name='blog_list'),

# ]


from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('get-token/',obtain_auth_token,name = 'api_token_auth'),
    path('profile/',user_profile,name = 'user_profile'),
    path('admin-panel/',admin_panel,name = 'admin_panel'),


]