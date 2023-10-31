from rest_framework import status, viewsets
from rest_framework.response import Response

from api.cart_api.serializers import CartCreateSerializer, CartListSerializer
from api.paginations import CustomPageNumberPagination
from api.permissions import IsAuthorOrAdmin
from cart.models import Cart


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    pagination_class = CustomPageNumberPagination
    permission_classes = [IsAuthorOrAdmin]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CartListSerializer
        return CartCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


