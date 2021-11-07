from rest_framework import routers
from app.groups.views import GroupViewSet


router = routers.DefaultRouter()
router.register(r"groups", GroupViewSet)

urlpatterns = [
    *router.urls,
]
