from dataclasses import fields
from turtle import title
from rest_framework import serializers

from django.contrib.auth.models import User, Group
from inspections.models import Inspection, Inspector, Item

class InspectionSerializer (serializers.ModelSerializer):
    '''
    Serializer for required inspections endpoint
    '''
    class Meta:
        model = Inspection
        fields = ['title', 'inspectorName', 'itemsOk', 'issuesWarningcount', 'issuesCriticalCount', 'Company' ]

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
