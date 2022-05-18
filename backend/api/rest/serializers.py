from django.contrib.auth.models import User, Group
from rest_framework import serializers
# from rest_framework import viewsets
# from rest_framework import permissions

class UserSerializer(serializers.ModelSerializer):
    '''
    Main User model serializer
    '''
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups', 'is_superuser', 'is_active']

class GroupSerializer(serializers.ModelSerializer):
    '''
    Main Group model serializer
    '''
    class Meta:
        model = Group
        fields = ['id', 'name']
