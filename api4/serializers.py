from .models import *
from rest_framework import serializers

class BlofSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

