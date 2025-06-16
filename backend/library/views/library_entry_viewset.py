from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from library.models import LibraryEntry
from library.serializers import LibraryEntrySerializer


class LibraryEntryViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = LibraryEntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return LibraryEntry.objects.filter(user=self.request.user)
