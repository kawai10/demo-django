from django.db.models import QuerySet
from rest_framework import serializers

from src.accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserListSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "name"]

    @staticmethod
    def get_queryset() -> QuerySet[User]:
        return User.objects.all().only("id", "email", "name")


class UserDetailSerializer(UserSerializer):
    class Meta:
        model = User
        exclude = ["password"]

    @staticmethod
    def get_queryset() -> QuerySet[User]:
        return User.objects.all().defer("password")
