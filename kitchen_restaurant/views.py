from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen_restaurant.forms import DishForm, CookUpdateForm, CookCreateForm
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

    return render(
        request,
        "kitchen_restaurant/index.html",
        context=context
    )


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "kitchen_restaurant/dish_type_list.html"
    context_object_name = "dish_type_list"


class DishTypeDetailView(generic.DetailView):
    model = DishType
    template_name = "kitchen_restaurant/dish_type_detail.html"
    context_object_name = "dish_type_detail"


class DishTypeCreateView(generic.CreateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen_restaurant/dish_type_form.html"
    success_url = reverse_lazy("dish-type-list")


class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen_restaurant/dish_type_form.html"
    success_url = reverse_lazy("dish-type-list")


class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("dish-type-list")
    template_name = "kitchen_restaurant/dish_type_confirm_delete.html"


class DishListView(generic.ListView):
    model = DishType
    queryset = Dish.objects.all().select_related("dish_type")


class DishDetailView(generic.DetailView):
    model = Dish


class DishCreateView(generic.CreateView):
    model = Dish
    form_class = DishForm


class DishUpdateView(generic.UpdateView):
    model = Dish
    form_class = DishForm


class DishDeleteView(generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("dish-list")


class CookListView(generic.ListView):
    model = Cook


class CookDetailView(generic.DetailView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("dishes__cooks")


class CookCreateView(generic.CreateView):
    model = Cook
    form_class = CookCreateForm


class CookUpdateView(generic.UpdateView):
    model = Cook
    form_class = CookUpdateForm


class CookDeleteView(generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("cook-list")
