from api.paginations import CustomPageNumberPagination
from djoser.views import UserViewSet
from rest_framework.permissions import IsAuthenticated

from users.models import User
from .serializers import CustomUserSerializer


class CustomUserViewSet(UserViewSet):

    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination
