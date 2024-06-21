from django.db.models import QuerySet
from rest_framework import serializers

from src.accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    @staticmethod
    def get_queryset() -> QuerySet[User]:
        return User.objects.all()


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["created_at", "updated_at"]
        extra_kwargs = {"password": {"write_only": True}}

    @staticmethod
    def get_queryset() -> QuerySet[User]:
        return User.objects.all().defer("password")


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = ["id", "created_at"]

    @staticmethod
    def get_queryset() -> QuerySet[User]:
        return User.objects.all().defer("password")
