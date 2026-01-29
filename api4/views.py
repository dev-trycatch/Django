# from django.shortcuts import render
# from rest_framework.decorators import api_view,permission_classes
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated,AllowAny


# # Create your views here.
# # public view accessible without authentication 

# @api_view(['GET'])
# @permission_classes([AllowAny])
# def public_view(request):
#     return Response({'Message':'This is a public view Accesible to everyone.'})


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def private_view(request):
#     return Response({'Message':f'Hello,{request.user.username}.This is a private view Accesible to only to authenticated users.'})



# Sessoion  start
# from rest_framework.decorators import api_view,permission_classes
# from rest_framework.response import Response
# from .models import *
# from .serializers import BlofSerializer
# from rest_framework import status

# @api_view(['GET',"POST"])
# def blog_list(request):
#     if request.method == "GET":
#         blogs = Blog.objects.all()
#         serializer = BlofSerializer(blogs,many = True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = BlofSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status= status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



from rest_framework.decorators import authentication_classes,permission_classes,api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

# api only for authenticated users

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user
    return Response({
        "username":user.username,
        "email":user.email,
        "is_staff":user.is_staff,
    })

# api only for admin users
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def admin_panel(request):
    return Response({"message":f"Welcome to the admin panel, {request.user.username}"})