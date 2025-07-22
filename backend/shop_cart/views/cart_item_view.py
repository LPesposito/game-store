from rest_framework import viewsets, permissions
from shop_cart.models import CartItem, Cart
from shop_cart.serializers import CartItemSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    swagger_schema_fields = {
        "tags": ["shop_cart"]
    }
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)

    def perform_create(self, serializer):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        serializer.save(cart=cart)
