from rest_framework import serializers
from .models import User, UserTask


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name']


class UserTaskSerializer(serializers.ModelSerializer): 
    class Meta:
        model = UserTask
        fields = ['id', 'description', 'state']

class UserandTasksSerializer(serializers.ModelSerializer):
    user_id = UserSerializer(many=False, read_only=True)    
    class Meta:
        model = UserTask
        fields = ['id', 'user_id', 'description', 'state']
