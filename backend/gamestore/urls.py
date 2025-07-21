from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Game Store API",
        default_version='v1',
        description="Documentação dos endpoints da Game Store",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

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
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
