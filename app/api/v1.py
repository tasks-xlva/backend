from rest_framework import routers
from app.groups.views import GroupViewSet
from app.subjects.views import SubjectViewSet
from app.tasks.views import TaskViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register(r"groups", GroupViewSet)
router.register(r"subjects", SubjectViewSet)
router.register(r"tasks", SubjectViewSet)

urlpatterns = [
    *router.urls,
]
