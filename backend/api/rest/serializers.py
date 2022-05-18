from rest_framework import serializers

from inspections.models import Inspection

class InspectionSerializer (serializers.ModelSerializer):
    '''
    Serializer for required inspections endpoint
    '''
    class Meta:
        model = Inspection
        fields = ['title', 'inspectorName', 'itemsOk', 'issuesWarningCount', 'issuesCriticalCount', 'Company' ]