from rest_framework.viewsets import ReadOnlyModelViewSet

from api.category_api.serializers import CategorySerializer
from api.paginations import CustomPageNumberPagination
from store.models import Category


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPageNumberPagination
