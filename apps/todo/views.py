from django.shortcuts import render


from .models import Task
from .serializers import TaskSerializer

from rest_framework import viewsets
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated


class TaskViewSet(viewsets.ModelViewSet):
    #authentication_classes = (BaseAuthentication,)
    #permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer