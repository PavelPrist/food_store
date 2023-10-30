from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.product_api.views import ProductViewSet

router = DefaultRouter()
router.register('product', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]
