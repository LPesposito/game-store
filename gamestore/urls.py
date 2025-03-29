from django.contrib import admin
from django.urls import path, re_path, include


urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    re_path('game-store/(?P<version>(v1|v2))/', include('order.urls')),
    re_path('game-store/(?P<version>(v1|v2))/', include('product.urls')),
]
