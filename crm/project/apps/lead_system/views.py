from django.http import JsonResponse
from rest_framework.permissions import AllowAny

from .serializers import LeadSerializer, ListLeadSerializer
from ...base_generic import base_views


class LeadAPI(base_views.BaseCreateGetAPIView):
    serializer_class = [LeadSerializer, ListLeadSerializer]
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs) -> JsonResponse:
        return JsonResponse(data={}, status=200)
