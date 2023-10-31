from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.cart_api.views import CartViewSet

router = DefaultRouter()
router.register('cart', CartViewSet, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
]
