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

    def is_valid(self, raise_exception=False):
        is_valid = super().is_valid(raise_exception=False)
        validated_leads = []

        for lead_data in self.initial_data.get('leads', []):
            lead_serializer = LeadSerializer(data=lead_data)
            if not lead_serializer.is_valid():
                continue
            validated_leads.append({**lead_serializer.validated_data})

        self._validated_data = {'leads': validated_leads}
        self._errors = {}

        if not is_valid:
            self._errors['leads'] = self.errors
        return is_valid or len(validated_leads) > 0

# {
#     "leads": [{"name": 4565, "email": "a@a.com","phone": 6546464, "ip_address": "89.0.142.86"},{"name": 4565, "email": "a@a.com","phone": 6546464, "ip_address": "89.0.142.86"}]
# }
