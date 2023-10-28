from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.users_api.views import CustomUserViewSet


router = DefaultRouter()
router.register('users', CustomUserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
