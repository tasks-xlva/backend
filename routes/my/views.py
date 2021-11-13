from rest_framework import permissions, generics
from .serializers import *


class MyProfileViewSet(generics.RetrieveUpdateAPIView):
    serializer_class = MyProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
