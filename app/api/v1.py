from rest_framework import routers
from routes.groups.views import GroupViewSet
from routes.subjects.views import SubjectViewSet
from routes.tasks.views import TaskViewSet
from routes.users.views import UserViewSet
from routes.me.views import MyProfileViewSet, MyPasswordView

from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from app.utils.decorated_jwt_views import (
    DecoratedTokenObtainPairView,
    DecoratedTokenRefreshView,
)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"groups", GroupViewSet)
router.register(r"subjects", SubjectViewSet)
router.register(r"tasks", TaskViewSet)
router.register(r"users", UserViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Tasks API",
        default_version="v1",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(
        "^swagger(?P<format>.json|.yaml)$",
        schema_view.without_ui(),
        name="schema-json",
    ),
    path(
        "swagger",
        schema_view.with_ui("swagger"),
        name="schema-swagger-ui",
    ),
    path("redoc", schema_view.with_ui("redoc"), name="schema-redoc"),
    *router.urls,
    path("token", DecoratedTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", DecoratedTokenRefreshView.as_view(), name="token_refresh"),
    path("me", MyProfileViewSet.as_view()),
    path("me/password", MyPasswordView.as_view()),
]
