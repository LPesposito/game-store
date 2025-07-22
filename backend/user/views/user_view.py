from rest_framework import viewsets, permissions
from user.models import CustomUser
from user.serializers import UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    swagger_schema_fields = {
        "tags": ["user"]
    }
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
