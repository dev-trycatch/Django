from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import StudentSerializer

class StudentAPI(APIView):
    # read all or single data
    def get(self,request,pk=None):
        if pk:
            try:
                student = Student.objects.get(pk= pk)
                serializer = StudentSerializer(student)
                return Response(serializer.data,status = status.HTTP_200_OK)
            except Student.DoesNotExist:
                return Response({'Error':'student not found'},status = status.HTTP_200_OK)
        else:
            student = Student.objects.all()
            serializer = StudentSerializer(student,many = True)
            return Response(serializer.data,status = status.HTTP_200_OK)
        

    # create data
    def post(self,request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    # update data 
    def put(self,request,pk):
        try:
            student = Student.objects.get(pk= pk)
        except Student.DoesNotExist:
            return Response({'Error':'student not found'},status = status.HTTP_200_OK)

        serializer = StudentSerializer(student,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_200_OK)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        try:
            student = Student.objects.get(pk= pk)
            student.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            return Response({'Error':'student not found'},status = status.HTTP_200_OK)
        


        

        
        