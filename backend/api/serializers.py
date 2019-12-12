from rest_framework import serializers
from .models import User, UserTask


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name']


class UserTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTask
        fields = ['id', 'description', 'state', 'user_id']
