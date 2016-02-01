from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.models import User
from myapp.models import Project, Task


class UserRegistrationSerializer(serializers.Serializer):
    """
    """
    password = serializers.CharField(max_length=20, required=True, write_only=True)
    email = serializers.CharField(max_length=20, required=True)
    username = serializers.CharField(max_length=20, required=True)


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    """
    """
    created_by = serializers.CharField(max_length=20, required=False)

    class Meta:
        model = Project
        exclude = ('created_by_id',)

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    """
    """
    created_by = serializers.CharField(max_length=20, required=False)

    class Meta:
        model = Task
        exclude = ('created_by_id',)
