## We don't need render for REST API
# from django.shortcuts import render

from rest_framework import permissions, generics

from inspections.models import Inspection
from rest.serializers import InspectionSerializer

class InspectionList(generics.ListAPIView):
    '''
    Required inspections endpoint
    '''
    serializer_class = InspectionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        company = self.request.query_params.get('company')
        queryset = Inspection.objects.filter(Company=company)
        return queryset