from django.http import Http404
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.accounts.models import User
from src.accounts.serializer import (
    UserListSerializer,
    UserDetailSerializer,
    UserSerializer,
)


# APIView
class UserListAPIView(APIView):
    @staticmethod
    def get(request: Request) -> Response:
        user_queryset = User.objects.all()
        user_serializer = UserListSerializer(user_queryset, many=True)
        return Response(user_serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request: Request) -> Response:
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPIView(APIView):

    def _get_object(self, user_id) -> User:
        return get_object_or_404(User, pk=user_id)

    def get(self, reqeust: Request, user_id: int) -> Response:
        user_object = self._get_object(user_id)
        user_serializer = UserDetailSerializer(user_object)
        return Response(user_serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, user_id: int):
        user_object = self._get_object(user_id)
        user_serializer = UserSerializer(user_object, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request: Request, user_id: int):
        user_object = self._get_object(user_id)
        user_serializer = UserSerializer(user_object, data=request.data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# GEN APIView
class UserListGenAPIView(ListAPIView):
    queryset = UserListSerializer.get_queryset()
    serializer_class = UserListSerializer


class UserDetailGenAPIView(RetrieveAPIView):
    queryset = UserDetailSerializer.get_queryset()
    serializer_class = UserDetailSerializer
