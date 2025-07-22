from rest_framework import generics, permissions
from user.serializers import RegisterSerializer
from user.models import CustomUser

class RegisterView(generics.CreateAPIView):
    swagger_schema_fields = {
        "tags": ["user"]
    }
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
