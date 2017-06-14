from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *




class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = tutorial
        fields = ('__all__')