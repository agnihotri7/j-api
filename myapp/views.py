import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, status, filters, mixins, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User

from myapp.models import Project, Task
from myapp.serializers import UserRegistrationSerializer, ProjectSerializer, TaskSerializer
from collegedekho.permissions import IsProjectOwner, IsTaskMemberOwner


class ProjectViewSet(viewsets.ModelViewSet):
    """
    """
    model = Project
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsProjectOwner]
    parser_classes = (JSONParser,)

    def pre_save(self, obj, created=False):
        if created:
            obj.created_by = self.request.user
            obj.save()

class TaskViewSet(viewsets.ModelViewSet):
    """
    """
    model = Task
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsTaskMemberOwner]
    parser_classes = (JSONParser,)

    def pre_save(self, obj, created=False):
        if created:
            obj.created_by = self.request.user

class UserViewSet(viewsets.ModelViewSet):
    """
    """
    model = User
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated,]
    parser_classes = (JSONParser,)


@api_view(['POST'])
def create_auth(request):
    """
    """
    serialized = UserRegistrationSerializer(data=request.DATA)

    if serialized.is_valid():
        User.objects.create_user(
            serialized.init_data['email'],
            serialized.init_data['username'],
            serialized.init_data['password']
        )
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
