from rest_framework import serializers

from .logic.get_leads import get_all_leads
from .models import Lead
from .serializer_utils.validate import validator_lead


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('name', 'email', 'phone', 'ip_address')

    def is_valid(self, *, leads, raise_exception=False):
        data = self.initial_data
        data, have_error = validator_lead(data, leads)
        if have_error:
            self._errors = data
            return False
        self._validated_data = self.initial_data
        return True


class ListLeadSerializer(serializers.Serializer):
    leads = LeadSerializer(many=True)

    class Meta:
        fields = ('leads',)

    def is_valid(self, raise_exception=False):
        is_valid = super().is_valid(raise_exception=False)
        validated_leads = []
        errors_leads = []
        if len(data := self.initial_data.get('leads', [])) == 0:
            self._errors['leads'] = ['Empty leads']
            return False
        leads = get_all_leads()
        for lead_data in data:
            lead_serializer = LeadSerializer(data=lead_data)
            if not lead_serializer.is_valid(leads=leads):
                errors_leads.append(lead_serializer.errors)
                continue
            validated_leads.append({**lead_serializer.validated_data})
        if len(validated_leads) == 0:
            self._errors['leads'] = errors_leads
            return False
        self._validated_data = {'leads': validated_leads}
        if not is_valid:
            self._errors['leads'] = self.errors
        return is_valid or len(validated_leads) > 0

# {
#     "leads": [{"name": 4565, "email": "a@a.com","phone": 26565466546, "ip_address": "89.0.142.86"},{"name": 26565466546, "email": "a@a.com","phone": 6546464, "ip_address": "89.0.142.86"}]
# }
