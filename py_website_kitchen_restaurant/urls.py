from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include(
        "kitchen_restaurant.urls",
        namespace="kitchen_restaurant")
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
