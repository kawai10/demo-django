from rest_framework.generics import ListAPIView

from src.accounts.models import User
from src.accounts.serializer import UserSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all().defer("password")
    serializer_class = UserSerializer
