from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import api, views

app_name = "accounts"

router = DefaultRouter()
router.register(
    "",
    api.UserViewSet,
)

urlpatterns = [
    path("gen", api.UserListGenAPIView.as_view(), name="gen-user-list"),
    path("gen/<int:pk>", api.UserDetailGenAPIView.as_view(), name="gen-user-detail"),
    path("view", api.UserListAPIView.as_view(), name="view-user-list"),
    path(
        "view/<int:user_id>", api.UserDetailAPIView.as_view(), name="view-user-detail"
    ),
    path("mixin", api.UserLIstMixinAPIView.as_view(), name="mixin-user-list"),
    path(
        "mixin/<int:pk>",
        api.UserDetailMixinAPIView.as_view(),
        name="mixin-user-detail",
    ),
    path("viewset", include(router.urls)),
    path("fbv", views.get_user_list, name="fbv-user-list"),
    path("fbv/<int:user_id>", views.get_user_detail, name="fbv-user-detail"),
]
