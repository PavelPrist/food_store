from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.category_api.views import CategoryViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
