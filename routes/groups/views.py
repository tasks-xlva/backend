from .serializers import *
from rest_framework import viewsets, permissions


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Group.objects.filter(membership__user=self.request.user)


class MembershipViewSet(viewsets.ModelViewSet):
    serializer_class = GroupMembershipSerializer
    queryset = Membership.objects.none()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Membership.objects.filter(
            user=self.request.user, group=self.kwargs["group_pk"]
        )
