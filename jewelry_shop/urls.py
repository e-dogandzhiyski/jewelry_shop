from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('jewelry_shop.shop.urls')),
        path('profile/', include('jewelry_shop.accounts.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

