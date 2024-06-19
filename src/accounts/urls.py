from django.urls import path
from . import api

app_name = "accounts"

urlpatterns = [
    path("", api.UserListAPIView.as_view(), name="user-list"),
]
