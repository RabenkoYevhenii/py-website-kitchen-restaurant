from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField()

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField()
    dish_type = models.ForeignKey(
        DishType,
        on_delete=models.CASCADE,
        related_name="dishes"
    )
    cooks = models.ManyToManyField(Cook, related_name="dishes")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
