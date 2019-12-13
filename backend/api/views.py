from django.shortcuts import render

from rest_framework import generics, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import User, UserTask
from .serializers import UserSerializer, UserTaskSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    This view handles all about user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserTaskViewSet(viewsets.ModelViewSet):
    """
    This view handles all about tasks
    """
    queryset = UserTask.objects.all()
    serializer_class = UserTaskSerializer

class UserandTasksView(generics.ListAPIView):
    queryset = UserTask.objects.all()
    serializer_class = UserTaskSerializer
# Create your views here.
