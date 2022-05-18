## We don't need render for REST API
# from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest.serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    '''
    CRUD endpoint for User model
    '''
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAdminUser]
    permission_classes = [permissions.AllowAny]

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    Admin read only endpointo for Group model
    '''
    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]