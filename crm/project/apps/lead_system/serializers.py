from rest_framework import serializers

from .models import Lead


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('name', 'email', 'phone', 'ip_address')


class ListLeadSerializer(serializers.Serializer):
    leads = LeadSerializer(many=True)

    class Meta:
        fields = ('leads',)
