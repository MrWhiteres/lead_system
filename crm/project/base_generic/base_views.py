from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView,
    UpdateAPIView, DestroyAPIView,
    ListAPIView,
)
from rest_framework.views import (
    APIView
)


class BaseAPIView(APIView):
    """
    Base parent view
    """
    permission_classes = []
    serializer_class = []

    def serializer_data(self, data: dict) -> dict | bool:
        """
        Base serializer method
        :param data:
        :return: dict or boolean
        """
        for serializer in self.serializer_class:
            data_serialize = serializer(data=data)
            if data_serialize.is_valid():
                return {**data_serialize.data}
        return False


class BaseCreateAPIView(BaseAPIView, CreateAPIView):
    """
    Base create API view class
    """

    def post(self, request, *args, **kwargs):
        """Base post method"""


class BaseGetAPIView(BaseAPIView, RetrieveAPIView):
    """
    Base get API view class
    """

    def get(self, request, *args, **kwargs):
        """Base get method"""


class BaseUpdateAPIView(BaseAPIView, UpdateAPIView):
    """
    Base update API view class
    """

    def put(self, request, *args, **kwargs):
        """Base put method"""


class BaseDeleteAPIView(BaseAPIView, DestroyAPIView):
    """
    Base delete API view class
    """

    def delete(self, request, *args, **kwargs):
        """Base delete method"""


# pylint: disable=too-many-ancestors
class BaseCreateGetAPIView(BaseGetAPIView, RetrieveAPIView):
    """
    Base create get API view class
    """

    def get(self, request, *args, **kwargs):
        """Base get method"""

    def post(self, request, *args, **kwargs):
        """Base post method"""


# pylint: disable=too-many-ancestors
class BaseUpdateGetAPIView(BaseGetAPIView, UpdateAPIView):
    """
    Base update get API view class
    """

    def get(self, request, *args, **kwargs):
        """Base get method"""

    def put(self, request, *args, **kwargs):
        """Base put method"""


# pylint: disable=too-many-ancestors
class BaseDeleteGetAPIView(BaseDeleteAPIView, DestroyAPIView):
    """
    Base delete get API view class
    """

    def get(self, request, *args, **kwargs):
        """Base get method"""

    def delete(self, request, *args, **kwargs):
        """Base delete method"""


class BaseListAPIView(BaseAPIView, ListAPIView):
    """
    Base list API view class
    """

    def get(self, request, *args, **kwargs):
        """Base get method"""

    def post(self, request, *args, **kwargs):
        """Base post method"""

    def put(self, request, *args, **kwargs):
        """Base put method"""

    def delete(self, request, *args, **kwargs):
        """Base delete method"""
