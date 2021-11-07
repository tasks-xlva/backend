from rest_framework import routers
from app.groups.views import GroupViewSet
from app.subjects.views import SubjectViewSet


router = routers.DefaultRouter()
router.register(r"groups", GroupViewSet)
router.register(r"subjects", SubjectViewSet)

urlpatterns = [
    *router.urls,
]
