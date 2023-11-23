from django.test import TestCase
from django.urls import reverse
from kitchen_restaurant.models import DishType, Cook, Dish


class DishTypeModelTests(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Test Dish Type")

    def test_str_method(self):
        self.assertEqual(str(self.dish_type), "Test Dish Type")

    def test_get_absolute_url(self):
        url = reverse(
            "kitchen_restaurant:dish-type-detail",
            kwargs={"pk": self.dish_type.pk}
        )
        self.assertEqual(self.dish_type.get_absolute_url(), url)


class CookModelTests(TestCase):
    def setUp(self):
        self.cook = Cook.objects.create(first_name="John", last_name="Doe")

    def test_str_method(self):
        self.assertEqual(str(self.cook), "John Doe")

    def test_get_absolute_url(self):
        url = reverse(
            "kitchen_restaurant:cook-detail",
            kwargs={"pk": self.cook.pk}
        )
        self.assertEqual(self.cook.get_absolute_url(), url)


class DishModelTests(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Test Dish Type")
        self.cook = Cook.objects.create(first_name="John", last_name="Doe")
        self.dish = Dish.objects.create(
            name="Test Dish",
            description="Test description",
            price=10.99,
            dish_type=self.dish_type,
        )
        self.dish.cooks.add(self.cook)

    def test_str_method(self):
        self.assertEqual(str(self.dish), "Test Dish")

    def test_get_absolute_url(self):
        url = reverse(
            "kitchen_restaurant:dish-detail",
            kwargs={"pk": self.dish.pk}
        )
        self.assertEqual(self.dish.get_absolute_url(), url)

    def test_dish_type_related_name(self):
        self.assertEqual(self.dish_type.dishes.first(), self.dish)

    def test_cook_related_name(self):
        self.assertEqual(self.cook.dishes.first(), self.dish)
