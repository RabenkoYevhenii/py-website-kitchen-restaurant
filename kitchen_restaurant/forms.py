from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

from kitchen_restaurant.models import Dish, Cook


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Dish
        fields = "__all__"


class CookUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ("first_name", "last_name", "username")


class CookCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "years_of_experience"
        )
