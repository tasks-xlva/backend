from .serializers import *
from rest_framework import viewsets, permissions, mixins, generics
from rest_framework.decorators import action


class GroupViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = GroupSerializer
    queryset = Group.objects.none()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Group.objects.filter(membership__user=self.request.user)


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            Membership.objects.get(
                group_id=view.kwargs.get("group_pk"),
                user=request.user.pk,
            ).role
            == "ADMIN"
        )


class IsItself(permissions.BasePermission):
    def has_permission(self, request, view):
        return Membership.objects.get(pk=view.kwargs.get("pk")).user == request.user


class MembershipViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = GroupMembershipSerializer
    queryset = Membership.objects.none()

    def get_queryset(self):
        return Membership.objects.filter(group=self.kwargs["group_pk"])

    def get_permissions(self):
        if self.action == "destroy":
            return [permissions.IsAuthenticated(), IsItself()]
        elif self.action == "update" or self.action == "partial_update":
            return [permissions.IsAuthenticated(), IsAdmin()]
        return [permissions.IsAuthenticated()]


class JoinGroupView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = JoinGroupSerializer
    queryset = Group.objects.all()
    permission_classes = [permissions.IsAuthenticated]
