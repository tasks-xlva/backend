from rest_framework_nested import routers
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from routes.groups.views import GroupViewSet, MembershipViewSet, JoinGroupView
from routes.subjects.views import SubjectViewSet
from routes.tasks.views import TaskViewSet
from routes.files.views import FileViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register(r"groups/join", JoinGroupView)
router.register(r"groups", GroupViewSet)
router.register(r"subjects", SubjectViewSet)
router.register(r"tasks", TaskViewSet)
router.register(r"files", FileViewSet)

groups_router = routers.NestedDefaultRouter(router, r"groups", lookup="group")
groups_router.register("memberships", MembershipViewSet)

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
    path("redoc", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include("djoser.urls")),
    *router.urls,
    *groups_router.urls,
]
