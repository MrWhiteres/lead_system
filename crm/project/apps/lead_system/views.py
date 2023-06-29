from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import AllowAny

from .serializers import ListLeadSerializer
from ...base_generic import base_views


class LeadAPI(base_views.BaseCreateAPIView):
    serializer_class = ListLeadSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs) -> JsonResponse:
        data = self.serializer_data(request.data)
        if not data:
            return JsonResponse(data={}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse(data={}, status=status.HTTP_200_OK)
