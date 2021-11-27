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


class MembershipViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = GroupMembershipSerializer
    queryset = Membership.objects.none()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Membership.objects.filter(group=self.kwargs["group_pk"])


class JoinGroupView(generics.CreateAPIView):
    serializer_class = JoinGroupSerializer
    queryset = Group.objects.all()
    permission_classes = [permissions.IsAuthenticated]
