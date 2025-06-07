from rest_framework.routers import DefaultRouter
from django.urls import path, include
from user.viewsets import UserViewSet, RegisterView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),
]