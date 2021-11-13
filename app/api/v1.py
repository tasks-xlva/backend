from rest_framework import routers
from routes.groups.views import GroupViewSet
from routes.subjects.views import SubjectViewSet
from routes.tasks.views import TaskViewSet
from routes.users.views import UserViewSet
from routes.me.views import MyProfileViewSet, MyPasswordView

from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"groups", GroupViewSet)
router.register(r"subjects", SubjectViewSet)
router.register(r"tasks", TaskViewSet)
router.register(r"users", UserViewSet)

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
    path("redoc", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    *router.urls,
    path("token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("users/me", MyProfileViewSet.as_view()),
    path("users/me/password", MyPasswordView.as_view()),
]
