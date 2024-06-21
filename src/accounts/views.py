from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response

from src.accounts.models import User
from src.accounts.serializer import UserListSerializer, UserDetailSerializer


@api_view(["GET"])
def get_user_list(request: Request) -> Response:
    user_queryset = User.objects.all().defer("password")
    user_serializer = UserListSerializer(user_queryset, many=True)
    return Response(user_serializer.data)


@api_view(["GET"])
def get_user_detail(request: Request, user_id: int) -> Response:
    user_detail = get_object_or_404(User, pk=user_id)
    user_serializer = UserDetailSerializer(user_detail)
    return Response(user_serializer.data)
