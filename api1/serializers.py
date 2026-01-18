from rest_framework import routers, serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ['age','city']
        fields = '__all__'
