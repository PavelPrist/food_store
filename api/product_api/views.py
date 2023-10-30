from rest_framework.viewsets import ReadOnlyModelViewSet

from api.paginations import CustomPageNumberPagination
from api.product_api.serializers import ProductSerializer
from store.models import Product


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPageNumberPagination
