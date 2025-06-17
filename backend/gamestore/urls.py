from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('api/order/', include('order.urls')),
    path('api/product/', include('product.urls')),
    path('api/wallet/', include('wallet.urls')),
    path('api/shop-cart/', include('shop_cart.urls')),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    path('api/user/', include('user.urls')),
    path('api/library/', include('library.urls')),
]
