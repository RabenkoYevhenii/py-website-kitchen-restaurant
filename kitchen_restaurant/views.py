from django.shortcuts import render
from django.views import generic

from kitchen_restaurant.models import DishType, Cook, Dish


def index(request):
    """View function for the home page of the site."""

    num_dish_types = DishType.objects.count()
    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()

    context = {
        "num_dish_types": num_dish_types,
        "num_dishes": num_dishes,
        "num_cooks": num_cooks
    }

    return render(request, "kitchen_restaurant/index.html", context=context)


class DishTypeView(generic.ListView):
    model = DishType
    template_name = "kitchen_restaurant/dish_types_list.html"
    context_object_name = "dish_types_list"
