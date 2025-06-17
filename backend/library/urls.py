from rest_framework.routers import DefaultRouter
from library.views.library_entry_viewset import LibraryEntryViewSet

router = DefaultRouter()
router.register(r'library', LibraryEntryViewSet, basename='library')

urlpatterns = router.urls
