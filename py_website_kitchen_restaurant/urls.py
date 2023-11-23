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
    DishTypeDetailView,
    CookDetailView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("", index, name="index"),
    path("dish_types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish/", DishListView.as_view(), name="dish-list"),
    path("cook/", CookListView.as_view(), name="cook-list"),
    path("dish_types/<int:pk>", DishTypeDetailView.as_view(), name="dish-type-detail"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("cook/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("dish_types/create", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish_types/<int:pk>/update", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dish_types/<int:pk>/delete", DishTypeDeleteView.as_view(), name="dish-type-delete"),
    path("dish/create", DishCreateView.as_view(), name="dish-create"),
    path("dish/<int:pk>/update", DishUpdateView.as_view(), name="dish-update"),
    path("dish/<int:pk>/delete", DishDeleteView.as_view(), name="dish-delete"),
]


app_name = "kitchen_restaurant"
