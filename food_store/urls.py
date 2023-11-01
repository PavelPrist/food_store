from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.users_api.urls')),
    path('api/', include('api.category_api.urls')),
    path('api/', include('api.product_api.urls')),
    path('api/', include('api.cart_api.urls')),
    path('swagger/', schema_view),
]

if settings.DEBUG:
    from api.schema import schema
    urlpatterns.append(
        path('', schema)
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # noqa
