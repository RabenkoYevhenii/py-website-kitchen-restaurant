"""
URL configuration for py_website_kitchen_restaurant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from kitchen_restaurant.views import (
    index,
    DishTypeListView,
    DishListView,
    CookListView,
    DishDetailView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("", index, name="index"),
    path("dish_types/", DishTypeListView.as_view(), name="dish-types-list"),
    path("dish/", DishListView.as_view(), name="dishes-list"),
    path("cook/", CookListView.as_view(), name="cooks-list"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail")
]
