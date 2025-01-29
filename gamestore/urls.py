from django.contrib import admin
from django.urls import path, re_path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('game-store/order/', include('order.urls')),
    re_path('game-store/product/', include('product.urls')),
]
